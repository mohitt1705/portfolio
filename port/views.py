from django.shortcuts import render,redirect
from .models import*
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def index(request):
    about=About.objects.first()
    skill=Skills.objects.all()
    eduction=Eduction.objects.all()
    experince=Experince.objects.all()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save() #agar model form he
            messages.success(request,"Your message has been sent succesfully")
            return redirect('index') #reload karke success message show karega
        
    else:
        form=ContactForm()    
    
    
    return render(request,'index.html',{'about':about,'skill':skill,'eduction':eduction,'experince':experince,'form':form})