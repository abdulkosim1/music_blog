from django.db import models as m

# Create your models here.
class Category(m.Model):
    name = m.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Music(m.Model):
    title = m.CharField(max_length=50)
    duration = m.PositiveBigIntegerField()
    created_at = m.DateTimeField(auto_now_add=True)
    category = m.ForeignKey(Category, on_delete=m.CASCADE, related_name='musics')


    def __str__(self) -> str:
        return self.title