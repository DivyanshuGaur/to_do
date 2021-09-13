from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from to_do_app.models import Todo


# Create your views here.
def homepage(request):
        all_todo=Todo.objects.all().order_by("-date")
        return render(request,'index.html',{

            "todo_items" : all_todo
        }
        
        )



def add_to(request):
    activity=request.POST["add"]
    date=timezone.now()

    model_obj=Todo(date=date,content=activity)



    model_obj.save()
    print('Data saved')

    print(model_obj)

    return HttpResponseRedirect('/')




def delete(request,todo_id):
    print('Deleted call ')
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')



