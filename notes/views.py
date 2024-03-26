from django.shortcuts import render, redirect
from .models import Note, Tag, Fact


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        # Verifica se a tag existe ou não
        if tag in [tag_obj.name for tag_obj in Tag.objects.all()]:
            tag = Tag.objects.get(name=tag)
            note = Note(title=title, content=content, tags=tag)
        else:
            tag = Tag(name=tag)
            tag.save()
            tag = Tag.objects.get(name=tag.name)
            note = Note(title=title, content=content, tags=tag)
        note.save()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/index.html', {'notes': all_notes})
    
def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect('index')

def update(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/update.html', {'note': note})
    
def cancel(request):
    return redirect('index')

def all_tags(request):
    all_tags_obj = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags_obj})

def tag(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    notes = Note.objects.filter(tags=tag)
    return render(request, 'notes/tag.html', {'notes': notes, 'tag': tag})

def prova(request):
    if request.method == 'POST':
        desc_fact = request.POST.get('descricao')
        # Cria o fato interessante
        if desc_fact not in [fact.descricao for fact in Fact.objects.all()]:
            fact = Fact(descricao=desc_fact, curtidas=0)
            fact.save()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
    all_facts = Fact.objects.all()
    print(all_facts)
    qtd_facts = len(all_facts)
    return render(request, 'notes/page.html', {'facts': all_facts, 'qtd_facts': qtd_facts})

def curtiu(request, fact_id):
    fact = Fact.objects.get(pk=fact_id)
    fact.curtidas += 1
    fact.save()
    return redirect('prova')