from rest_framework import serializers

from .models import Movies

def get_name(value):
    """
        This method is a validator for a field 'name' specified in name field
    """
    if (len(value)==0):
        raise serializers.ValidationError('Value should not be empty')

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[get_name]) #validator
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

#1. Field-Level Validator:

    def validate_name(self,value):
        if(len(value)<2):
            raise serializers.ValidationError("Name is too short")
        else:
            return value


#object level

    def validate(self,data):
        # if data['name']==data['description']:
        #     raise serializers.ValidationError('name and description should be diferent')
        # else:
        #     return data

        name=data.get('name')
        description=data.get('description')

        if Movies.objects.filter(name=name,description=description).exists():
            """
            Check if object with same values exists if it exists 
            """
            raise serializers.ValidationError('Object already exist')
        else:
            return data




#In serializers we can customize validators and there are three types of validators
#1.field-level validator
#2.object-level validator
#3.validators

