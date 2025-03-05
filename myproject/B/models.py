from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=128, primary_key=True)
    course_name = models.CharField(max_length=128)
    course_teacher = models.CharField(max_length=128)

    def __str__(self):
        return self.course_name
