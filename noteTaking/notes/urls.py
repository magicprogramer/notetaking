from django.urls import path, include
from . import views
app_name = "Note"
urlpatterns = [
    path("", views.index),
    path("vaults/<int:vault_id>", views.vault, name="Vault-Url"),
    path("notes/<int:note_id>", views.note, name = "Note-Url"),
    path("pragraphs/<int:pragraph_id>", views.pragraph, name = "Pragraph-Url"),
    path("pop", views.pop),
]