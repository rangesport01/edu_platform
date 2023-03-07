from django.db import models
from mentorship.models import Specialization, Teacher
from mixins import DateTimeMixin


class Course(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.TextField
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_DEFAULT, default="specialization")

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"
