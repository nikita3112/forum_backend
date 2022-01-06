from django.db import models
from users.models import User
from django.utils.timezone import now


# Create your models here.
class Thread(models.Model):
    title = models.CharField('Заголовок', max_length=128)

    def __str__(self):
        return self.title

class Theme(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=255, null=True)
    text = models.TextField('Текст')
    datetime = models.DateTimeField('Дата публкации', default=now)

    def __str__(self):
        return self.title


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    text = models.TextField('Текст сообщения')
    datetime = models.DateTimeField('Дата публикации', default=now)

    def __str__(self):
        return f'Сообщение от {self.user.name}'
