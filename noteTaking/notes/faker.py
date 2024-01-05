from faker import Faker
from django.contrib.auth.models import User
from .models import *
import random
from django.db import transaction
fake = Faker()
def populate():
    with transaction.atomic():
        populate_vaults()
        populate_note()
        populate_links()
        populate_pragraph()
        populate_tags()
        populate_note_tag()
def populate_tags():
    for i in range(100):
        Tag.objects.create(name = fake.word())
    
def populate_vaults():
    users = User.objects.all()
    for user in users:
        for i in range(random.randint(1, 5)):
            Vault.objects.create(name = fake.word(), user = user)
def populate_note():
    vaults = Vault.objects.all()
    for vault in vaults:
        for i in range(random.randint(1, 8)):
            Note.objects.create(vault = vault, user = vault.user, title = fake.sentence())
def populate_links():
    notes = Note.objects.all()
    for note in notes:
        for i in range(random.randint(0, 1)):
            Link.objects.create(note = note, url=fake.url())
def create_delta(text):
    ops = []
    at = [{"bold" : True}, {"italic" : True}]
    ops.append({"attributes" : at[random.randint(0, len(at) - 1)]})
    ops.append({"insert" : text})
    ops.append({"insert" : "\\n"})
    return {"ops" : ops}
def populate_pragraph():
    notes = Note.objects.all()
    delta_string = '{"ops": [{"insert": "Man radio main dog first. Claim during role safe."}, {"insert": "\\n"}]}'
    for note in notes:
        for i in range(random.randint(1, 4)):
            Pragraph.objects.create(note = note, content= delta_string)
def populate_note_tag():
    notes = Note.objects.all()
    tags = Tag.objects.all()
    for note in notes:
        note.Tags.set(random.sample(list(tags), random.randint(1, 3)))
