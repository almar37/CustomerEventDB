# Generated by Django 4.1.7 on 2023-02-26 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_rename_staff_teacher_rename_staff_customer_teacher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='surname',
            new_name='event',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='teacher',
        ),
    ]
