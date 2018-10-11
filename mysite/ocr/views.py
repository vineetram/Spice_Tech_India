from django.shortcuts import render, render_to_response
from PIL import Image
import pytesseract
from .models import document
from .forms import DocumentForm
from django.http import HttpResponse
import os

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = document(docfile=request.FILES['docfile'])
            newdoc.save()
            documents = document.objects.all()
            if(os.name=='nt'):
                pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
            data = pytesseract.image_to_string(Image.open(documents[len(documents)-1].docfile))
            form = DocumentForm()
            return render(request, 'ocr/list.html', {'data':data, 'form':form, 'documents':documents[len(documents)-1]})
        else:
            form = DocumentForm()
    else:
        form = DocumentForm()
        return render(request, 'ocr/list.html', {'form':form})
