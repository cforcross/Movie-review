from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
CATEGORY_CHOICES=(
    ('action','ACTION'),
    ('drama','DRAMA'),
    ('comedy','COMEDY'),
    ('romance','ROMANCE')
)

LANGUAGE_CHOICES =(
    ('english','ENGLISH'),
    ('german','GERMAN'),
)

STATUS_CHOICES=(
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED')
)






class Movie(models.Model):
    title = models.CharField(max_length=1000)
    describtion = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner')
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=50)
    year_of_production= models.DateField(auto_now=False, auto_now_add=False)
    views_count = models.IntegerField(default=0)
    movie_trailer = models.URLField()

    created = models.DateTimeField(default = timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

LINK_CHOICES =(
    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK'),
)

class MovieLInks(models.Model):
    movie = models.ForeignKey(Movie,related_name='movie_watch_link',on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.movie
    