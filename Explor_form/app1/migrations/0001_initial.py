# Generated by Django 5.0.6 on 2024-07-02 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('big_auto_field', models.BigAutoField(primary_key=True, serialize=False)),
                ('big_integer_field', models.BigIntegerField()),
                ('boolean_field', models.BooleanField()),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='files/')),
                ('image_field', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('foreign_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_foreign_key', to='app1.othermodel')),
                ('many_to_many_field', models.ManyToManyField(related_name='contact_many_to_many', to='app1.othermodel')),
                ('one_to_one_field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_one_to_one', to='app1.othermodel')),
            ],
        ),
    ]