from rest_framework import serializers
from django.db.models import Avg
from .models import *
from applications.file.sersializers import FileSerializer
from applications.file.models import File


  
        
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    comments = CommentSerializer(many=True, read_only = True)
    files = FileSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Product
        fields = '__all__'
        
        
    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES
        product = Product.objects.create(**validated_data)

        for file in files_data.getlist('files'):
            File.objects.create(product=product, file=file)  
        return product
    
        
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.filter(like=True).count()
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(instance)
        if not instance.parent:
            rep.pop('parent')
        return rep
        
        
class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = ['rating']


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Favorite
        exclude = ['favorite']