from django.shortcuts import redirect, render

# Create your views here.
from django.db.models import Q
from mainapp.models import Company_Data





def search(request):
    company_list = Company_Data.objects.all()
    search_key = request.GET.get('search_key')

    if search_key :
        search_key=Company_Data.objects.filter(
        Q(company_name__icontains=search_key) |
        Q(number__icontains=search_key) |
        Q(area__icontains=search_key)
    )
        context={'search_key':search_key}
        return render(request , 'search.html' , context)
    else :
        return redirect('company_list')