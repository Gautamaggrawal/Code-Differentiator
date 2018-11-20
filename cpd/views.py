from django.shortcuts import render,HttpResponseRedirect
from cpd.forms import UploadFileForm
import subprocess

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():            
            file1_ext=form.cleaned_data.get("first_ext")
            file2_ext=form.cleaned_data.get("second_ext")
            file1=request.FILES['first_file']
            file2=request.FILES['second_file']
            outputdif=compare(file1_ext,file2_ext,file1,file2)	
            return render(request, 'cpd/index.html', {'form': form,'out':outputdif })


        else:
            form = UploadFileForm(request.POST, request.FILES)
            return render(request, 'cpd/index.html', {'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'cpd/index.html', {'form':form})    

def compare(file1_ext,file2_ext,file1,file2):
	print(file1_ext,file2_ext,file1,file2)
	f1='file1.'+file1_ext
	f2='file2.'+file2_ext
	with open(f1, 'wb+') as destination:
		for chunk in file1.chunks():
			destination.write(chunk)
	with open(f2, 'wb+') as destination:
		for chunk in file2.chunks():
			destination.write(chunk)
	chcom1='chmod 777 '+f1
	chcom2='chmod 777 '+f2
	f1 = 'file1.' + file1_ext +' file1.s'
	f2 = 'file2.' + file2_ext +' file2.s'
	b1='bash comC++.sh '+f1
	b2='bash comC++.sh '+f2
	b3='bash comC.sh '+f1
	b4='bash comC.sh '+f2
	subprocess.call(chcom1,shell=True)
	subprocess.call(chcom2,shell=True)
	if file1_ext=='c':
		subprocess.call(b3,shell=True)
	if file2_ext=='c':
		subprocess.call(b4,shell=True)
	if file1_ext=='c++':
		subprocess.call(b1,shell=True)
	if file2_ext=='c++':
		subprocess.call(b2,shell=True)


	ff='file1.s '+'file2.s '+' output.txt'
	final_script='bash diff.sh '+ff
	subprocess.call(final_script,shell=True)
	output=open('output.txt','r+')
	outputdif=(output.readlines())
	return(outputdif)

















