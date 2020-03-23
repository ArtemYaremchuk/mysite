from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from rewives.models import Comment
from django.utils import timezone


# функция
def index(request):   # (3) и смотрит здесь на index и делает request
    comment = Comment.objects.all()  # извлекает все элементы из таблицы
    return render(request, 'rewives/rewives.html', {"comment": comment})


def leave_rewive(request):      # функция делающая "POST" и сохраняющая комментарий в БД
    if request.method == "POST":
        rewives = Comment()
        rewives.author_name = request.POST.get("name")
        rewives.comment_text = request.POST.get("text")
        rewives.pub_date = timezone.now()
        rewives.save()
    return HttpResponseRedirect("/rewives/")

