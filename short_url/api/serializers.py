from rest_framework.serializers import ModelSerializer, SerializerMethodField

from short_url.models import ShortURL


class ShortURLCreateSerializer(ModelSerializer):
    short_url = SerializerMethodField('_get_short_url')

    class Meta:
        model = ShortURL
        fields = ('url', 'short_url')
        read_only_fields = ('short_url',)
        extra_kwargs = {'url': {'write_only': True}}

    @staticmethod
    def _get_short_url(obj):
        return obj.get_short_url()

    def create(self, validated_data):
        return ShortURL.objects.get_or_create(url=validated_data['url'])[0]
