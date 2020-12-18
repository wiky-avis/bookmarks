from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Расширение модели пользователя
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

# Поле photo имеет тип ImageField. Для работы с ним нам необходимо установить 
# библиотеку изображений Pillow - pip install Pillow


# для связи пользователей
class Contact(models.Model):
    user_from = models.ForeignKey(
        'auth.User', related_name='rel_from_set', on_delete=models.CASCADE
        )
    user_to = models.ForeignKey(
        'auth.User', related_name='rel_to_set', on_delete=models.CASCADE
        )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follws {}'.format(self.user_from, self.user_to)

# Динамическое добавление поля following в модель User
User.add_to_class('following', models.ManyToManyField(
    'self', through=Contact, related_name='followers', symmetrical=False
    ))