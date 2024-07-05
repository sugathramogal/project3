from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is first project")
    
def demo(request):
     return HttpResponse("this is second project")

def demo2(request):
    return HttpResponse("this is thired project")    
def demo3(request):
    A=10
    B=5
    C=A+B
    D="sugathra"
    response_text = f"{D}-{C}"

    print(B)

    return render(request,'demo3.html',{'response_text':response_text,'cc':D})

def  demo4(request):

    context={

        'cars':[
            {
                'brand':'ford',
                'model':'mustang',
                'year' :'1964',
            },
            
            {
                'brand':'Ford',
                'model':'Bronco',
                'year' :'1970',
            },
            {
                'brand':'Volvo',
                'model':'P1800',
                'year' :'1964',   
            }]
         }
    return render(request, 'demo4.html', context)
