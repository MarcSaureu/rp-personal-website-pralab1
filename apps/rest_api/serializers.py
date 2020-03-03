from rest_framework import serializers
from . import models

class PostSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.Post
		fields = '__all__'
		depth = 1

class CategorySerializer(serializers.ModelSerializer):
	posts = PostSerializer(read_only=True, many=True)

	class Meta:
		model = models.Category
		fields = '__all__'
