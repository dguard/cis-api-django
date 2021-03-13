from rest_framework import serializers
from .models import Valute


class ValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valute
        fields = ('external_id', 'num_code', 'char_code', 'nominal', 'name', 'value', 'previous')

