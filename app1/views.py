from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.core.files.storage import FileSystemStorage
import os
import time
from datetime import date

# Create your views here.

def courses_reg(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                obj=course_master()
                course_name=request.POST['T1']
                fees=request.POST['T2']
                duration=request.POST['T3']

                obj.course_name=course_name
                obj.fees=fees
                obj.duration=duration
                obj.save()
                return render(request,'courses_reg.html',{'data':'success'})
            else:
                return render(request,'courses_reg.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def courses_show(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            obj=course_master.objects.all()
            return render(request,'courses_show.html',{'data':obj})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_courses(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                course_id=request.POST['H1']
                obj=course_master.objects.filter(course_id=course_id)
                return render(request,'edit_courses.html',{'data':obj})
            else:
                return HttpResponseRedirect('/courses_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_courses1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                course_name=request.POST['T1']
                fees=request.POST['T2']
                duration=request.POST['T3']
                course_id=request.POST['T4']
                obj=course_master.objects.get(course_id=course_id)
                obj.course_name=course_name
                obj.fees=fees
                obj.duration=duration
                obj.save()
                return render(request,'edit_courses1.html',{'data':'change'})
            else:
                return HttpResponseRedirect('/courses_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_courses(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                course_id=request.POST['H1']
                obj=course_master.objects.filter(course_id=course_id)
                return render(request,'delete_courses.html',{'data':obj})
            else:
                return HttpResponseRedirect('/courses_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_courses1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                course_id=request.POST['T4']
                obj=course_master.objects.get(course_id=course_id)
                obj.delete()
                return render(request,'delete_courses1.html',{'data':'delete'})
            else:
                return HttpResponseRedirect('/courses_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def add_courses(request):

    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['S1']
                obj=course_master.objects.all()
                return render(request,'add_courses.html',{'data':obj,'email':email})
            else:
                return render(request,'add_courses.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def add_courses1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['H1']
                course_id=request.POST['H2']
                obj=course_master.objects.get(course_id=course_id)
                obj1=st_course()
                obj1.course_id=course_id
                obj1.email=email
                obj1.course_name=obj.course_name
                obj1.fees=obj.fees
                obj1.duration=obj.duration
                obj1.commencement_date=date.today()
                obj1.save()
                return render(request,'add_courses1.html',{'data':'ADD'})
            else:
                return render(request,'add_courses1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def pay_installment(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                st_course_id=request.POST['H2']
                email=request.POST['H1']
                obj=st_course.objects.filter(email=email,st_course_id=st_course_id)
                return render(request,'pay_installment.html',{'data':obj})
            else:
                return render(request,'pay_installment.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def pay_installment1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method=='POST':
                email=request.POST['H1']
                st_course_id=request.POST['H2']
                obj=st_course.objects.filter(st_course_id=st_course_id)
                obj1=st_installment(email=email)
                obj1.course_id=st_course_id
                obj1.amount=request.POST['T1']
                obj1.t_date=date.today()
                obj1.remark=request.POST['T2']
                obj1.save()
                return render(request,'pay_installment1.html',{'data':'success'})
            else:
                return render(request,'pay_installment1.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def operator_reg(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':

                obj=operatordata()
                obj1=logindata()

                a=request.POST['T1']
                b=request.POST['T2']
                c=request.POST['T3']
                d=request.POST['T4']
                e=request.POST['T5']
                f='operator'

                obj.name=a
                obj.address=b
                obj.contact=c
                obj.email=d

                obj1.email=d
                obj1.password=e
                obj1.usertype=f

                obj.save()
                obj1.save()
                return render(request,'operator_reg.html',{'data':'success'})
            else:
                return render(request,'operator_reg.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def student_reg_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin' :
            if request.method=='POST':
                obj=studentdata()
                obj1=logindata()

                a=request.POST['T1']
                b=request.POST['T2']
                c=request.POST['T3']
                d=request.POST['T4']
                e=request.POST['T5']
                f='student'

                obj.name=a
                obj.address=b
                obj.contact=c
                obj.email=d

                obj1.email=d
                obj1.password=e
                obj1.usertype=f

                obj.save()
                obj1.save()
                return render(request,'student_reg_admin.html',{'data':'success'})
            else:
                return render(request,'student_reg_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def student_reg_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator' :
            if request.method=='POST':
                obj=studentdata()
                obj1=logindata()

                a=request.POST['T1']
                b=request.POST['T2']
                c=request.POST['T3']
                d=request.POST['T4']
                e=request.POST['T5']
                f='student'

                obj.name=a
                obj.address=b
                obj.contact=c
                obj.email=d

                obj1.email=d
                obj1.password=e
                obj1.usertype=f

                obj.save()
                obj1.save()
                return render(request,'student_reg_operator.html',{'data':'success'})
            else:
                return render(request,'student_reg_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')



def student_show_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype== 'operator':
            obj=studentdata.objects.all()
            return render(request,'student_show_operator.html',{'data':obj})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def view_student_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator':
            if request.method=='POST':
                email = request.POST['H1']
                obj = studentdata.objects.filter(email=email)
                obj1 = photodata.objects.filter(email=email)
                obj2=st_course.objects.filter(email=email)
                obj3=st_installment.objects.filter(email=email)
                student_courses = []
                total_paid = 0
                for d in obj2:
                    paid = course_total(d.st_course_id)
                    total_paid = total_paid + paid
                    fees = d.fees
                    due = int(fees) - paid
                    aa = [d.st_course_id, d.course_id, d.email, d.course_name, d.fees, d.duration, d.commencement_date,
                          paid, due]
                    student_courses.append(aa)

                t1 = all_course_fee(email)
                total_due = t1 - total_paid
                return render(request, 'view_student_operator.html', {'data': obj, 'data1': obj1, 'email': email,'data2':student_courses,'data3':obj3,'total':t1,'total_paid':total_paid,'total_due':total_due})

            else:
                return render(request, 'view_student_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')
def view_operator_admin(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        e1 = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                email = request.POST['H1']
                obj = operatordata.objects.filter(email=email)
                obj1 = photodata.objects.filter(email=email)
                return render(request, 'view_operator_admin.html',{'data': obj, 'data1': obj1, 'email': email})
            else:
                return render(request, 'view_operator_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def view_student_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        e1=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email = request.POST['H1']
                obj = studentdata.objects.filter(email=email)
                obj1 = photodata.objects.filter(email=email)
                obj2 = st_course.objects.filter(email=email)

                student_courses=[]
                total_paid=0
                for d in obj2:
                    paid=course_total(d.st_course_id)
                    total_paid=total_paid+paid
                    fees=d.fees
                    due=int(fees)-paid
                    aa=[d.st_course_id,d.course_id,d.email,d.course_name,d.fees,d.duration,d.commencement_date,paid,due]
                    student_courses.append(aa)

                obj3=st_installment.objects.filter(email=email)
                t1 = all_course_fee(email)
                total_due=t1-total_paid
                return render(request, 'view_student_admin.html', {'data': obj, 'data1': obj1, 'email': email,'data2':student_courses,'data3':obj3,'total':t1,'total_paid':total_paid,'total_due':total_due})
            else:
                return render(request, 'view_student_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def course_total(cid):

    obj=st_installment.objects.filter(course_id=cid)
    t=0
    for d in obj:
        t=t + int(d.amount)
    return t


def student_show_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            obj=studentdata.objects.all()
            return render(request,'student_show_admin.html',{'data':obj})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def admin_show(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            obj=admindata.objects.all()
            obj1=photodata.objects.filter(email=email)
            return render(request,'admin_show.html',{'data':obj,'data1':obj1})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def operator_show(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            obj = operatordata.objects.all()
            obj1 = photodata.objects.filter(email=email)
            return render(request,'operator_show.html',{"data":obj,'data1':obj1})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['H1']
                obj=operatordata.objects.filter(email=email)
                return render(request,'edit_operator.html',{'data':obj})
            else:
                return HttpResponseRedirect('/operator_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_operator1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                name=request.POST['T1']
                address=request.POST['T2']
                contact=request.POST['T3']
                email=request.POST['T4']
                obj=operatordata.objects.get(email=email)
                obj.name=name
                obj.address=address
                obj.contact=contact
                obj.save()
                return render(request,'edit_operator1.html',{'data':'change'})
            else:
                return HttpResponseRedirect('/operator_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['H1']
                obj=operatordata.objects.filter(email=email)
                return render(request,'delete_operator.html',{'data':obj})
            else:
                return HttpResponseRedirect('/operator_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_operator1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['T4']
                obj=operatordata.objects.get(email=email)
                obj1=logindata.objects.get(email=email)
                obj.delete()
                obj1.delete()
                return render(request,'delete_operator1.html',{'data':'delete'})
            else:
                return HttpResponseRedirect('/operator_show/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def edit_student_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator':
            if request.method=='POST':
                email=request.POST['H1']
                obj=studentdata.objects.filter(email=email)
                return render(request,'edit_student_operator.html',{'data':obj})
            else:
                return HttpResponseRedirect('/student_show_operator/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def edit_student_operator1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator':
            if request.method=='POST':
                name=request.POST['T1']
                address=request.POST['T2']
                contact=request.POST['T3']
                email=request.POST['T4']
                obj=studentdata.objects.get(email=email)
                obj.name=name
                obj.address=address
                obj.contact=contact
                obj.save()

                return render(request,'edit_student_operator1.html',{'data':'saved'})
            else:
                return HttpResponseRedirect('/student_show_operator/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def edit_student_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['H1']
                obj=studentdata.objects.filter(email=email)
                return render(request,'edit_student_admin.html',{'data':obj})
            else:
                return HttpResponseRedirect('/student_show_admin/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def edit_student_admin1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                name=request.POST['T1']
                address=request.POST['T2']
                contact=request.POST['T3']
                email=request.POST['T4']
                obj=studentdata.objects.get(email=email)
                obj.name=name
                obj.address=address
                obj.contact=contact
                obj.save()

                return render(request,'edit_student_admin1.html',{'data':'saved'})
            else:
                return HttpResponseRedirect('/student_show_admin/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def delete_student_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator':
            if request.method=='POST':
                email=request.POST['H1']
                obj=studentdata.objects.filter(email=email)
                return render(request,'delete_student_operator.html',{"data":obj})
            else:
                return HttpResponseRedirect('student_show_operator')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def delete_student_operator1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator':
            if request.method=='POST':
                email=request.POST['T4']
                obj=studentdata.objects.get(email=email)
                obj1=logindata.objects.get(email=email)
                obj2=photodata.objects.get(email=email)
                obj.delete()
                obj1.delete()
                obj2.delete()
                return render(request,'delete_student_operator1.html',{'data':'delete'})
            else:
                return HttpResponseRedirect('/student_show_operator/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def delete_student_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['H1']
                obj=studentdata.objects.filter(email=email)
                return render(request,'delete_student_admin.html',{"data":obj})
            else:
                return HttpResponseRedirect('student_show_admin')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def delete_student_admin1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                email=request.POST['T4']
                obj=studentdata.objects.get(email=email)
                obj1=logindata.objects.get(email=email)
                obj2=photodata.objects.get(email=email)
                obj.delete()
                obj1.delete()
                obj2.delete()
                return render(request,'delete_student_admin1.html',{'data':'delete'})
            else:
                return HttpResponseRedirect('/student_show_admin/')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def login(request):
    if request.method=='POST':
        email=request.POST['T1']
        password=request.POST['T2']
        try:
            obj=logindata.objects.get(email=email,password=password)
            usertype=obj.usertype
            request.session['usertype']=usertype
            request.session['email']=email
            if usertype=='admin':
                return HttpResponseRedirect('/admin_home/')
            elif usertype=='student':
                return HttpResponseRedirect('/student_home/')
            elif usertype=='operator':
                return HttpResponseRedirect('/operator_home/')
        except:
            return render(request,'login.html',{'data':'Invalid email & password'})
    else:
        return render(request,'login.html')

def admin_home(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype=='admin':
            return render(request, 'admin_home.html')
        else:
            return render(request,'auth_error.html')
    else:
        return render(request,'auth_error.html')

def student_home(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype=='student':
            return render(request,'student_home.html')
        else:
            return render(request,'auth_error.html')
    else:
        return render(request,'auth_error.html')

def operator_home(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype=='operator':
            return render(request,'operator_home.html')
        else:
            return render(request,'auth_error.html')
    else:
        return render(request,'auth_error.html')

def logout(request):
    try:
        del request.session['usertype']
        del request.session['email']
    except:
        pass
    return HttpResponseRedirect('/login/')


def auth_error(request):
    return render(request,'auth_error.html')

def upload_photo_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method == 'POST':
                try:
                    upload_file=request.FILES['F1']
                    path=os.path.basename(upload_file.name)
                    file_ext=os.path.splitext(path)[1][1:]
                    file_name=str(int(time.time())) + '.' + file_ext
                    fs=FileSystemStorage()
                    fs.save(file_name,upload_file)
                    obj=photodata()
                    obj.email=email
                    obj.photo=file_name
                    obj.save()
                    return render(request,'upload_photo_admin.html',{'data':'success'})
                except :
                    return render(request,'upload_photo_admin.html',{'data':'Please Choose File'})
            else:
                return render(request,'upload_photo_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def upload_photo_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype== 'operator':
            if request.method == 'POST':
                try:
                    upload_file=request.FILES['F1']
                    path=os.path.basename(upload_file.name)
                    file_ext=os.path.splitext(path)[1][1:]
                    file_name=str(int(time.time())) + '.' + file_ext
                    fs=FileSystemStorage()
                    fs.save(file_name,upload_file)
                    obj=photodata()
                    obj.email=email
                    obj.photo=file_name
                    obj.save()
                    return render(request,'upload_photo_operator.html',{'data':'success'})
                except:
                    return render(request, 'upload_photo_operator.html', {'data': 'Please Choose  File'})
            else:
                return render(request,'upload_photo_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def upload_photo_student_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype== 'operator':
            if request.method == 'POST':
                try:
                    email=request.POST['H1']
                    upload_file=request.FILES['F1']
                    path=os.path.basename(upload_file.name)
                    file_ext=os.path.splitext(path)[1][1:]
                    file_name=str(int(time.time())) + '.' + file_ext
                    fs=FileSystemStorage()
                    fs.save(file_name,upload_file)
                    obj=photodata()
                    obj.email=email
                    obj.photo=file_name
                    obj.save()
                    return render(request,'upload_photo_student_operator.html',{'data':'success'})
                except:
                    return render(request, 'upload_photo_student_operator.html', {'data': 'Please Choose File'})
            else:
                return render(request,'upload_photo_student_operator.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def upload_photo_student_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype== 'admin':
            if request.method == 'POST':
                    try:
                        email=request.POST['H1']
                        upload_file=request.FILES['F1']
                        path=os.path.basename(upload_file.name)
                        file_ext=os.path.splitext(path)[1][1:]
                        file_name=str(int(time.time())) + '.' + file_ext
                        fs=FileSystemStorage()
                        fs.save(file_name,upload_file)
                        obj=photodata()
                        obj.email=email
                        obj.photo=file_name
                        obj.save()
                        return render(request,'upload_photo_student_admin.html',{'data':'success'})
                    except:
                        return render(request, 'upload_photo_student_admin.html', {'data': 'Please Choose File'})
            else:
                return render(request,'upload_photo_student_admin.html')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def change_photo_admin(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            obj=photodata.objects.get(email=email)
            obj.delete()
            return render(request,'change_photo_admin.html',{'data':'success'})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def change_photo_operator(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'operator':
            obj=photodata.objects.get(email=email)
            obj.delete()
            return render(request,'change_photo_operator.html',{'data':'success'})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def change_photo_student_operator(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'operator':
            if request.method=='POST':
                email=request.POST['H1']
                obj = photodata.objects.get(email=email)
                obj.delete()
                return render(request, 'change_photo_student_operator.html', {'data': 'success'})
            else:
                return render(request, 'change_photo_student_operator.htmnl')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def change_photo_student_admin(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method=='POST':
                email=request.POST['H1']
                obj = photodata.objects.get(email=email)
                obj.delete()
                return render(request, 'change_photo_student_admin.html', {'data': 'success'})
            else:
                return render(request, 'change_photo_student_admin.htmnl')
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def admin_profile(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                obj=admindata.objects.get(email=email)
                obj.name=request.POST['T1']
                obj.address=request.POST['T2']
                obj.contact=request.POST['T3']
                obj.save()
                return render(request,'admin_profile.html',{'result':'success'})
            else:
                obj=admindata.objects.filter(email=email)
                obj1=photodata.objects.filter(email=email)
                return render(request,'admin_profile.html',{'data1':obj1,'data':obj,'email':email})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def operator_profile(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator':
            if request.method=='POST':
                obj=operatordata.objects.get(email=email)
                obj.name=request.POST['T1']
                obj.address=request.POST['T2']
                obj.contact=request.POST['T3']
                obj.save()
                return render(request,'operator_profile.html',{'result':'success'})
            else:
                obj=operatordata.objects.filter(email=email)
                obj1=photodata.objects.filter(email=email)
                return render(request,'operator_profile.html',{'data1':obj1,'data':obj,'email':email})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def student_profile(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='student':
            if request.method=='POST':
                return render(request,'student_profile.html')
            else:

                obj = studentdata.objects.filter(email=email)
                obj1 = photodata.objects.filter(email=email)
                obj2 = st_course.objects.filter(email=email)
                obj3 = st_installment.objects.filter(email=email)
                student_courses = []
                total_paid = 0
                for d in obj2:
                    paid = course_total(d.st_course_id)
                    total_paid = total_paid + paid
                    fees = d.fees
                    due = int(fees) - paid
                    aa = [d.st_course_id, d.course_id, d.email, d.course_name, d.fees, d.duration, d.commencement_date,
                          paid, due]
                    student_courses.append(aa)

                t1 = all_course_fee(email)
                total_due = t1 - total_paid
                return render(request, 'student_profile.html', {'data': obj, 'data1': obj1, 'email': email,'data2':student_courses,'data3':obj3,'total':t1,'total_paid':total_paid,'total_due':total_due})
        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def changepass_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='admin':
            if request.method=='POST':
                obj=logindata.objects.get(email=email)
                old_password=request.POST['T1']
                new_password=request.POST['T2']
                confirm_password=request.POST['T3']
                if new_password==confirm_password and old_password==obj.password:
                    obj.password=new_password
                    obj.save()
                    return render(request,'changepass_admin.html',{'data':'change'})
                else:
                    return render(request,'changepass_admin.html',{'data':'not match password'})
            else:
                return render(request,'changepass_admin.html')

        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def changepass_operator(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='operator':
            if request.method=='POST':
                obj=logindata.objects.get(email=email)
                old_password=request.POST['T1']
                new_password=request.POST['T2']
                confirm_password=request.POST['T3']
                if new_password==confirm_password and old_password==obj.password:
                    obj.password=new_password
                    obj.save()
                    return render(request,'changepass_operator.html',{'data':'change'})
                else:
                    return render(request,'changepass_operator.html',{'data':'not match password'})
            else:
                return render(request,'changepass_operator.html')

        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')

def changepass_student(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        email=request.session['email']
        if usertype=='student':
            if request.method=='POST':
                obj=logindata.objects.get(email=email)
                old_password=request.POST['T1']
                new_password=request.POST['T2']
                confirm_password=request.POST['T3']
                if new_password==confirm_password and old_password==obj.password:
                    obj.password=new_password
                    obj.save()
                    return render(request,'changepass_student.html',{'data':'change'})
                else:
                    return render(request,'changepass_student.html',{'data':'not match password'})
            else:
                return render(request,'changepass_student.html')

        else:
            return HttpResponseRedirect('/auth_error/')
    else:
        return HttpResponseRedirect('/auth_error/')


def all_course_fee(email):
    obj=st_course.objects.filter(email=email)
    t=0
    for d in obj:
        t=t+ int(d.fees)
    return t

