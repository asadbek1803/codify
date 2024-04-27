from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username,  email, password=None):
        if not email:
            raise ValueError('Elektron pochtani kiritishingiz shart!')

        if not username:
            raise ValueError('Username kiritilishi shart!')

        if not first_name:
            raise ValueError('First name kiritilishi shart!')

        if not last_name:
            raise ValueError('Last name kiritilishi shart!')





        user = self.model(
            first_name = first_name,
            last_name= last_name,

            username=username,
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, username,  email, password):
        user = (
            self.create_user(
                first_name,
                last_name,
                username,

                email = email,
                password=password

            )
        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    location = (
        ('fergana', 'Fergana'),
        ('andijan', 'Andijan'),
        ('namangan', 'Namangan'),
        ('tashkent', 'Tashkent'),
        ('other', 'Other')
    )
    dev_typse = (
        ('oldin ishlamaganman', 'Oldin ishlamaganman'),
        ('junior', 'Junior dasturchiman'),
        ('middle', 'Middle dasturchiman'),
        ('senior', 'Senior dasturchiman')
    )
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telegram = models.URLField(default="https://t.me/username")
    instagram = models.URLField(default="https://instagram.com/username")
    facebook = models.URLField(default="https://facebook.com/username")
    me = models.CharField(max_length=50, choices=dev_typse, blank=True, null=True)
    working_location = models.CharField(max_length=24, choices=location, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    working_name = models.CharField(max_length=200, null=True, blank=True)


    is_verified = models.BooleanField(default=False)
    score = models.IntegerField(blank=True, null=True)
    starting_test = models.DateTimeField(blank=True, null=True)
    finished_test = models.DateTimeField(blank=True, null=True)
    total_results = models.SmallIntegerField(blank=True, null=True)
    is_failed = models.BooleanField(default=False)

    #
    # connect_upwork_account = models.URLField(null=True, blank=True)
    # connect_toptal_account = models.URLField(null=True, blank=True)
    # connect_kwork_account = models.URLField(null=True, blank=True)
    # connect_freever_account = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    about = models.TextField(null=True, blank=True)

    profile_image = models.ImageField(upload_to='users/profile/images/', blank=True, null=True)
    # required

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username



    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



    def starting_test(self):
        self.starting_test = self.starting_test.auto_now()


    def failed_test(self):
        if self.score < 8:
            self.is_failed = self.is_failed = True
            self.finished_test = self.finished_test.auto_now()
        else:
            self.finished_test = self.finished_test.auto_now()


    def profile_image_tur(self):
        if Account.profile_image == None:
            return False
        else:
            return True





class Test(models.Model):
    platforms = (
        ('upwork', 'Upwork'),
        ('kwork', 'Kwork'),
        ('freelancer', 'Freelancer'),
        ('toptal', 'Toptal')
    )
    test_question = models.CharField(max_length=200)
    true_test = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D')
    )
    a = models.CharField(max_length=200, null=True, blank=True)
    b = models.CharField(max_length=200, null=True, blank=True)
    c = models.CharField(max_length=200, null=True, blank=True)
    d = models.CharField(max_length=200, null=True, blank=True)
    correct_answer = models.CharField(max_length=14, choices=true_test, null=True, blank=True)

    def __str__(self):
        return self.test_question





