from django.http import HttpResponse
from django.shortcuts import render
from app_media.forms import *
from django.views import *


class UploadFileView(View):
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name + ' size: '+ str(file.size), status=200)
    def get(self, request):
        form = UploadFileForm()
        return render(request,'media/upload_file.html', context={'form':form})