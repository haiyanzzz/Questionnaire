from django.db.models.aggregates import Count
from django.shortcuts import render
from app01 import models
# Create your views here.
def index(request):
    Questionnaire_obj = models.Questionnaire.objects.all()
    #查询每一个班级的学生个数
    class_obj = models.ClassList.objects.all()
    li = []
    for i in class_obj:
        li.append(i.student_set.all().count())
    answer_obj = models.Answer.objects.all()
    l = []
    for i in answer_obj:
        # print(i.student_id)
        l.append(i.student_id)
    # L=len(l)
    return render(request,"index.html",locals())

def questionedit(request):
    return render(request,"questionedit.html")