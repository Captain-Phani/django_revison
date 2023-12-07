from rest_framework import serializers

from .models import Movies

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()

    def create(self, validated_data):
        """
        this method creates an object in the database
        **valid_data is equivalent to name=validated_data['name],description=validated_data['description']
        """
        return Movies.objects.create(**validated_data)



    def update(self, instance, validated_data):
        """
        Update method is responsible for making changes
        This method takes three params, self, instance,validated_data
        self:points to current instance
        instance:aldready existing data
        validated_data:data to be replaced with existing data

        instance.name=validated_data.get('name',instance.name)
        it extracts the data with the 'name' if 'name' exists it will be assigned to instance.name or else
        it considers existing value
        """
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance

