from rest_framework import serializers
from library.models import Library,Rack




class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Library
        fields=['name','address']


class RackSerializer(serializers.ModelSerializer):
    library = LibrarySerializer(read_only=True)
    libraryId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=Library.objects.all(), source='library')
    class Meta:
        model=Rack
        fields=['id','number','location','library','libraryId']