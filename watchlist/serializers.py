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

    # watchlist_movies=serializers.StringRelatedField(many=True,read_only=True,source='watchlist') #returns only string related fields
    # watchlist_url=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='watchlist-movie',source='watchlist') # returns Urls

    watchlist=WatchlistSerializer(many=True,read_only=True)

    def to_representation(self, instance):
        """
        This method is provided by django itself to modify our data while being converted into JSON(serialization)
        The reason to use this method is if a streaming platoform does not have a list of movies then
        the field watchlist is displaying as empty list[] instead of displaying empty list we can modify
        that field to display message that 'movies are yet to be added'
        Moreover it will return message only if watchlist is empty otherwise it returns watchlist
        :param instance:
        :return:
        """
        representation=super().to_representation(instance)
        if not representation['watchlist']:
            representation['watchlist']='Movies are yet to be added'
        return representation

    def validate(self,data):
        name=data.get('name')
        about=data.get('about')
        website=data.get('website')

        if StreamPlatform.filter(name=name,about=about,website=website).exists():
            raise serializers.ValidationError("Object Already Exists")
        else:
            return data


