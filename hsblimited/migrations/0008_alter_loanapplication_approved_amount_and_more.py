# Generated by Django 4.1.7 on 2024-04-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsblimited', '0007_alter_loanapplication_approved_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='approved_amount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]