from . import views
from django.urls import path
app_name ="api"
urlpatterns = [
    path("retrieve_vaults", views.retrieve_vaults, name = "r_vaults"),
    path("retrieve_notes/<int:vault_id>", views.retrieve_notes, name = "r_notes"),
    path("retrieve_notes", views.note_search, name="note_search")
]