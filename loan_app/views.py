from django.shortcuts import render, redirect
from .models import Applicant


def index(request):
    return render(request, 'index.html')  # This is fine


def start(request):
    
    return render(request, 'apply.html')  # working fine


def apply(request):
   
    return render(request, 'apply.html')  # working fine

def result(request):
    
    Applicant.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        employed=request.POST['employed'],
        # approved_amount=request.POST['approved_amount'],
        credit=(request.POST['credit']), # removed int(request.POST['credit'])
        income=(request.POST['income']),
    )
    # new_applicant = Applicant.objects.all()
    # request.session["applicant_id"] = new_applicant

    # if  a.credit > 600 and a.income > 60000 and a.employed == True:
    #     Applicant.objects.approved_amount == .80*(4*(a.income))
    # a = Applicant.objects.all()
    return redirect('/success') 
    # else:
    #     return redirect('/pending')

        
def success(request):
    for a in Applicant.objects.all():
        print(a)
    # Applicant.objects.GET(
    #         first_name=request.GET['first_name'],
    #         last_name=request.GET['last_name'],
    #         email=request.GET['email'],
    #         employed=request.GET['employed'],
    #         approved_amount=request.GET['approved_amount'],
    #         credit=(request.GET['credit']),
    #         income=(request.GET['income']),
    #     )
    # a = Applicant.objects.all()
    if  int(a.credit) > 600 and int(a.income) > 60000 and a.employed == True:
        a.approved_amount == .80*(4*(a.income)) 
     
        return redirect('/approved')
    else: 
        
        return redirect('/denied')

def approved(request):
    context =  {
                "data": Applicant.objects.last()
            }
    
    return render(request,'result.html',context)

def denied(request):
    
    
        context =  {
                "data": Applicant.objects.last()
            }
    

    # if 'applicant_id' in request.session:
    #     loans = Applicant.objects.filter(id=request.session['applicant_id'])
    #     if loans:
    #         context =  {
    #             "loans": loans[0],
    #         }
        return render(request, 'denied.html', context)
    # return redirect("/")