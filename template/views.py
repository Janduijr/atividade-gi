from django.shortcuts import render

def nova_view(request):
    return render(request, 'template_novo.html', {'autor': 'jandui'})