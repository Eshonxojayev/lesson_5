from django.shortcuts import render
from django.views import View
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer, CategorySerializer, CommentSerializer, CartSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from .models import Product, Category, Comment, Cart
from customers.models import Customers
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')

    @action(detail=True, methods=['GET'])
    def top_products(self, request, *args, **kwargs):
        products = self.queryset.order_by('-price')[:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')

    @action(detail=True, methods=['GET'])
    def categories(self, request, *args, **kwargs):
        categories = Category.objects.all()
        page = self.paginate_queryset(categories)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')

    @action(detail=True, methods=['GET'])
    def top_comments_like(self, request, *args, **kwargs):
        comments = self.queryset.order_by('-created_at')[:5]
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CartAPIView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')


class ProductListView(View):
    def get(self, request):
        search = request.GET.get('search')
        print(search)
        if not search:
            products = Product.objects.all()
            categories = Category.objects.all()
            featured_products = Product.objects.all()
            context = {'products': products,
                       "categories": categories,
                       "featured_products": featured_products,
                       }
            return render(request, 'vegetable_web/shop.html', context)
        else:
            products = Product.objects.filter(title__icontains=search)
            featured_products = Product.objects.all()
            categories = Category.objects.all()
            context = {'products': products,
                       "categories": categories,
                       "featured_products": featured_products,
                       }
            return render(request, 'vegetable_web/shop.html', context)


class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        featured_products = Product.objects.all()
        categories = Category.objects.all()
        customers = Customers.objects.all()
        comments = Comment.objects.all()
        user_id = request.user.id
        " userning malumotlari faqat comment yozish uchun test qilishga olingan "
        user = User.objects.get(id=user_id)
        print(user)
        context = {
            'product': product,
            "categories": categories,
            'featured_products': featured_products,
            'customers': customers,
            'comments': comments,
            'user': user,
        }
        return render(request, 'vegetable_web/shop-detail.html', context)

    def post(self, request, id):
        """ bu methodni customer emas user yozsa qabul qiladigan qilmoqchi edim lekin ozor kamchiliklar bor shuning uchun bu ishlamaydi """
        user = request.user
        text = request.POST.get('comment')
        comment = Comment.objects.create(text=text, user=user)
        product = Product.objects.get(id=id)
        product.comments.add(comment)
        product.save()
        product = Product.objects.get(id=id)
        featured_products = Product.objects.all()
        categories = Category.objects.all()
        customers = Customers.objects.all()
        comments = Comment.objects.all()
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        context = {
            'product': product,
            "categories": categories,
            'featured_products': featured_products,
            'customers': customers,
            'comments': comments,
            'user': user,
            }
        return render(request, 'vegetable_web/shop-detail.html', context)


class CartView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        Cart.objects.create(product=product)
        # Mahsulotlar uchun umumiy narxni va yetkazib berish narxini hisoblash
        total_price = 0
        shipping_price = 0
        for cart_product in Cart.objects.all():
            total_price += cart_product.product.price
            shipping_price = cart_product.shipping_price
        cart = Cart.objects.all()
        context = {
            'product': product,
            'cart': cart,
            'total_price_ship': total_price + shipping_price,
            'total_price': total_price,
            'shipping_price': shipping_price,
        }
        return render(request, 'vegetable_web/cart.html', context)