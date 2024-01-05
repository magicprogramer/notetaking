from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Vault, Note
class VaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vault
        fields = ["name", "id"]
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title"]