from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import DetailView
from blog.models import Post , Comment
from blog.models import Senior
from blog.models import Enterprise
from blog.models import Youth
from django.http import Http404
from django.contrib.auth.decorators import login_required


from blog.forms import PostForm, CommentForm
from django.contrib import messages


# Create your views here.
### generic -> Detail뷰를 쓸수있다 5대뷰를 가져다가 쓸수있음 post_detail 참조

def index(request):
    return render(request, 'blog/index.html')
def bio(request):
    return render(request, 'blog/bio.html')
def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html',{'post_list':post_list})

post_detail = DetailView.as_view(model=Post)

def senior_list(request):
    senior_list = Senior.objects.all()
    return render(request, 'blog/senior_list.html',{'senior_list':senior_list})

senior_detail = DetailView.as_view(model=Senior)

def enterprise_list(request):
    enterprise_list = Enterprise.objects.all()
    return render(request, 'blog/enterprise_list.html', {'enterprise_list':enterprise_list})

enterprise_detail = DetailView.as_view(model=Enterprise)

def youth_list(request):
    youth_list = Youth.objects.all()
    return render(request, 'blog/youth_list.html', {'youth_list' : youth_list})

youth_detail = DetailView.as_view(model=Youth)






from django.contrib.auth.decorators import login_required

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid() :
            #post = form.save()
            ### post = form.save(commit=False)
            ### 세이브를 늦추고
            ### post.author = request.user
            ### 작성자는 모델에서 외래키로 줄텐데, 사용자에게 권한을 줄경우
            ### 다른사람들의 아이디가 보이니까, 입력값으로 받는게 아님
            ### 고로 자동으로해야하는데, 그리까 commit을 false로놔서
            ### 저장시기를 늦춰야한다.
            ### post.save()
            ### 이렇게하면 중간에 변환을 시킬 수 있어서 디비에 쿼리를 덜 날려도 됨
            #return redirect('blog.views.post_detail', post.pk)
            ###인자가 한개있는 post_detail을 찾아라!
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect(post)

    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form,})
@login_required
def post_edit(request, pk):
    post = Post.get_object_or_404(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid() :
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_form.html', {'form': form,})
@login_required
def comments_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit= False)
            comment.author = request.user
            comment.post = get_object_or_404(Post,pk = post_pk)
            comment.save()
            ## 메세지 쓰는법 알아보기
            messages.debug(request, '새로운 댓글을 등록했습니다.')
            return redirect(comment.post) ## redirect comment.post
    else:
         form = CommentForm()
    return render(request,'blog/comment_form.html',{'form' : form})
@login_required
def comments_edit(request, post_pk,pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid() :
            comment =form.save(commit= False)
            comment.post = Post.get_object_or_404(pk = post_pk)
            comment.save()
            return redirect(comment.post)
    else:
        form = CommentForm(instance = comment)
    return render(request, 'blog/comment_form.html', {'form': form,})


"""
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
"""

"""
class PostDetailView(DetailView):
    def get_object(selfm queryset=None):

        try :
            return Post.objects.get(pk=self.)


"""




"""
class PostDetailView(DetailView):

    def get_object(self, queryset=None):
        ##slef.kwargs : year, month, day,pk
        ##self.kwargs['year']
        return post.objects.get(pk=self.kwargs['pk'])
"""



"""
def senior(request):
    senior_list = Senior.objects.all()
    return render(request, 'blog/seior.html',{'senior_list':senior_list})
"""


"""
#### render()-> 2번째 인자 템플릿 3번째 인자 딕셔너리 -> 가져갈 변수받아오는 곳####
### Funtion based view###
### Class based view###
"""






"""
장식자
@require_POST
@login_required    ####장식자는 우래코드 감싸는 구조
def post_new(request):
    return render(request, 'blog/post_form.html')


결국 이거 ㅇㅇㅇㅇ post_new = require_POST(login_required(post_new))


import time

def cache(fn):
    cached = {}
    def wrap(x,y):
        key = (x, y)
        if key not in cached:
            cached[key] = fn(x,y)
        return cached[key]
    return wrap


@cache ===> 장식자
add = cache(add) ——> 풀어쓰면 이 의미

def add ( x, y) :
    time.sleep(1)
    return x+y


"""


