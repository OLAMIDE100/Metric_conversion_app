from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


# Create your views here.

def Conv(request):

    return render(request,'base.html')


@method_decorator(csrf_exempt,name='dispatch')
def ConvTemp(request):


    conversion = ['Celsius ==> Fahrenheit','Fahrenheit ==> Celsius']

    data = {}

    Value = request.POST.get("Value")
    Units =  request.POST.get("Units")


    if Value == '':

        data = {"answer": f" ENTER VALUE"}

        

    else:

        

        if Units == 'Fahrenheit ==> Celsius':
            result = (int(Value) - 32) *  0.5556
            data = {"answer": f"{result} celsuis"}

            

        elif Units == 'Celsius ==> Fahrenheit':
            result = (int(Value) * 1.8) + 32 
            data = {"answer": f"{result} fahrenheit"}


    return render(request,'home.html',{'units':conversion,"mide":data.get('answer')})
    
@method_decorator(csrf_exempt,name='dispatch')
def ConvTime(request):


    conversion = ['seconds ==> minutes','minutes ==> seconds']

    data = {}

    Value = request.POST.get("Value")
    Units =  request.POST.get("Units")


    if Value == '':

        data = {"answer": f" ENTER VALUE"}

        

    else:

        

        if Units == 'seconds ==> minutes':
            result = int(Value) / 60
            data = {"answer": f"{result} minutes"}

            

        elif Units == 'minutes ==> seconds':
            result = int(Value) * 60 
            data = {"answer": f"{result} seconds"}


    return render(request,'home.html',{'units':conversion,"mide":data.get('answer')})