from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm


def home(request):
    return render(request, "employees/home.html")


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employees/employee_list.html", {"employees": employees})


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Added Successfully")
            return redirect("employee_list")
    else:
        form = EmployeeForm()

    return render(request, "employees/employee_form.html", {"form": form})


def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Updated Successfully")
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employees/employee_form.html", {"form": form})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee Deleted Successfully")
        return redirect("employee_list")

    return render(request, "employees/employee_confirm_delete.html", {"employee": employee})