from django.shortcuts import render,redirect
import sys
from backoffice_engine.forms import *
from django.contrib import messages
from backoffice_engine.models import *
import random
from django.core.mail import send_mail
from meme_mania import settings
from datetime import date,timedelta
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from backoffice_engine.utils import text2vision
from django.utils.timezone import now
from django.utils import timezone
import traceback
import re


# Create your views here.
def index(request):
        return render(request,'index_2.html')
        
def profile(request):
    if 'id' in request.session:
        id = request.session.get('id')
        e = User.objects.get(id=id)
        s = Subscription.objects.get(user=e)
        return render(request, 'profile.html',{'e':e,'s':s})
    else:
        return redirect("/login/")    
def about(request):
    
        f = Feedback.objects.all()
        fc = f.count()
        uc = User.objects.all().count()
        sc = Subscription.objects.all().count()
        ic = Generated_image.objects.all().count()
        return render(request,'about.html',{'f':f,'fc':fc,'uc':uc,'sc':sc,'ic':ic})
    
    
def blog_details(request):
    
        f = Feedback.objects.all()
        return render(request,'blog_details.html',{'f':f})
   
    

def blog(request):
    
        return render(request,'blog.html')
    
    
def contact(request):
    
        return render(request,'contact.html')
    
    
def e(request):
   
        return render(request,'e.html')
    

def img(request):
   
        return render(request,'img.html')
    

def login(request):
    if request.method == 'POST':
        useremail = request.POST.get("email")
        pwd = request.POST.get("password")

        e_count = User.objects.filter(email=useremail, password=pwd).count()
        if e_count == 1:
            e = User.objects.get(email=useremail)

           
            try:
                subscription = Subscription.objects.get(user=e)

                if subscription.end_date <= timezone.now().date():
                    
                    free_plan = Plan.objects.get(name="FREE")  
                    subscription.plan = free_plan
                    subscription.start_date = timezone.now().date()
                    subscription.end_date = timezone.now().date() + timedelta(days=30)
                    subscription.status = 'active'
                    subscription.pending_credit = Plan.credit
                    subscription.save()

            except Subscription.DoesNotExist:
                
                free_plan = Plan.objects.get(name="FREE")  
                Subscription.objects.create(
                    user=e,
                    plan=free_plan,
                    start_date=timezone.now().date(),
                    end_date=timezone.now().date() + timedelta(days=30),
                    status='active',
                    pending_credit=0
                )
                
            request.session['id'] = e.id
            request.session['name'] = e.name
            request.session['email'] = e.email
            request.session['password'] = e.password 

            return redirect("/index/")

        else:
            messages.error(request, "Invalid Email or Password")
            return render(request, "login.html", {'e': e_count})
    else:
        return render(request, 'login.html')

def portfolio_details(request):
   
        return render(request,'portfolio_details.html')
    

def portfolio(request):
   
        return render(request,'portfolio.html')
    
    
def price(request):
    if request.method == 'POST':
        
        if 'id' not in request.session:
            return redirect('/login/')
        user_id = request.session.get('id')
        plan_id = request.POST.get('planid')
        user = User.objects.get(id=user_id)

        
        plan = Plan.objects.get(id=plan_id)
        
        Subscription.objects.create(user=user, plan=plan, status='active')
        return redirect('/price/')

    
    if 'id' in request.session:
        user_id = request.session['id']
        active_sub = Subscription.objects.filter(user_id=user_id, status='active').first()
        active_plan_id = active_sub.plan.id if active_sub else None
    else:
        active_plan_id = None

    all_plan = Plan.objects.filter(duration_days=30, is_active=True)
    all_plan_yearly = Plan.objects.filter(duration_days=365, is_active=True)

    return render(request, 'price.html', {
        'all_plan': all_plan,
        'all_plan_yearly': all_plan_yearly,
        'active_plan_id': active_plan_id,
    })

def services(request):
   
        return render(request,'services.html')
    

def t_params(request):
   
        return render(request,'t_params.html')
    

def team(request):
   
        return render(request,'team.html')
    
def index_1(request):
    return render(request,'index_1.html')

def index_3(request):
    return render(request,'index_3.html')


def registration(request):
    if request.method == "POST":
        f = UserRegistration(request.POST)

        email = request.POST.get("email")  
        mobile_number = request.POST.get("mobile_number")  
        
        if not re.fullmatch(r'\d{10,15}', mobile_number):
            messages.error(request, "Enter a valid mobile number (10–15 digits).")
            return render(request, "registration.html", {"form": f})
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please use another email.")
            return render(request, "registration.html", {"form": f})
            
        if f.is_valid():
            try:
                user = f.save()
                free_plan = Plan.objects.filter(
                    name="FREE",
                    duration_days=30,
                    is_active=True
                ).first()

                if free_plan:
                    start_date = date.today()
                    end_date = start_date + timedelta(days=free_plan.duration_days)

                    Subscription.objects.create(
                        user=user,
                        plan=free_plan,
                        start_date=start_date,
                        end_date=end_date,
                        status='active',
                        pending_credit=free_plan.credit
                    )
                else:
                    print("No free plan found. Please create one in Plan table.")

                messages.success(request, "Registration successful! You can now login.")
                return redirect("/login/")
                
            except:
                print("----------------------", sys.exc_info())
                messages.error(request, "Something went wrong. Try again later.")
                return render(request, "registration.html", {"form": f})
        else:
            messages.error(request, "Please fix the errors in the form.")
            return render(request, "registration.html", {"form": f})
    else:
        f = UserRegistration()
        return render(request, "registration.html", {"form": f})
     
def send_otp(request):
    if request.method == "POST":
        otp1 = random.randint(10000, 99999)

        
        e = request.POST.get('email')

        if not e:
            messages.error(request, "Email is required!")
            return render(request, 'send_otp.html')
        
        request.session['temail'] = e  
        
        obj = User.objects.filter(email=e).count()
        if obj == 1:
            User.objects.filter(email=e).update(otp=otp1, otp_used=0)

            subject = 'This is your One Time Password [OTP] for Text2Vision website. DO NOT SHARE WITH ANYONE.'
            message = subject + '\n\nYour OTP is: ' + str(otp1)

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [e]

            send_mail(subject, message, email_from, recipient_list)

            return render(request, 'reset_pass.html')
        else:
            messages.error(request, "INVALID EMAIL ID")
            return render(request, 'send_otp.html')
    return render(request, 'send_otp.html')


def reset_pass(request):
    if request.method == "POST":
        otp = request.POST.get("otp", "").strip()
        pwd = request.POST.get("password", "")
        cpwd = request.POST.get("confirm_password", "")
        e = request.session.get('temail')

        
        if not e:
            messages.error(request, "Session expired. Please try again.")
            return redirect("/send_otp/")  

        
        if not otp.isdigit() or len(otp) != 5:
            messages.error(request, "OTP must be a 5 digit number.")
            return render(request, "reset_pass.html")

        
        if len(pwd) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return render(request, "reset_pass.html")

        
        if pwd != cpwd:
            messages.error(request, "Password and confirm password do not match.")
            return render(request, "reset_pass.html")

        
        val = User.objects.filter(email=e, otp=otp, otp_used=0).count()
        if val != 1:
            messages.error(request, "Invalid or used OTP.")
            return render(request, "reset_pass.html")

        
        User.objects.filter(email=e).update(password=pwd, otp_used=1)
        messages.success(request, "Password reset successfully! You can now log in.")
        return redirect("/login/")  

    return render(request, "reset_pass.html")


def update_profile(request,id):
    e = User.objects.get(id = id)  
    if request.method == "POST":
        f = UserUpdate(request.POST,instance = e)
        print(f"Update User Form Error = {f.errors}")
        if f.is_valid():
            try:
                 f.save()
            except:
                print(sys.exc_info())
        return redirect('/profile/')
    else:
         return render(request,"profile.html",{'e':e})
     
def logout(request):
    try:
        del request.session["id"]
        del request.session["name"]
        del request.session["email"]
        del request.session["password"]
        return redirect('/login/')
    except:
        pass
    return render(request,'login.html')

def delete_account(request,id):
    if 'id' in request.session:
        e = User.objects.get(id=id)
        e.delete()
        return redirect('/registration/')
    else:
        return render(request,'profile.html')

def generate_image(request):
    if 'id' in request.session:
        category = Category.objects.all()
        prompts = Suggested_prompt.objects.all()
        return render(request, 'generate_image.html', {'category': category,"prompts":prompts})
    else:
        return redirect('/login/')


def show(request):
    if 'id' in request.session:
        if request.method == 'POST':
            try:
                category_id = request.POST.get('category')
                instruction = request.POST.get('instruction')
                creativity = request.POST.get('creativity')
                user_id = request.session.get('id')

                user = User.objects.get(id=user_id)
                subscription = Subscription.objects.filter(
                    user=user,
                    status='active',
                    start_date__lte=now().date(),
                    end_date__gte=now().date()
                ).first()

                if not subscription:
                    return render(request, "show.html", {'error': "You do not have an active subscription."})
                if subscription.pending_credit <= 0:
                    return render(request, "show.html", {'error': "Your credits are finished. Please renew your plan."})

                category = Category.objects.get(id=category_id)
                userprompt = f"{category.name}, {instruction}"
                generated_image_object = text2vision(userprompt, creativity, user, category.name, instruction)

                subscription.pending_credit -= 1
                subscription.save()

                return render(request, "show.html", {
                    'category': category,
                    'instruction': instruction,
                    'creativity': creativity,
                    'generated_image_url': generated_image_object.image,
                    'remaining_credits': subscription.pending_credit
                })
            except User.DoesNotExist:
                return redirect("/login/")
            except Category.DoesNotExist:
                return HttpResponse("Invalid category selected", status=400)
            except Exception as e:
                traceback.print_exc()
                return render(request, "show.html", {'error': "An error occurred. Please try again later."})
        else:
            return redirect("/generate-image/")
    else:
        return redirect("/login/")

def gallery(request):
    if 'id' in request.session:
        user_id = request.session['id']
        user = User.objects.get(id=user_id)
        
        images = Generated_image.objects.filter(user=user)
        cat = Category.objects.all()
        return render(request, 'gallery.html', {'images': images,'cat':cat})
    else:
        return redirect('/login/')


@csrf_exempt
def payment(request): 
    uid=request.POST.get("userid")
    pid=request.POST.get("planid")
    print("-----------user id ----------",uid,pid)
    
    p=Plan.objects.get(id=pid)
    sd=date.today()
    ed = sd + timedelta(days=p.duration_days)
    s= Subscription.objects.filter(user=uid).update(plan=pid,start_date=sd,end_date=ed,status='active',pending_credit=p.credit)
    request.session["plan"]=int(pid)
    print("---------session---------",request.session['plan'])
    request.session["id"]=int(uid)
    request.session["plan"]=int(pid)

    return render (request,'payment.html')

def feedback(request):
    if 'id' in request.session:
        if request.method == "POST":
            comment = request.POST.get("feedback")
            user_id = request.session.get("id")
            user = User.objects.get(id=user_id)
            Feedback.objects.create(user=user, comment=comment)
            return render(request, 'feedback.html', {'feedback_sent': True})  
        else:
            return render(request, 'feedback.html')
    else:
        return redirect('/login.html/')

def check(request):
    uid = request.session['id']
    s = Subscription.objects.get(user=uid)
    end = s.end_date
    print("--------------------------------------------------------------",end)
    if date.today() >= end:
        logout(request)
        return HttpResponse("YOUR PLAN IS EXPIRED")
    return HttpResponse ("")