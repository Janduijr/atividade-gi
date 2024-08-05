from django.shortcuts import render

def nova_view(request):
feature-jandui
    return render(request, 'template_novo.html', {'autor': 'jandui'})
=======
    return render(request, 'template_novo.html', {'autor': 'camille'})
develop
