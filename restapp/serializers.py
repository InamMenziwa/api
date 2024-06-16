from rest_framework import serializers
from .models import Titles

class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ["type","title","director","cast","country","date_added","release_year","rating","duration","listed_in","description"]