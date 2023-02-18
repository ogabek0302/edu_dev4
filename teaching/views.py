from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Group, Student, Mark


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        group_id = request.POST.get('group_id')
        student = Student.objects.create(name=name, last_name=last_name, phone_number=phone_number, group_id=group_id)
    edu_groups = Group.objects.all()
    edu_students = Student.objects.all()

    contex = {'groups': edu_groups, 'students': edu_students}

    return render(request, 'index.html', context=contex)


def group(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        students = Student.objects.filter(group_id=group_id)
        context = {'groups': groups, 'students': students}

        return render(request, 'group.html', context=context)

    context = {'groups': groups}

    return render(request, 'group.html', context=context)


def mark(request):
    students = Student.objects.all()
    marks = Mark.objects.all()
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        mark = request.POST.get('mark')
        student_marks = Mark.objects.create(student_id=student_id, mark=mark)
        marks = Mark.objects.all()
        students = Student.objects.all()

        context = {'marks': marks, 'students': students}
        return render(request, 'mark.html', context=context)

    context = {'students': students, "marks": marks}
    return render(request, 'mark.html', context=context)


#
# def edit_student(request, pk):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         last_name = request.POST.get('last_name')
#         phone_number = request.POST.get('phone_number')
#         group_id = request.POST.get('group_id')
#         group = Group.objects.get(id=group_id)
#         student = Student.objects.get(id=pk)
#
#         student.name = name
#         student.last_name = last_name
#         student.phone_number = phone_number
#         student.group = group
#         student.save()
#
#     edu_groups = Group.objects.all()
#     context = {'groups': edu_groups, 'student': student}
#     return render(request, 'edit_student.html', context)


def edit_student(request, id):
    if request.method == "GET":
        try:
            student = Student.objects.get(id=id)
            context = {"student": student}
        except Student.DoesNotExist:
            context = {"errors": "Bu idlik post mavjus emas"}
            return render(request, 'edit_student.html', context=context)
    if request.method == 'POST':
        try:
            student = Student.objects.get(id=id)
            student.delete()
            context = {"deleted": True}
        except Student.DoesNotExist:
            context = {"deleted": True}
            return render(request, 'edit_student.html', context=context)
    return render(request, 'edit_student.html', context=context)

#
# def delete_student(request, id):
#     # students = Student.objects.get(id=id)
#     # students.delete()
#     #
#     # context = {'students': students}
#     #
#     # return render(request, 'edit_student.html', context)
#     if request.method == 'POST':
#         try:
#             student = Student.objects.get(id=id)
#             student.delete()
#             context = {"deleted": True}
#         except Student.DoesNotExist:
#             context = {"deleted": True}
#             return render(request, 'delete_student.html', context=context)
#
