# Generated by Django 4.1.6 on 2023-03-01 17:38

from django.db import migrations, models
import django.db.models.deletion
import mixins


class Migration(migrations.Migration):
    dependencies = [
        ("testing_system", "0001_create_course_model"),
        ("mentorship", "0003_create_model_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="testing_system.course",
                    ),
                ),
                (
                    "student",
                    models.ManyToManyField(blank=True, to="mentorship.student"),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mentorship.teacher",
                    ),
                ),
            ],
            options={
                "verbose_name": "group",
                "verbose_name_plural": "groups",
            },
            bases=(models.Model, mixins.DateTimeMixin),
        ),
    ]
