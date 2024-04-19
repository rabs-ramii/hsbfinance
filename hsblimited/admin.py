from django.contrib import admin
from hsblimited.models import User,LoanApplication

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('email','fullname','mobile','gender','password')
admin.site.register(User,UserAdmin)


class LoanApplicationAdmin(admin.ModelAdmin):
    list_display=('loan_id','user_email','loan_type','loan_amount','address','approved_amount','status')

admin.site.register(LoanApplication,LoanApplicationAdmin)
