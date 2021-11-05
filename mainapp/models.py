from django.db import models

# Create your models here.
from django.urls import reverse
from PIL import Image

class Company_Data(models.Model):
    '''회사 정보 
    추가해야될 내용 : 카테고리 , 좌표 
    '''

    # 검색 기능에는 회사이름 , 지역 , 속한 제품명 3가지를 통해서 구현할 예정임 -> 어떤식으로 모델을 나누는게 좋을지 아직 못정함

    # 회사 이름
    company_name=models.CharField(
        max_length=100,
        blank=False,
        verbose_name='회사 이름', )
    # 대표자
    ceo_of_company = models.CharField(
        max_length=50,
        verbose_name='회사 대표',)
    #설립연도
    year_of_establishment = models.CharField(
        max_length=15,
    verbose_name='설립 연도',)
    #지역
    area=models.CharField(
        max_length=50,
        verbose_name='지역'
        )
    #전화번호
    number=models.CharField(
        max_length=12,
        verbose_name='전화번호',
        )
    #이메일주소
    email_address=models.CharField(
        max_length=50,
        verbose_name='이메일 주소',
        )
    #홈페이지
    homepage=models.CharField(
        max_length=30,
        verbose_name='홈페이지',
        )
    #회사소개
    introduce_company=models.TextField(
        verbose_name='회사 소개'
    )#제한 자체를 두지 않기 위해서 Textfield 사용.

    company_image = models.ImageField(
        upload_to='images/' , 
        default='DEFAULT VALUE',
        null=True)

    #회사 카테고리
    Category_choices = (("bolt","볼트"),("nut","너트"),("반도체","반도체"))
    company_category = models.CharField(max_length= 10, choices = Category_choices)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.company_image.path)

        if img.height >256 or img.width >256:
            output_size = (256,256)
            img.thumbnail(output_size)
            img.save(self.company_image.path)



class Category(models.Model):
    name = models.CharField(max_length=50, )
    slug = models.SlugField(max_length=200, allow_unicode=True, default='DEFAULT VALUE',unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categories'

class Product(models.Model):
    ''' 
    회사 제품 
    위의 company_data 와 1:n관계를 맺고있도록 설정.
    
    제품이름 / 카테고리 / 가격 /관계표시 

    추가할 내용 : 사진업로드 
    '''
    product_name=models.CharField(max_length=100)
    category = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default = "select")
    image = models.ImageField(upload_to='images/' , default='DEFAULT VALUE',null=True)

    post = models.ForeignKey(to=Company_Data , null=True,on_delete=models.CASCADE,)
    category = models.ForeignKey(to=Category, null=True, on_delete=models.SET_NULL,)


    def __str__(self):
        return self.product_name
