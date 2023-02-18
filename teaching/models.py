from django.db import models


class Academy(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    center = models.ForeignKey(Academy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    center = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.TextField(max_length=15)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.TextField(max_length=15)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Mark(models.Model):
    reyting = models.FloatField(default=0, null=True, blank=True)
    mark = models.FloatField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.student.name
