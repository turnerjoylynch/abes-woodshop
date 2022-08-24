""" A module for handling Shop Items requests """
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