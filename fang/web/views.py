from django.shortcuts import render
from django.http import HttpResponse
from web.models import Fang,Hot
from urllib import parse
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # 接受查询参数
    kw = request.GET.get('kw','')
    #户型
    housetype = request.GET.get('housetype','')
    #区域
    region = request.GET.get('region','')
    #总价
    totalPrice = request.GET.get('totalPrice','')
    if totalPrice:
        if '-' in totalPrice:
            smoney = int(totalPrice.split('-')[0])
            emoney = int(totalPrice.split('-')[1])


        else:
            smoney = ''
            emoney = ''
    else:
        smoney = ''
        emoney = ''
    #页数
    pn = request.GET.get('pn','')
    if pn:
        try:
            pn = int(pn)
        except Exception as e:
            pn = 1
    else:
        pn = 1
    #面积
    # # acreage = request.GET.get('acreage','')
    # if acreage:
    #     if '-' in acreage:
    #         sacreage = float(acreage.split('-')[0])
    #         eacreage = float(acreage.split('-')[1])
    #         print(eacreage)
    query = {}
    # if acreage:
    #     query['acreage__gte'] = float(sacreage)
    #     query['acreage__lte'] = eacreage


    if kw:
        query['title__contains'] = kw
    if region:
        query['region'] = region
    if totalPrice:
        query['totalPrice__gte'] = int(smoney)
        query['totalPrice__lte'] = int(emoney)

    if housetype:
        query['housetype__contains'] = housetype

    #查询所有的信息
    fang_list = Fang.objects.filter(**query).all()[:1000]
    #分页
    paginator = Paginator(fang_list,20)
    try:
        fang_list = paginator.page(pn)
    except Exception as e:
        fang_list = paginator.page(1)

    start =int(pn) - 3
    end = int(pn) + 4

    if start <= 0:
        start = 1
    if end >= paginator.num_pages:
        end = paginator.num_pages + 1

    page_num = range(start, end)


    qs = parse.urlencode(request.GET)
    # 获取搜索条件
    hot_list1 = Hot.objects.filter(status=1, cat=1).order_by('-weight').all()
    hot_list2 = Hot.objects.filter(status=1, cat=2).order_by('-weight').all()
    hot_list3 = Hot.objects.filter(status=1, cat=3).order_by('-weight').all()
    hot_list4 = Hot.objects.filter(status=1, cat=4).order_by('-weight').all()

    return render(request,'index.html',locals())
def data(request):
    return render(request,'data.html')