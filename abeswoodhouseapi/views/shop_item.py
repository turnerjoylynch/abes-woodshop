""" A module for handling Shop Items requests """
from cgi import print_exception
from turtle import title
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from abeswoodhouseapi.models import ShopItem


class ShopItemView(ViewSet):
    """ Shop Items Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a shop item """
        try:
            shop_item = ShopItem.objects.get(pk=pk)
            serializer = ShopItemSerializer(shop_item)
            return Response(serializer.data)
        except ShopItem.DoesNotExist as e:
            return Response({"Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
    
    def list(self, request):
        """ Handle a GET request for all of the shop items """
        shop_items = ShopItem.objects.all()
        serializer = ShopItemSerializer(shop_items, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a shop item """
        # incoming_user = request.auth.user (I have a question about this)
        new_shop_item = ShopItem.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            price=request.data["price"],
            type=request.data["type"],
        )
        serializer = ShopItemSerializer(new_shop_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """ Handles a PUT request for a shop item """
        editing_shop_item = ShopItem.objects.get(pk=pk)
        
        editing_shop_item.title = request.data["title"]
        editing_shop_item.description = request.data["description"]
        editing_shop_item.price = request.data["price"]
        editing_shop_item.type = request.data["type"]
        
        editing_shop_item.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a shop item """
        try:
            shop_item = ShopItem.objects.get(pk=pk)
            shop_item.delete()
        except ShopItem.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ShopItemSerializer(serializers.ModelSerializer):
    """ JSON serializer for shop items """
    class Meta:
        model = ShopItem
        fields = (
            'id',
            'title',
            'description',
            'price',
            'type')