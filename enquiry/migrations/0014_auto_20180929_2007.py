# Generated by Django 2.1.1 on 2018-09-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0013_auto_20180926_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='courses',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='enquries', to='enquiry.Course'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]