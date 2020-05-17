from django import forms


#Signupform
class Signup( forms.Form ):
    FirstName = forms.CharField(max_length=100)
    LirstName = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=100, unique=True)
    Mobile = forms.CharField(max_length=50,primary_key=True)

class Verify ( forms.Form ):
    otp1 = forms.IntegerField()


class Login(forms.Form):
    mobile_no = forms.CharField(max_length=50)



