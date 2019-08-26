from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        print("This shit is working bro.")
        form = UserRegisterForm(request.POST)
        # username = form.cleaned_data.get('username')
        # print(username,"This shit is working")
        # return redirect('/')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username,"This shit is working")
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('/')
    else:
        #If there is no a post request just send an empty form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#The decoratior add functionality to the function is this case the login required functionality
@login_required
def profile(request):
    return render(request, 'users/profile.html')

"""
Messages is django.

message.debug
message.info
message.success
message.warning
message.error 

"""
