from rest_framework import serializers

from apps.user.models import SaveListStellaris


class SaveListStellarisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveListStellaris
        fields = ['user_id', 'save_id', 'name']
