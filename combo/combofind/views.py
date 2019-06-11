from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from combofind import comboapp
from combofind import mailsend
from django.conf import settings
import os


# Create your views here.
def index(request):
	context={'done':"FIle  UplOaded"}
	if request.method=='POST':
		

		uploaded_file = request.FILES['data']
		fs = FileSystemStorage()
		if os.path.exists(settings.MEDIA_ROOT+'/'+uploaded_file.name):#deletes pre existing file with same name
			os.remove(settings.MEDIA_ROOT+'/'+uploaded_file.name)
		fs.save(uploaded_file.name,uploaded_file)
		l=int(request.POST['low'])
		h=int(request.POST['high'])
		to=request.POST['email']
		result=comboapp.combo(settings.MEDIA_ROOT+'/'+uploaded_file.name,l,h)
		if len(result)==0:
			context['result']=99
		else:	
			context['result']= result
			mailsend.mailer(result,to)

	return render(request,'combofind/index.html',context)