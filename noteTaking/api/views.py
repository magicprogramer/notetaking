from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import VaultSerializer, NoteSerializer
from notes.models import Vault, Note
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated

from rest_framework.authentication import BasicAuthentication

@api_view(["GET"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def retrieve_vaults(request):
    qs = Vault.objects.filter(user = request.user)
    serializer = VaultSerializer(qs, many = True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def retrieve_notes(request, vault_id):
    qs = Note.objects.filter(vault = vault_id, user = request.user)
    serializer = NoteSerializer(qs, many = True)
    return Response(serializer.data)
def note_search(request):
    if request.method == "GET":
        return render(request, "api/vaultform.html")
    else:
        vault_id = request.POST['v_id']
        return redirect("api:r_notes", vault_id=vault_id)
