from django.shortcuts import get_object_or_404, render
from django.utils import timezone 
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from datetime import datetime
from .models import Post 

# Create your views here.

class PostListView(ListView):
    template_name = 'insta/home.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'
    for post in queryset:
        post.published()
    

    def posted_time_onIG(self):
        posts = Post.objects.all()
        for post in posts:
            Id = post.id 
            print(post)
            #print(post_id)
            Now = datetime.now()
            time_created = post[Id-1].created_date
            if (Now.day - post.created_date.day == 0):
                if (Now.hour - post.created_date.hour == 0):
                    posted_time = str(Now.minute - time_created.minute) + " MINUTES AGO"
                    print("------------>",posted_time, time_created)
                else:
                    posted_time = str(Now.hour - time_created.hour) + " HOURS AGO"
                    print("------------>",posted_time, time_created)
                
            else:
                posted_time = str(Now.day - time_created.day) +" DAYS AGO maybe wrong  "+ str(Now.day - post.created_date.day) + "post id = " + str(post.id) 
                print("------------>",posted_time)
            return posted_time
            print("....................................................................")

