from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # URL 패턴을 만들어주는 장고의 내장함수 reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)  # 별칭 : verbose_name 폼 화면에서 레이블로 사용되는 문구
    # 단어와 단어 사이에 '-' 로 이어져 있는 값 e.g. the-46-year-old-man
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.ßß')
    content = models.TextField('CONTENT')
    created_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now_add=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)  # tuple 형삭에서 ',' 는 구분되어지는 큰 의미를 가지기 때문에 반드시 넣어준다.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
