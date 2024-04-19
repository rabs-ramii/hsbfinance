# Generated by Django 4.1.7 on 2024-04-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsblimited', '0012_alter_loanapplication_approved_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='approved_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='status',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
