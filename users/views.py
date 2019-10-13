from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
from django.views.generic import DetailView

#for rest frame work 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

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
            return redirect('login')
    else:
        #If there is no a post request just send an empty form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#The decoratior add functionality to the function is this case the login required functionality
# @login_required
# def profile(request, user):
#     print(request.user.profile)
#     print(type(request.user.profile))


    # return render(request, 'users/profile.html')


class Profile(DetailView):
    template_name = 'users/profile.html'
    queryset = User.objects.all()
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        # print(request.user)
        # print(user.profile.followed_by.all()[0])
        # print(type(user.profile.followed_by.all()[0]))
        return user 
        
    def get_context_data(self, *args, **kwargs):
        context = super(Profile,self).get_context_data(*args, **kwargs)
        # user_id = self.kwargs.get('id')
        # user = get_object_or_404(User,id=user_id)
        user = self.get_object()
        context.update({
            'posts' : user.posts.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
        })
        return context 
    def add_follow(self, request):
        user = self.get_object() 
        user.profile.followed_by.add(request.user.profile) 

def edit_profile(request):
    if request.method == "POST":

        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/edit_profile.html', context)
"""
Messages is django.

message.debug
message.info
message.success
message.warning
message.error 

"""

class ProfileFollowAPIToggle(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request,id=None, format=None):

        # id_ = self.kwargs.get("id")
        profile_obj = get_object_or_404(User, id=id)
        # url_ = profile_obj.get_absolute_url()
        user = self.request.user 
        updated = False 
        follow = False 
        if user.is_authenticated:
            if user.profile in profile_obj.profile.followed_by.all():
                follow = False
                print(user.profile ,"is un following ", profile_obj.profile)
                profile_obj.profile.followed_by.remove(user.profile)
            else:
                follow = True
                print(user.profile ,"is following ", profile_obj.profile)
                profile_obj.profile.followed_by.add(user.profile) 
            updated = True
        data = {
            "updated" : updated,
            "follow"  : follow,
            "list"    : profile_obj.profile.followed_by.all().values("name"),
        }
        print(data)
        return Response(data)
