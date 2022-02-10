from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# python manage.py makemigrations
# python manage.py migrate
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="posts")
    title = models.CharField(max_length=120,verbose_name="Başlık")
    context = models.TextField(verbose_name="Açıklama")
    # context = RichTextField(verbose_name="Açıklama")
    puplish_date = models.DateTimeField(verbose_name="Kayıt Tarihi",auto_now_add=True)
    #image = models.FileField(null=True,blank=True)
    #ImageField sadece resim kabul eder.Kullanımı FileField ile aynıdır. pip install Pillow ile bağımlılıkları kurulmalıdır.
    image = models.ImageField(null=True,blank=True)
    #burada unique True yaptıgımız için DB'yi silip yeniden olusturmamız gerkecek .
    #Çünkü daha once biz unique vermediğimiz için o id olustumustu
    slug = models.SlugField(unique=True,editable=False,max_length=130)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        #return "/post/list/{}".format(self.id)
        return reverse('post:detail',kwargs={'slug':self.slug})
    def get_update_url(self):
        #return "/post/list/{}".format(self.id)
        return reverse('post:update',kwargs={'slug':self.slug})
    def get_delete_url(self):
        #return "/post/list/{}".format(self.id)
        return reverse('post:delete',kwargs={'slug':self.slug})
    def get_create_url(self):
        #return "/post/list/{}".format(self.id)
        return reverse('post:creat')
    def get_date(self):
        return str(self.puplish_date)
    def get_unique_slug(self):
        slug = slugify(self.title.replace("ı","i"))
        uniq_slug = slug
        counter = 1
        while Post.objects.filter(slug=uniq_slug).exists():
            uniq_slug = "%s-%d"%(slug,counter)
            counter += 1
        return uniq_slug
    def save(self, *args,**kwargs):
        #if not self.slug:
            #slug alani yoksa title 'den dolduruyoruz
            # self.slug = slugify(self.title.replace("ı","i"))
            #self.slug = self.get_unique_slug()
        self.slug = self.get_unique_slug()
        #Esas save metodunu cağırıyoruz.
        return super(Post,self).save(self,*args,**kwargs)
    class Meta:
        #siralamak için siralayacağımız isimleri koyuyoruz.
        # Basina - koymamız tersine göre sıralama yapılacağı anlamına gelir.
        ordering=['-puplish_date']

class Comment(models.Model):
    post = models.ForeignKey('post.Post',models.CASCADE,related_name='comments')
    name = models.CharField(max_length=200,verbose_name='isim')
    comment = models.TextField(verbose_name='yorum')
    creat_date = models.DateTimeField(auto_now_add=True)
