
from django.shortcuts import render, redirect
from .models import Post, Outgoing, Look, Upload
from .forms import UserRegisterForm, SendForm, UserRegisterForm1, UploadForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#imports for Class  based views
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from collections import Iterator
from django.template.loader import render_to_string
import csv,io




from django.http import HttpResponseRedirect


# Create your views here.
posts = [
  {
    'author': "Ronald Mosomi",
    'title' : "Learning python",
    'content':'The book is about to teach you how to programin pythona nd leave other languages',
    'date_posted':'19th Feb 2019',
    },
{
      'author':'Benard Mosomi',
      'title': 'Learning Perl',
      'content':'The book is about to teach you how to programin perl',
      'date_posted':'18th Feb 2019',
     },

{
        'author':'Levy Molel',
        'title': 'Learning Linux',
        'content':'The book is about to teach you how to use linux and leave all other os',
        'date_posted':'10th Feb 2019',
        }


  ]

def home(request):
    return render(request, 'sms/home.html')

def about(request):
    return render(request, 'sms/about.html')

def blog(request):
    context = {
    'posts':Post.objects.all()


    }
    print(posts)

    return render(request, 'sms/blog.html', context)


def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your account {username} has been created! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'sms/simple.html', {'form':form})




@login_required
def profile(request):
    return render(request, 'sms/profile.html')





#class based views here

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering =['-date_posted']



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SendSmsView(LoginRequiredMixin, CreateView):
    model = Outgoing
    fields = ['phone_numbers','text_message']

    def form_valid(self, form):
        m = form.cleaned_data['phone_numbers'].splitlines()

        # for n in form.cleaned_data['phone_numbers'].splitlines():
        for n in m:


            form.instance.phone_numbers=n
            form.instance.text_message=form.cleaned_data['text_message']
            form.instance.user=self.request.user
            form.instance.access_code=self.request.user.profile.access_code
            form.instance.service_id=self.request.user.profile.service_id


        print (m)
        return super().form_valid(form)
            # print(form.cleaned_data['phone_numbers'])


#
# class SendSmsView(LoginRequiredMixin, CreateView):
#     model = Outgoing
#     fields = ['phone_numbers','text_message']
#
#     def form_valid(self, form):
#
#         numbers = self.get(self.fields[0])
#         myNumbers = iter(numbers)
#         message = self.get(self.fields[1])
#
#         for number in numbers:
#             temp = []
#             temp.append(number)
#             temp.append(message)
#         return temp
#
#         form.instance.user=self.request.user
#         form.instance.access_code=self.request.user.profile.access_code
#         form.instance.service_id=self.request.user.profile.service_id
#         return super().form_valid(form)

class SmsReportView(ListView):
    model = Outgoing



@login_required
def send(request):
    if request.method == 'POST':
        if request.POST.get('phone_numbers') and request.POST.get('text_message'):
            m =  request.POST.get('phone_numbers').splitlines()
            print(m)
            print(len)

            for n in m:
                s = ''.join(n.split())
                p=f"{254}{s[-9:]}"
                smsout = Outgoing()
                smsout.phone_numbers = p
                smsout.text_message = request.POST.get('text_message')
                smsout.service_id = request.user.profile.service_id
                smsout.access_code = request.user.profile.access_code
                smsout.user= request.user
                smsout.save()


            return redirect('profile')

    else:
            return render(request,'sms/send.html')

        # return render(request, 'sms/send.html')


def createbook(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                look=Look()
                look.title= request.POST.get('title')
                look.content= request.POST.get('content')
                look.save()

                return redirect('profile')

        else:
                return render(request,'sms/createbook.html')
# list2 = []

# @login_required
# def upload2(request, *arg, **kwargs):
#
#     if request.method == "POST":
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             datas = request.FILES["csv"]
#             file_data = datas.read().decode("utf-8")
#             list2.append(file_data)
#
#
#
#
#
#
#
#
#
#
#             print(list2)
#
#
#
#             form.instance.author=request.user
#             form.save()
#
#
#             return redirect ('upload')
#
#
#
#
#
#     else:
#         form = UploadForm()
#     #
#     # return render(request, 'sms/upload.html', {'form':form})
#
def upload(request):
        template = 'sms/upload2.html'
        prompt = {'order':'order of the CSV should be'}

        if request.method =="GET":
            return render(request, template, prompt)
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'This is not a csv file')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        row = csv.reader(io_string, delimiter=',', quotechar="|")
        # next(io_string)
        print(row)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):

            print(io_string)
            # index = column[0].index('first_name')
            # print(index)
            # # _, created = Contact.objects.update_or_create(
            #     first_name = column[0],
            #     last_name=column[1],
            #     email=column[2],
            #     ip_address=column[3],
            #     message=column[4]
            # # )

        context = {}
        print(context)

        return render(request, template, context)
