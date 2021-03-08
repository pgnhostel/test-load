from django.shortcuts import render, redirect
from . models import Pgs
from . forms import PgsForm


def home(request):
    pgs = Pgs.objects.all()
    return render(request, 'home.html', {'pgs': pgs})


def upload_pgs(request):
    if request.method == 'POST':
        form = PgsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PgsForm()
    return render(request, 'upload_pgs.html', {
        'form': form
    })

