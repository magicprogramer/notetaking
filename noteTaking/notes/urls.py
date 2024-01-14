from django.urls import path, include
from . import views
app_name = "Note"
urlpatterns = [
    path("", views.index, name="main"),
    path("vaults/<int:vault_id>", views.vault, name="Vault-Url"),
    path("vault/create", views.createvault, name='vault-create'),
    path("notes/<int:note_id>", views.note, name = "Note-Url"),
    path("notes/note/create/<int:vault_id>", views.createNote, name = "note-create"),
    path("pragraphs/<int:pragraph_id>", views.pragraph, name = "Pragraph-Url"),
    path("paragraph/create/<int:note_id>", views.createParagraph, name="paragraph-create"),
    path("paragraph/delete/<int:note_id>/<int:paragraph_id>", views.delete_paragraph, name = "paragraph-delete"),
    path("paragraph/update/<int:note_id>/<int:paragraph_id>", views.update_paragraph, name= "Paragraph-Update"),
    path("pop", views.pop),
    path("notes/notes/search", views.search, name="search"),
    path("error/<str:msg>", views.error, name="error"),
    path('notes/aboutus', views.aboutus, name="aboutus")
]