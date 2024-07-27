from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        

product_delete_view = ProductDestroyApiView.as_view()

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateApiView.as_view()

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateApiView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailApiView.as_view()

class ProductListApiView(generics.ListAPIView):
    # not needed because it is covered in the ProductListCreateApiView
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == "GET":
        if pk is None:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        else:
            return Response({"invalid":"not a valid data"})