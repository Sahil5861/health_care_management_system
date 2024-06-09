from django.db import models

# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length = 255)
    department = models.CharField(max_length = 255)
    doctor_name = models.CharField(max_length = 255)
    appointmaent_date = models.DateField()
    time_slot = models.TimeField()

    problem = models.TextField(max_length = 255)

    def __str__(self) -> str:
        return f'{self.patient_name} - {self.department} - {self.doctor_name} - {self.appointmaent_date} - {self.problem}'
    

class Healthchceck(models.Model):
    age = models.CharField(max_length = 128)
    gender = models.CharField(max_length = 128)
    pastdisease = models.CharField(max_length = 255)
    hospital = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.age} - {self.gender} - {self.pastdisease} - {self.hospital}'
    

class Specialist(models.Model):
    specialist = models.CharField(max_length = 128)
    title = models.CharField(max_length = 255)

    
    



    