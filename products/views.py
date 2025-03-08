from rest_framework.response import Response
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
	def list(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)

	def create(self, request):
		print('====>', request)
	def retrieve(self, request):
		print('====>', request)
	def update(self, request):
		print('====>', request)
	def delete(self, request):
		print('====>', request)