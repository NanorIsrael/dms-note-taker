import random
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView

from .producer import publish

from .models import Product, User
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
	def list(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		publish('product_list', serializer.data)
		return Response(serializer.data)

	def create(self, request):
		serializer = ProductSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		publish('product_created', serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def retrieve(self, request, pk=None):
		products = Product.objects.get(id=pk)
		serializer = ProductSerializer(products)
		return Response(serializer.data)

	def update(self, request, pk=None):
		product = Product.objects.get(id=pk)
		serializer = ProductSerializer(instance=product, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		publish('product_update', serializer.data)
		return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

	def destroy(self, request, pk=None):
		product = Product.objects.get(id=pk);
		product.delete()
		publish('product_update', pk)
		return Response({"status": True}, status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
	def get(self, _):
		users = User.objects.all()
		user = random.choice(users)
		return Response({"id": user.id})