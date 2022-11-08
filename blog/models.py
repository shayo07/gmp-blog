from django.db import models

# Create your models here.


class Device(models.Model):
    name= models.CharField(max_length=50, primary_key=True, help_text='user uppercase' )
    type= models.CharField(max_length=50, null=True, blank=True)
    description= models.CharField(max_length=1000, blank=True, null=True)
    image1= models.ImageField(null=True, blank=True)
    image2= models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    


class Frp_bypass(models.Model):
    device_name= models.ForeignKey(Device, on_delete=models.CASCADE)
    link= models.CharField(max_length=200, null=True, blank=True)
    file =models.FileField(null=True, blank=True)
    description= models.CharField(max_length=1000, blank=True, null=True)
    installation_guide= models.TextField(null=True, blank=True)
    image1= models.ImageField(null=True, blank=True)
    image2= models.ImageField(null=True, blank=True)
    image3= models.ImageField(null=True, blank=True)
    image4= models.ImageField(null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.description

class Frp_Comment(models.Model):
    name =  models.ForeignKey(Device, on_delete=models.CASCADE)
    email= models.CharField(max_length=100)
    comment= models.CharField(max_length=200, null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

class Firmwares(models.Model):
    device_name= models.ForeignKey(Device, on_delete=models.CASCADE)
    link= models.CharField(max_length=200, null=True, blank=True)
    file =models.FileField(null=True, blank=True)
    description= models.CharField(max_length=1000, blank=True, null=True)
    installation_guide= models.TextField(null=True, blank=True)
    image1= models.ImageField(null=True, blank=True)
    image2= models.ImageField(null=True, blank=True)
    image3= models.ImageField(null=True, blank=True)
    image4= models.ImageField(null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description
    
class Firm_Comment(models.Model):
    d_name =  models.ForeignKey(Device, on_delete=models.CASCADE)
    email= models.CharField(max_length=100)
    comment= models.CharField(max_length=200, null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

class Cracked_tools(models.Model):
    device_name= models.ForeignKey(Device, on_delete=models.CASCADE)
    link= models.CharField(max_length=200, null=True, blank=True)
    file =models.FileField(null=True, blank=True)
    description= models.CharField(max_length=1000, blank=True, null=True)
    installation_guide= models.TextField(null=True, blank=True)
    image1= models.ImageField(null=True, blank=True)
    image2= models.ImageField(null=True, blank=True)
    image3= models.ImageField(null=True, blank=True)
    image4= models.ImageField(null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description

class Crack_Comment(models.Model):
    device_name =  models.ForeignKey(Device, on_delete=models.CASCADE)
    email= models.CharField(max_length=100)
    comment= models.CharField(max_length=200, null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

class  VideoTorent(models.Model):
    video_name=models.CharField(max_length=100, primary_key=True)
    category= models.CharField(max_length=100, help_text='use upper case words')
    year_released= models.CharField(max_length=10, null=True, blank=True)
    link= models.CharField(max_length=200, null=True, blank=True)
    file=models.FileField(null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)
    image1= models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.category


class Torent_Comment(models.Model):
    torrent_name=models.ForeignKey(VideoTorent, on_delete=models.CASCADE)
    email= models.CharField(max_length=100)
    comment= models.CharField(max_length=200, null=True, blank=True)
    date_posted= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email