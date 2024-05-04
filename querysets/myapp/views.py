from django.shortcuts import render,HttpResponse
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    # student=Student.objects.all()
    # student=Student.objects.filter(marks=32)#student who has marks =32
    # student=Student.objects.exclude(marks=32)#those student who dont have marks =32
    
    # student=Student.objects.order_by('?')#rondom order at each referesh
    # student=Student.objects.order_by('marks')[:4]#ascending order #upto 4 row only display    
    # student=Student.objects.order_by('-marks')#descending order
    # student=Student.objects.order_by('id').reverse()[:3]
    
    # student=Student.objects.values('name','marks')#in the form of disctionary # specific column
    # student=Student.objects.values_list('name','marks',named=True)#in the form of tuple # specific column


    ##################   teacher column started for union  #########################

    # qs1=Student.objects.values_list('name','city',named=True)
    # qs2=Teacher.objects.values_list('name','city',named=True)

    # ##dublicate are removed
    ## student=qs2.union(qs1)#both name and city equal dublicate are removed,,,,if all=true then all data will be shown
    
    ##dublicate are include only both table combined 
    ### student=qs2.union(qs1,all=True)  


    # #########intersection###############
    # qs1=Student.objects.values_list('name','city',named=True)
    # qs2=Teacher.objects.values_list('name','city',named=True)

    # ##only common are shown
    # student=qs2.intersection(qs1)


    # ######### difference ###############
    # qs1=Student.objects.values_list('name','city',named=True)
    # qs2=Teacher.objects.values_list('name','city',named=True)

    # ##only qs2 are shown which are not common with qs1 ie qs2-qs1
    # student=qs2.difference(qs1)

    # ##for qs1-qs2
    # #student=qs1.difference(qs2)

    ########### Or And operator ###########
    # qs1=Student.objects.values_list('name','city',named=True)
    # qs2=Teacher.objects.values_list('name','city',named=True)

    # student=Student.objects.filter( Q(name='bijaya') & Q(city='brt') )#ie and operator
    # student=Student.objects.filter( Q(name='bijaya') | Q(city='brt') )#ie OR  operator

    ######## create, get_or_create, update ,update_or_create ,bulk_create ###############

    # Student.objects.create(name='dhiraj',roll=234,city='brt',marks=44)
    # student=Student.objects.all()


    # student,created=Student.objects.get_or_create(name='dhiraj',roll=23000,city='brt',marks=44)
    # student=Student.objects.all()

    # st=Student.objects.filter(city='brt').update(marks=30)
    # student=Student.objects.all()

    # st,created=Student.objects.update_or_create(name='bj',marks=30, defaults={'name':'ojha','roll':800,'marks':100})
    # student=Student.objects.all()

    objs =[
        Student(name='flora',roll='987',city='slg',marks='23'),
        Student(name='funna',roll='654',city='brt',marks='32'),
    ]
    Student.objects.bulk_create(objs)
    student=Student.objects.all()
    

    # print(st)
    # print(created)
    # print("sql queries=",student)
    return render(request,'myapp/home.html',{'stu':student})


