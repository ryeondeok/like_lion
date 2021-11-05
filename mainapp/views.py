from django.core import paginator
from django.core.paginator import Paginator
from django.db.models.enums import Choices
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Company_Data, Product ,Category


def mainpage(request):
    return render(request,'mainpage.html')


def company_list(request):
    company_list_all = Company_Data.objects.all()
    category = Category.objects.all()
    # 검색용
    search_key = request.GET.get('search_key','')
    if search_key:
        company_list = company_list_all.filter(company_name__contains = search_key)
        page = request.GET.get('page','1') #페이지 조회
        paginator = Paginator(company_list,10) #페이지 10개당 조회
        page_obj = paginator.get_page(page)
        context={'company_list_all':company_list, 'category':category, 'page_obj':page_obj, "search_key":search_key} 
        return render(request ,'company_list.html' , context)
    else:
        page = request.GET.get('page','1') #페이지 조회
        paginator = Paginator(company_list_all,10) #페이지 10개당 조회
        page_obj = paginator.get_page(page)
        context={'company_list_all':company_list_all, 'category':category, 'page_obj':page_obj, "search_key":search_key} 
        return render(request ,'company_list.html' , context)




def company_detail(request,id):
    company_id = Company_Data.objects.get(id=id)
    product = Product.objects.all()
    context ={'company_id':company_id ,'product':product , }
    return render(request, 'company_product.html', context)


# 이부분이 제일 마음에 안듬
def checkbox(request):
    choices = Category.objects.all().values_list("name","name")
    choice_list = []
    for item in choices:
        choice_list.append(item)
    # want에 전체 카테고리의 이름이 리스트에 저장되어 있음. 

    product=Product.objects.all()
    if request.method == 'POST':
        c_id=[]
        product_name=[]
        checkbox_data=request.POST.getlist('checks[]') # 선택한체크박스의 id 가 들어있음
        for c in checkbox_data:
            c=c.split('.')
            product_name.append(c[0])
            c_id.append(int(c[1]))

        context = {'checkbox_data':checkbox_data , 'product':product ,'product_name':product_name ,'c_id':c_id }
        return render(request,'checkbox_data.html' , context)
    else:
        return redirect('/')

