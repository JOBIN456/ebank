from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect
from bank_app.models import user

# Create your views here.
def dmo(request):
    return render(request,"home.html")
def apply(request):
    if request.method == "POST":
        try:
            name=request.POST.get('name')
            dob=request.POST.get('dob')
            age=request.POST.get('age')
            gender=request.POST.get('gender')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            address=request.POST.get('address')
            branch=request.POST.get('branch')
            branches=request.POST.get('branches')
            account_type=request.POST.get('account_type')
            debit_card = request.POST.get('debitCard') is not None
            credit_card = request.POST.get('creditCard') is not None
            cheque_book = request.POST.get('chequeBook') is not None
            og=user(name=name,
                    dob=dob,age=age,
                    gender=gender,
                    phone=phone,
                    email=email,
                    address=address,
                    branch=branch,
                    sub_branch=branches,
                    account_type=account_type,
                     debit_card=debit_card,
                    credit_card=credit_card,
                    cheque_book=cheque_book,)
            
            og.save()
            
            print("og created")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, "apply.html", {"error": str(e)})
            
    return render(request,"apply.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('apply')
        else:
            messages.info(request,'Enter a valid username password')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password,)

                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
     auth.logout(request)
     return redirect('/')
     