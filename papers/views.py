from django.shortcuts import render, HttpResponse
from papers.models import Papers
# Create your views here.


def HomeView(request):

    all_papers = Papers.objects.all()

    context = {
        'all_papers': all_papers
    }
    return render(request, 'papers/paper.html', context )
