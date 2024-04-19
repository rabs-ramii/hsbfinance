# Generated by Django 4.1.7 on 2024-04-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsblimited', '0015_alter_loanapplication_loan_amount'),
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
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=30),
        ),
    ]
