from django.contrib import admin
from blog.models import (Post, Senior, Enterprise, Youth, Comment, Tag)
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','get_title_length']
    list_display_links = ['id','title']

    def get_title_length(self, post):
        return len(post.title)



admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
"""
class Senior(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(blank = True)
    birth = models.DateField(auto_now=False, default = datetime.date.today)
    email = models.EmailField(default="hanyang@sap.com")
    career = models.TextField()

    def __str(self):
        return self.name
"""

class SeniorAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id','name']

admin.site.register(Senior, SeniorAdmin)

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links =['id','name']

admin.site.register(Enterprise, EnterpriseAdmin)


class YouthAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_display_links=['id','name']

admin.site.register(Youth, YouthAdmin)












