from django.db import models

# Create your models here.


class Admin(models.Model):
    imag = models.ImageField(upload_to='photos/%y/%m/%d')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Price = models.IntegerField()

    def __str__(self):
        return self.title
    






class DateTime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return f"{self.date} - {self.time}"


class User(models.Model):
    TRIP_CHOICES = [
        ('أشقار', 'أشقار'),
        ('الغابة الديبلوماسية', 'الغابة الديبلوماسية'),
        ('أصيلة', 'أصيلة'),
        ('فنيدق', 'فنيدق'),
        ('العرائش', 'العرائش'),
        ('بليونيش', 'بليونيش'),
        ('بليونيش', 'بليونيش'),
    ]

    select_your_trip = models.CharField(
        max_length=50, 
        choices=TRIP_CHOICES,
        verbose_name="Selected Trip"
    )
    
    first_name = models.CharField(
        max_length=50, 
        verbose_name="First Name"
    )
    
    last_name = models.CharField(
        max_length=50, 
        verbose_name="Last Name"
    )
    
    phone_number = models.CharField(
        max_length=20, 
        verbose_name="Phone Number"
    )
    

    special_requests = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Special Requests"
    )
    def __str__(self):
        return f"{self.date} - {self.time}"

    datetime = models.ForeignKey(DateTime, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.select_your_trip} - {self.datetime.date} {self.datetime.time}"
    
    




    class Meta:
        verbose_name = "Trip Booking"
        verbose_name_plural = "Trip Bookings"

