from django.contrib import admin
from .models import Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ["title","puplish_date","slug"]
    list_display_links= ["puplish_date"]
    list_filter = ["puplish_date"]
    search_fields = ["title","context"]
    list_editable = ["title"] #link olmamasi gerekiyor
    # prepopulated_fields = {
    #     "slug" : ("title",)
    # }
    class Meta:
        model=Post



admin.site.register(Post,PostAdmin)