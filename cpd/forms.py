from django import forms

class UploadFileForm(forms.Form):
    
    PROGRAM = (
       ("cpp", ("C++")), 
       ("c", ("C")),
    )
    first_file=forms.FileField()
    first_ext = forms.ChoiceField(choices=PROGRAM,label="Select the programming language in which you have written brute force",required=True)
    second_file=forms.FileField()
    second_ext = forms.ChoiceField(choices=PROGRAM,label="Select the programming language in which you have written optimized code",required=True)