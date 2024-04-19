from django.shortcuts import render,redirect
from django.http import HttpResponse
from hsblimited.models import User,LoanApplication
from hsblimited.backend import login,logout,authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from hsbfinance.utility import send_otp

def homepage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('userIndex')

        else:
            message = {"message": "invalid username or password"}
            return render(request, "index.html", message)

    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")


def partners(request):
    return render(request, "partners.html")

def createAccount(request):
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        hashed_password = make_password(password)
        user=User.objects.get(email=email)
        if user is None:
            try:
                en=User(email=email,fullname=name,mobile=mobile,gender=gender,password=hashed_password)
                en.save()
                return redirect('homepage')
            except:
                return HttpResponse("oops! something went wrong")
                
        else:
            message={"message":"email already exist please login"}
            return render(request,"create-account.html",message)

    return render(request,"create-account.html")

def forgetPassword(request):
    if request.method=="POST":
        email=request.POST.get("email")
        print(email)
        user=User.objects.filter(email=email).values()
        print(user[0]['email'],user[0]['password'])
        if user.exists():
            otp=send_otp(request)
            send_mail(
                "One-Time Password (OTP) for Password Reset",
                "Your one time otp for password reset is: "+otp,
                "rjgulshan4498@gmail.com",
                [email],
                fail_silently=False,
            )
           
            request.session['email']=user[0]['email']
            return redirect('otpVerification')
        else:
            message = {"message": "user doesnot exist"}
            return render(request, "forget-password.html", message)

    return render(request,"forget-password.html")

def userIndex(request):
    if 'username' in request.session.keys():
        username = request.session.get("name", None)
        username={'username': username}
        return render(request, "user-account/index.html",username)
    else:
        return render(request, "index.html")
   

def loanApply(request):
    if 'username' in request.session.keys():
        username = request.session.get("name", None)
        username={'username': username}
        if request.method == 'POST':
            loanType = request.POST.get('loanType')
            loanAmount = request.POST.get('loanAmount')
            street = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            address = f"{street} {city} {state} {pincode}"

            useremail = request.session.get("username")  # Use get() with a default value
            user = User.objects.get(email=useremail)  # Retrieve the User object
            
        
            try:  
                en=LoanApplication(user_email=user,loan_type=loanType,loan_amount=loanAmount,address=address,approved_amount=0,status="Pending")
                en.save()
                message = {"message": "YOU HAVE SUCCESSFULLY APPLIED FOR THE LOAN"}
                data={'message':message,'username':username,}
                return render(request, "user-account/status.html",data)
            except:
                return HttpResponse("oops! something went wrong")    
        return render(request, "user-account/loan-apply.html",username)   
    else:
        return render(request, "index.html")


def loan(request):
    if 'username' in request.session.keys():
        useremail = request.session.get("username")
        data=LoanApplication.objects.filter(user_email=useremail)
        username = request.session.get("name", None)
        username={'username': username}
        if data.exists():
           
           data={"data": data,'username':username}
           return render(request, "user-account/loan.html",data) 
        else:
            data={"data": data,'username':username}
            return render(request, "user-account/loan.html",data) 

    else:
        return render(request, "index.html")

def loanStatus(request):
    if 'username' in request.session.keys():
        useremail = request.session.get("username")
        data=LoanApplication.objects.filter(user_email=useremail)
        username = request.session.get("name", None)
        username={'username': username}
        if data.exists():
            message = {"message": "YOU HAVE SUCCESSFULLY APPLIED FOR THE LOAN"}
            data={'message':message,'username':username,}
            return render(request, "user-account/status.html",data) 
        else:
            message = {"message": "YOU HAVE NOT APPLY FOR ANY LOAN YET"}
            data={'message':message,'username':username,}
            return render(request, "user-account/status.html",data)      
        
    else:
        return render(request, "index.html")
    

def otpVerification(request):
    if request.method=="POST":
        user_otp=request.POST.get('otp') 
        email=request.session.get("email",None)
        if email is not None:       
            otp=request.session['otp']
            print(otp)
            if user_otp==otp:
                return redirect('resetPassword')
            else:
                message = {"message": "Please Enter Valid OTP"}
                return render(request,"otp-verification.html",message)
        else:
                message = {"message": "user is not verified"}
                return render(request, "index.html", message)
    return render(request,"otp-verification.html")
    
def resetPassword(request):
    if request.method=="POST":
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        email=request.session.get("email",None)
        if email is not None:
            if new_password==confirm_password:
                hashed_password = make_password(new_password)
                
            
                user=User.objects.get(email=email)
            
                user.password=hashed_password
                user.save()
                request.session.flush()
                message2 = {"message2": "password changed successfully"}
                return render(request, "index.html", message2)
            else:
            
                message = {"message": "confirm password didnot match"}
                return render(request,"password-reset.html",message)
        else:
            message = {"message": "user is not verified"}
            return render(request, "index.html", message)
    return render(request,"password-reset.html")

def profile(request):
    if 'username' in request.session.keys():
        email=request.session.get("username",None)
        user=User.objects.filter(email=email).values()
        data={'data': user[0]}
        return render(request, "user-account/profile.html",data)
    else:
        return render(request, "index.html")

def edit_profile(request):
    if 'username' in request.session.keys():
        email=request.session.get("username",None)
        user=User.objects.filter(email=email).values()
        data={'data': user[0]}
        if request.method=="POST":
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            password=request.POST.get('password')
            gender=request.POST.get('gender')
            hashed_password = make_password(password)
            try:
                
                user=User.objects.get(email=email)
                user.fullname=name
                user.mobile=mobile
                user.password=hashed_password
                user.gender=gender
                user.save()
                request.session["name"] = user.fullname
                message = {"message": "Profile Updated successfully"}
                return redirect('profile')
            except:
                message = {"message": "Failed to update Profile Please try after sometime"}
                return render(request, "user-account/profile.html", message)
               
        return render(request, "user-account/editProfile.html",data)
    else:
        return render(request, "index.html")
    

def userLogout(request):
    logout(request)
    return redirect('homepage')