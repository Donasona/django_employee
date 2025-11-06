from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from crm.forms import Userregistration
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
      
class EmployeeUpdateView(View):
    def get(self,request,**kwargs): #**kwargs ={"pk":2}
        update_id=kwargs.get("pk")
        emp_data =Employeemodel.objects.get(id=update_id)
        return render(request,"emp_update.html", {"emp_data":emp_data}) 
         
    # get request fetches values from the database and fills the input fields with current value

    def post(self,request,**kwargs):
        update_id=kwargs.get("pk")
        emp_data =Employeemodel.objects.get(id=update_id)
        print(request.POST)
        emp_data.name =request.POST.get("username")
        emp_data.role =request.POST.get("userrole")
        emp_data.place =request.POST.get("userplace")
        emp_data.salary =request.POST.get("usersalary")
        emp_data.save()
        return render(request,"emp_update.html")
    
class EmployeedeleteView(View):
    def get(self,request,**kwargs):
        delete_id =kwargs.get("pk")
        emp_data =Employeemodel.objects.get(id=delete_id)
        emp_data.delete()
        return render(request,"add_employee.html") 

class EmployeeretriveView(View):
    def get(self,request,**kwargs):
        retrive_id = kwargs.get("pk")
        emp_data =Employeemodel.objects.get(id=retrive_id)
        return render(request,"emp_details.html",{"emp_data":emp_data})   
    
class Userregisterview(View):
    def get(self,request):
        form =Userregistration()
        return render(request,"register.html",{"form":form})

    