from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django import forms

from django.core.validators import RegexValidator
import re
from uuid import uuid4


from programming.utils import random_name_upload_to

from django.conf import settings

from django.core.urlresolvers import reverse




# Create your models here.

@python_2_unicode_compatible

def min_length_validator(value):
    if len(value) < 3 :
        raise forms.ValidationError("3글자 이상 입력하라고!!")




### 휴대폰 필드 개선 2번
def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    return RegexValidator(r'^01[016789]\d{7,8}$', message= '번호를 입력해주세요')(number)



class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)
        super(PhoneField, self).__init__(*args, **kwargs)
        self.validators.append(phone_validator)



"""
개선 1번

class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)

        위에거 설명
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 11

        super(PhoneField, self).__init__(*args, **kwargs) ###오버라이딩했으니까
        validator = RegexValidator(r'^01[016789]\d{7,8}$', message = '휴대폰번호 입력해여')
        self.validators.append(validator)

##### 계속해서 Charfield에다가 validator = @$@#$ 이런식으로 안하기 위해서 아예 클래스 받아오는것

"""



class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, validators = [min_length_validator], help_text = '포스팅 제목을 100자 이내로 써주세요')
    content = models.TextField()
    phone = PhoneField(blank =  True)

    photo = models.ImageField(blank = True, upload_to = random_name_upload_to)
    """
    photo = models.ImageField(blank = True, upload_to = "%Y/%m/%d") ## 이렇게하면 한 directory에 많은 파일이 안들어가게 된다.

    photo = models.ImageField(blank = True, upload_to = '/blog/post') ### photo에는 (ROOT뒤)이미지 경로만 가지고있다.
    """
    ### 먼저 MEDIA 루트찾고, 이미지 경로 넣어서 이미지 주소를 찾을 것이다.
    created_at = models.DateTimeField(auto_now_add=True) #### 저장될때 시간 갖는것 auto_now_add
    updated_at = models.DateTimeField(auto_now=True) #### 업데이트될때마다 시간 바꾸는것
    tags = models.ManyToManyField('Tag', blank = True)  ###문자로 써주게되면 클래스명 알아서 찾는다.
    #tags = models.ManyToManyField('auth_User') ## 이렇게 앱으로 지정해줘도 된다
    def __str__(self):
        return self.title

    def get_abolute_url(self): ###어디로 갈껀지 정해주는
        return reverse('blog:post_detail', args = [self.pk])




class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def  __str__(self):
        return self.message



class Senior(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(blank = True)
    #birth = models.DateField(auto_now=False, default = datetime.now())
    email = models.EmailField(default="hanyang@sap.com")
    career = models.TextField()
    ## created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Enterprise(models.Model):
    logo = models.ImageField(blank=True)
    name = models.CharField(max_length=20)
    #established = models.DateField(auto_now=False, default= datetime.now())
    email = models.EmailField(default = "hanyang@sap.com")
    url = models.URLField(max_length=200, default='http://localhost')

    def __str__(self):
        return self.name


class Youth(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)
    #birth = models.DateField(auto_now=False, default=datetime.now())
    email = models.EmailField(default = "seoul@sap.com")
    career = models.TextField()

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name









