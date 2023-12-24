from rest_framework import serializers

from watchlist.models import Watchlist,StreamPlatform

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Watchlist
        fields="__all__"

    def validate(self,data):
        title=data.get('name')
        storyline=data.get('storyline')

        if Watchlist.filter(title=title,storyline=storyline).exists():
            raise serializers.ValidationError("Object Already Exists")

        else:
            return data



class StreamPlatformSerializers(serializers.ModelSerializer):
    class Meta:
        model=StreamPlatform
        fields="__all__"

    def validate(self,data):
        name=data.get('name')
        about=data.get('about')
        website=data.get('website')

        if StreamPlatform.filter(name=name,about=about,website=website).exists():
            raise serializers.ValidationError("Object Already Exists")
        else:
            return data


