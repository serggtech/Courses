from django.db import models

# Create your models here.


class StudentProfile(models.Model):
    student_name = models.CharField(max_length=200, verbose_name="Имя")
    # student_city = models.CharField(max_length=200, verbose_name="Город")
    # student_linkidin = models.CharField(max_length=200, verbose_name="Город")
    student_insta = models.CharField(max_length=200, verbose_name="интса")
    student_tele = models.CharField(max_length=200, verbose_name="телега")
    student_stack = models.CharField(max_length=200, verbose_name="Стэк")


# class StudentSpecial(models.Model):
#     title = models.CharField(verbose_name="Проект", max_length=100)
#     title_description = models.CharField(
#         verbose_name="Описание проекта", max_length=100
#     )
#     slug = models.SlugField(max_length=50, unique=True)
#
#
# class StudentCity(models.Model):
#     title = models.CharField(verbose_name="Проект", max_length=100)
#     title_description = models.CharField(
#         verbose_name="Описание проекта", max_length=100
#     )
#     slug = models.SlugField(max_length=50, unique=True)
#
#
# class StudentMap(models.Model):
#     student_name = models.CharField(max_length=200, verbose_name="Имя")
#     student_last_name = models.CharField(max_length=200, verbose_name="Фамилия")
#     student_middle_name = models.CharField(max_length=200, verbose_name="Отчество")
#     student_x = models.FloatField(max_length=100, verbose_name="Координаты X")
#     student_y = models.FloatField(max_length=100, verbose_name="Координаты Y")
#     student_city = models.ManyToManyField(
#         StudentCity,
#         related_name="StudentSpecial",
#         blank=True,
#     )
#
#     student_create = models.DateTimeField(verbose_name="Дата добавления", auto_now=True)
#     student_update = models.DateTimeField(
#         verbose_name="Дата редактирования", auto_now=True
#     )
#     student_number_phone = models.CharField(
#         max_length=200, verbose_name="Номер телефона"
#     )
#     student_special = models.ManyToManyField(
#         StudentSpecial,
#         related_name="StudentSpecial",
#         blank=True,
#     )
