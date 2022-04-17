from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User, UserManager
from . import constants


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AdminPanel(TimestampModel):
    email = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=False)
    country_code = models.CharField(max_length=3, blank=False)
    mobile_no = models.IntegerField(max_length=10, unique=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    # gender = models.CharField(max_length=20, choices=constants.GENDER_TYPE)
    # age = models.IntegerField(max_length=3)
    # height = models.DecimalField(max_digits=3, decimal_places=2)
    # mother_tongue = models.CharField(max_length=100)
    # religion = models.CharField(max_length=100)
    # caste = models.CharField(max_length=100)
    # sub_caste = models.CharField(max_length=100)
    # annual_income = models.CharField(max_length=100, default=0)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    # nri_tag = models.IntegerField(max_length=1)
    # education = models.CharField(max_length=100)
    # occupation = models.CharField(max_length=100)
    # employed_in = models.CharField(max_length=100)
    # photo_available = models.IntegerField(max_length=1)
    # photo_protected = models.IntegerField(max_length=1)
    # photo_count = models.IntegerField(max_length=20)
    # horoscope_available = models.IntegerField(max_length=1)
    # horo_protected = models.IntegerField(max_length=1)
    # phone_hidden = models.IntegerField(max_length=1)
    # #    time_created =
    # profile_created_by = models.CharField(max_length=100)
    # about_me = models.CharField(max_length=500)  # , default="About Me")
    # personality = models.CharField(max_length=100)
    # marital_life = models.CharField(max_length=100)
    # gothra = models.CharField(max_length=100)
    # manglik = models.IntegerField(max_length=1)
    # star_rashi = models.CharField(max_length=100)
    # eating_habits = models.CharField(max_length=100)
    # drink = models.IntegerField(max_length=1)
    # smoke = models.IntegerField(max_length=1)
    # hobbies_music_sports = models.CharField(max_length=100)
    # languages = models.CharField(max_length=100)
    # ancestral_origin = models.CharField(max_length=100)
    # about_family = models.CharField(max_length=255)
    # family_des = models.CharField(max_length=255)
    # parents = models.CharField(max_length=255)
    # brother = models.DecimalField(max_digits=2, decimal_places=2)
    # sister = models.DecimalField(max_digits=2, decimal_places=2)
    # p_age = models.CharField(max_length=100)
    # p_height = models.CharField(max_length=100)
    # p_marital_status = models.IntegerField(max_length=1)
    # p_mother_tongue = ArrayField(models.CharField(max_length=20, blank=True), blank=True)
    # p_physical_status = models.CharField(max_length=100)
    # p_eating_habits = models.CharField(max_length=100)
    # p_drink = models.CharField(max_length=100)
    # p_smoke = models.CharField(max_length=100)
    # p_religion = models.CharField(max_length=100)
    # p_caste = models.CharField(max_length=100)
    # p_subcaste = models.CharField(max_length=100)
    # p_star = models.CharField(max_length=100)
    # p_manglik = models.CharField(max_length=100)
    # p_education = models.CharField(max_length=255)
    # p_employedin = models.CharField(max_length=255)
    # p_occupation = ArrayField(models.CharField(max_length=255, blank=True), blank=True)
    # p_annualincome = models.CharField(max_length=100)
    # p_country = ArrayField(models.CharField(max_length=100), blank=True)
    # p_city = ArrayField(models.CharField(max_length=100), blank=True)
    # p_state = ArrayField(models.CharField(max_length=100), blank=True)
    # p_citizenship = ArrayField(models.CharField(max_length=100), blank=True)
    # p_ancestral = ArrayField(models.CharField(max_length=100), blank=True)
    is_authenticated = True
    is_anonymous = False
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'country_code', 'mobile_no', 'is_admin', 'is_superuser']
    is_active = True
    objects = UserManager()
    check_password = User.check_password

    class Meta:
        ordering = ["-email"]

    def __str__(self):
        return self.name


class UserCheck(TimestampModel):
    # username = models.ForeignKey(AdminPanel, on_delete=models.CASCADE, primary_key=True)
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=255)
    caste = models.CharField(max_length=255)
    age = models.IntegerField(max_length=3)
    mother_tongue = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    annual_income = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    employed_in = models.CharField(max_length=255)
    photo_count = models.IntegerField(max_length=255)
    profile_created_by = models.CharField(max_length=255)
    marital_life = models.CharField(max_length=255)
    brother = models.IntegerField(max_length=3)
    sister = models.IntegerField(max_length=3)
    p_age = models.CharField(max_length=255)
    p_marital_status = models.CharField(max_length=255)
    p_mother_tongue = models.CharField(max_length=255)
    p_religion = models.CharField(max_length=255)
    # p_annualincome = models.CharField(max_length=255)

    class Meta:
        ordering = ["-religion"]

    def __str__(self):
        return self.religion


# class PersonalInfo(TimestampModel):
#     name = models.CharField(max_length=255)
#     username = models.ForeignKey(AdminPanel, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=20, choices=constants.GENDER_TYPE)
#     age = models.IntegerField(max_length=3)
#     height = models.DecimalField(max_digits=3, decimal_places=2)
#     mother_tongue = models.CharField(max_length=100)
#     religion = models.CharField(max_length=100)
#     caste = models.CharField(max_length=100)
#     sub_caste = models.CharField(max_length=100)
#     annual_income = models.CharField(max_length=100, default=0)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     nri_tag = models.IntegerField(max_length=1)
#     education = models.CharField(max_length=100)
#     occupation = models.CharField(max_length=100)
#     employed_in = models.CharField(max_length=100)
#     photo_available = models.IntegerField(max_length=1)
#     photo_protected = models.IntegerField(max_length=1)
#     photo_count = models.IntegerField(max_length=20)
#     horoscope_available = models.IntegerField(max_length=1)
#     horo_protected = models.IntegerField(max_length=1)
#     phone_hidden = models.IntegerField(max_length=1)
#     #    time_created =
#     profile_created_by = models.CharField(max_length=100)
#     about_me = models.CharField(max_length=500)  # , default="About Me")
#     personality = models.CharField(max_length=100)
#     marital_life = models.CharField(max_length=100)
#     gothra = models.CharField(max_length=100)
#     manglik = models.IntegerField(max_length=1)
#     star_rashi = models.CharField(max_length=100)
#     eating_habits = models.CharField(max_length=100)
#     drink = models.IntegerField(max_length=1)
#     smoke = models.IntegerField(max_length=1)
#     hobbies_music_sports = models.CharField(max_length=100)
#     languages = models.CharField(max_length=100)
#
#     class Meta:
#         ordering = ["-id"]
#
#     def __str__(self):
#         return self.name


# class AboutFamily(models.Model):
#     username = models.ForeignKey(AdminPanel, on_delete=models.CASCADE)
#     ancestral_origin = models.CharField(max_length=100)
#     about_family = models.CharField(max_length=255)
#     family_des = models.CharField(max_length=255)
#     parents = models.CharField(max_length=255)
#     brother = models.DecimalField(max_digits=2, decimal_places=2)
#     sister = models.DecimalField(max_digits=2, decimal_places=2)
#
#     class Meta:
#         ordering = ["-id"]
#
#     def __str__(self):
#         return self.ancestral_origin


# class PartnerPreferences(models.Model):
#     username = models.ForeignKey(AdminPanel, on_delete=models.CASCADE)
#     p_age = models.CharField(max_length=100)
#     p_height = models.CharField(max_length=100)
#     p_marital_status = models.IntegerField(max_length=1)
#     p_mother_tongue = ArrayField(models.CharField(max_length=20, blank=True), blank=True)
#     p_physical_status = models.CharField(max_length=100)
#     p_eating_habits = models.CharField(max_length=100)
#     p_drink = models.CharField(max_length=100)
#     p_smoke = models.CharField(max_length=100)
#     p_religion = models.CharField(max_length=100)
#     p_caste = models.CharField(max_length=100)
#     p_subcaste = models.CharField(max_length=100)
#     p_star = models.CharField(max_length=100)
#     p_manglik = models.CharField(max_length=100)
#     p_education = models.CharField(max_length=255)
#     p_employedin = models.CharField(max_length=255)
#     p_occupation = ArrayField(models.CharField(max_length=255, blank=True), blank=True)
#     p_annualincome = models.CharField(max_length=100)
#     p_country = ArrayField(models.CharField(max_length=100), blank=True)
#     p_city = ArrayField(models.CharField(max_length=100), blank=True)
#     p_state = ArrayField(models.CharField(max_length=100), blank=True)
#     p_citizenship = ArrayField(models.CharField(max_length=100), blank=True)
#     p_ancestral = ArrayField(models.CharField(max_length=100), blank=True)
#
#     def __str__(self):
#         return self.p_age


# class Membership(models.Model):
#     username = models.ForeignKey(AdminPanel, on_delete=models.CASCADE)
#     premium_tag = models.IntegerField(max_length=1)
#     membership = models.CharField(max_length=100)
#     identity_status = models.IntegerField(max_length=1)
#     professional_status = models.IntegerField(max_length=1)
#     profile_status = models.IntegerField(max_length=1)
#     education_status = models.IntegerField(max_length=1)
#     salary_status = models.IntegerField(max_length=1)
#
#     def __str__(self):
#         return self.membership


class ReportTable(TimestampModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
    report = ArrayField(models.CharField(max_length=100))
    reported_by = ArrayField(models.CharField(max_length=100))
    blacklist = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name
