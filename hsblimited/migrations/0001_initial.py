# Generated by Django 4.1.7 on 2024-04-10 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('loan_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=100)),
                ('loan_amount', models.IntegerField()),
                ('address', models.CharField(max_length=254)),
                ('approved_amount', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=30)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hsblimited.user')),
            ],
        ),
    ]
