from django.shortcuts import render
from django.contrib import messages
from .models import Login
# Create your views here.
def home(request):
    if request.method == 'POST':
        try:
            operator = Login.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request,'index.html')
        except Login.DoesNotExist as e:
            messages.error(request,'Username/Password Invalid!!')
            return render(request,'home.html')
    else:
        return render(request,'home.html')

def index(request):
    return render(request,'index.html')


def changepass(request):
    return render(request,'changepass.html')
def donar_register(request):
    return render(request,'donar_register.html')
def donar_today_collect(request):
    return render(request,'donar_today_collect.html')
def donar_mini_statement(request):
    return render(request,'donar_mini_statement.html')
def donar_detail_statement(request):
    return render(request,'donar_detail_statement.html')
def own_mother_register(request):
    return render(request,'own_mother_register.html')
def own_today_collect(request):
    return render(request,'own_today_collect.html')
def own_mini_statement(request):
    return render(request,'own_mini_statement.html')
def own_detail_statement(request):
    return render(request,'own_detail_statement.html')
def own_to_donar(request):
    return render(request,'own_to_donar.html')
def pasturization(request):
    return render(request,'pasturization_form.html')
def past_today_collect(request):
    return render(request,'past_today_collect.html')
def past_mini_statement(request):
    return render(request,'past_mini_statement.html')
def past_detail_statement(request):
    return render(request,'past_detail_statement.html')
def culture(request):
    return render(request,'culture.html')
def culture_today_collect(request):
    return render(request,'culture_today_collect.html')
def culture_mini_statement(request):
    return render(request,'culture_mini_statement.html')
def culture_detail_statement(request):
    return render(request,'culture_detail_statement.html')
def discard(request):
    return render(request,'discard.html')
def discard_today_collect(request):
    return render(request,'discard_today_collect.html')
def discard_mini_statement(request):
    return render(request,'discard_mini_statement.html')
def discard_detail_statement(request):
    return render(request,'discard_detail_statement.html')
def dispense(request):
    return render(request,'dispense.html')
def dispense_today_collect(request):
    return render(request,'dispense_today_collect.html')
def dispense_mini_statement(request):
    return render(request,'dispense_mini_statement.html')
def dispense_detail_statement(request):
    return render(request,'dispense_detail_statement.html')



