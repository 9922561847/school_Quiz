from django.shortcuts import render

# Create your views here.
from quiz.models import Exam
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def home(request):
    return render(request,'index.html')
def test(request):
    exam = Exam.objects.all()
    paginator = Paginator(exam,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'test.html',{"exam":exam,"page_obj":page_obj})
def answer(request):
    ans = Exam.objects.all
    return render(request,'answer.html',{"ans":ans})
