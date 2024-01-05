from django.shortcuts import get_object_or_404
from .models import Note
def update_recent_notes(request, note):
    #request.session['Notes'] = []
    add_note(request, note)
    return retrive_notes(request)

def add_note(request, note):
    if "Notes" not in request.session:
        request.session['Notes'] = []
    N = Note.objects.filter(id=note)
    print(N.count())
    if N.count() == 0:
        print("bad")
        return
    N = N.first()
    print(N.id)
    request.session['Notes'].append([N.id, N.get_absolute_url(), N.title])
    request.session.modified = True
def retrive_notes(request):
    st = set()
    notes = []
    data =[]
    while len(request.session['Notes']):
        record = request.session['Notes'].pop()
        id = record[0]
        if id in st:
            continue
        obj = Note.objects.filter(id = id)
        if obj.count() == 0:
            continue
        obj = obj.first()
        st.add(id)
        print("ok")
        data.append([obj.id, obj.get_absolute_url(), obj.title])
        notes.append(obj)
    print(len(data))
    length = len(data)
    if length < 10:
        request.session['Notes'] = data
    else:
        request.sessoin['Notes'] = data[length - 10 : ]
    request.session.modified = True
    print(request.session['Notes'])
    print("here")
    return notes
    
