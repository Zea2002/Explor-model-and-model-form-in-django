from django.db import models

class OtherModel(models.Model):
    name = models.CharField(max_length=100)

class Contact(models.Model):
    big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE, related_name='contact_foreign_key')
    image_field = models.ImageField(upload_to='images/')
    many_to_many_field = models.ManyToManyField(OtherModel, related_name='contact_many_to_many')
    one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE, related_name='contact_one_to_one')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
