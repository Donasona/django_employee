from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from crm.models import Employeemodel

class CreateemployeeView(View):
    def get(self,request):
        return render(request,"add_employee.html")
    def post(self,request):
        print(request.POST)
        Employeemodel.objects.create(name =request.POST.get('username'),
                                     role =request.POST.get('userrole'),
                                      place =request.POST.get('userplace'),
                                       salary =request.POST.get('usersalary') )
        return render(request,"add_employee.html")

class EmployeeListView(View):
    def get(self,request):
        data =Employeemodel.objects.all()
        return render(request,"employeelist.html",{"data":data})  
      