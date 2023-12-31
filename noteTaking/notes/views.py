from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from .faker import populate
@login_required
def index(request):
    if request.method == "GET":
        user = request.user
        valuts = Vault.objects.filter(user=user)
        return render(request, "notes/index.html", {"vaults" : valuts})
    else:
        return HttpResponse("sorry not yet")
@login_required
def vault(request, vault_id):
    user = request.user
    vlt = Vault.objects.filter(id = vault_id, user = user).first()
    posts = Note.objects.filter(vault = vlt)
    for post in posts:
        print(post.get_absolute_url())
       # print("next")
    return render(request, "notes/vaults.html", {"vault" : vlt, "posts" : posts})
@login_required
def note(request, note_id):
    note = Note.objects.get(id = note_id)
    pragraph = Pragraph.objects.filter(note=note)
    links = Link.objects.filter(note = note)
    tags = note.Tags.all()
    print(len(tags))
    return render(request, "notes/note.html", {"note" : note, "pragraph" : pragraph, "links" : links, "tags" : tags})
@login_required
def pragraph(request, pragraph_id):
    pragraph = Pragraph.objects.get(id=pragraph_id)
    return render(request, "notes/pragraph.html", {"p" : pragraph})
@login_required
def pop(request):
    populate()
    return HttpResponse("done")