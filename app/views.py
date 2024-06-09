from django.shortcuts import render, redirect
from .models import Appointment, Healthchceck, Specialist
from django.contrib import messages
# Create your views here.
def home(request):
    my_specialists = Specialist.objects.all()
    context = {
        'my_specialists': my_specialists,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def add_appointment(request):
    if request.method == 'POST':
        patientname = request.POST['patientname']
        department = request.POST['department']
        doctorname = request.POST['doctorname']
        date = request.POST['datetime']
        timeslot = request.POST['timeslot']
        problem = request.POST['problem']

        myappointment = Appointment.objects.create(patient_name=patientname, department=department, doctor_name=doctorname, appointmaent_date=date, time_slot=timeslot, problem=problem)
        myappointment.save()
        messages.success(request, 'Appointment added !!')
        return redirect('/add_appointment')
    return render(request, 'add_appointment.html')

def book_test(request):
    return render(request, 'book_test.html')

def all_appointments(request):
    myappointment = Appointment.objects.all()
    constext = {
        'myappointment': myappointment
    }
    return render(request, 'all_appointments.html', constext)


def delete(request, id):
    myappointment = Appointment.objects.get(id = id)
    myappointment.delete()
    messages.success(request, 'Appointment deleted Successfully !!')
    return redirect('/all_appointments')

def health_checkup(request):

    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST['gender']
        pastdisease = request.POST['pastdisease']
        hospital = request.POST['hospital']

        person = Healthchceck.objects.create(age=age, gender=gender, pastdisease=pastdisease, hospital=hospital)
        person.save()
        return redirect('/')
    return render(request, 'health_checkup.html')


def view_specialists(request, id):
    specialist = Specialist.objects.get(id = id)

    context = {
        'specialist': specialist,
    }
    return render(request, 'view_specialists.html', context)