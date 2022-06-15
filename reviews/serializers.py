from xml.etree.ElementTree import Comment
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Category, Company, Product, ProductSite, ProductSize
# from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        # sizes =[
        #     ('full_size', 'url'),
        #     ('thumbnail', 'thumbail__100x100'),
        # ]

        sizes='product_headshot'
    )
    
    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']

class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
            'products': ('reviews.ProductSerializer', {'many' : True})
        }

    
class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']


 


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('reviews.CategorySerializer', {'many': True}),
            'sites': ('reviews.ProductSiteSerializer', {'many':True}),
            'comments':('reviews.CommentSerializer', {'many': True}),
            'image': ('reviews.ImageSerializer',  {'many': True}),
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'productsize': 'reviews.ProductSizeSerializer',
            'company': 'reviews.CompanySerializer',
        }
    

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product' : 'reviews.CategorySerializer',
            'user': 'revews.UserSerializer'
        
        }

# def validate_title(self, value):
#     if 'django' not in value.lower():
#         raise serializers.ValidationError("error message")

#         return value

# def validate(self, data):
#     if data['start'] > data['finish']:
#         raise serializers.ValidationError("finish must occur after start")
#     return data

# def create(self, validated_data):
#     return Comment.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.email = validated_data.get('email', instance.email)
#     instance.title = validated_data.get('content', instance.title)
#     instance.save()
#     return instance


