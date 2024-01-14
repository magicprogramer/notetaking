from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from .faker import populate
from .helpers import update_recent_notes
from .forms import VaultForm, NoteForm, ParagraphForm

def index(request):
    if request.method == "GET":
        user = request.user
        if user.is_authenticated:
            valuts = Vault.objects.filter(user=user)
        else:
            valuts = {}
            user = None
        return render(request, "notes/index.html", {"vaults" : valuts, "user" : user})
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
    update_recent_notes(request, note_id)
    return render(request, "notes/note.html", {"note" : note, "pragraph" : pragraph, "links" : links, "tags" : tags})
@login_required
def pragraph(request, pragraph_id):
    pragraph = Pragraph.objects.get(id=pragraph_id)
    return render(request, "notes/pragraph.html", {"p" : pragraph})
@login_required
def pop(request):
    if request.user.is_staff == False:
        return redirect("Note:main")
    populate()
    return HttpResponse("done")
@login_required
def createvault(request):
    if request.method == "GET":
        form = VaultForm()
        return render(request, "notes/vaultform.html", {"form" : form})
    else:
        form = VaultForm(request.POST, user = request.user)
        print("here")
        if form.is_valid():
            form.save()
            return redirect("Note:main")
        return redirect("Note:error", msg = "sorry something is wrong")
    
@login_required
def createNote(request, vault_id=None):
    if request.method == "GET":
        form = NoteForm()
        return render(request, "notes/Noteform.html", {"form" : form})
    else:
        if vault_id == None:
            return HttpResponse("None")
        vault = get_object_or_404(Vault, id = vault_id)
       # print(vault)
       # print(vault.name)
        form = NoteForm(request.POST, user = request.user, vault = get_object_or_404(Vault, id = vault_id))
        if form.is_valid():
            instance = form.save()
            return redirect("Note:Vault-Url", vault_id = vault_id)
        return HttpResponse("Note error")
@login_required
def createParagraph(request, note_id = None):
    if request.method == "GET":
        form = ParagraphForm()
        return render(request, "notes/paragraphform.html", {"form" : form, "note_id" : note_id})
    else:
        print(request.POST['content'])
        form = ParagraphForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.note = Note.objects.get(id = note_id)
            instance.save()
            print(note_id)
            return redirect("Note:Note-Url", note_id = note_id)
        return redirect("Note:error", msg = "sorry invalid paragraph")
@login_required
def delete_paragraph(request, paragraph_id, note_id=None):
    Pragraph.objects.get(id = paragraph_id).delete()
    return redirect("Note:Note-Url", note_id = note_id)
@login_required
def update_paragraph(request, note_id, paragraph_id):
    paragraph = get_object_or_404(Pragraph, id = paragraph_id)
    print(paragraph_id)
    if request.method == "GET":
        form = ParagraphForm(instance=paragraph)
        return render(request, "notes/paragraphform.html", {"form" : form, "note_id" : note_id, "update" : True, 
                                                            "paragraph_id" : paragraph_id})
    else:
        form = ParagraphForm(request.POST, instance=paragraph)
        if form.is_valid():
            instance = form.save()
            print(paragraph.id, instance.id)
            return redirect("Note:Note-Url", note_id=note_id)
        return redirect("Note:error", msg = "sorry something is wrong")
@login_required
def search(request):
    if request.method == "POST":
        notes = Note.objects.filter(title__contains=request.POST['search'], user = request.user)
        return render(request, "notes/search.html", {"notes" : notes})
def error(request, msg):
    return render(request, "notes/error.html", {"msg" : msg})
def aboutus(request):
    return render(request, "notes/aboutus.html")