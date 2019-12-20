from django.shortcuts import render,render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def teacher(r):
    return HttpResponse("这是一个teacher的视图")

def v2_exception(r):
    raise Http404  #一旦引发异常，就转入异常处理，后面不执行了。
    return HttpResponse("OK")

def v10_1(r):
    return HttpResponseRedirect('/v11')

def v10_2(r):
    return HttpResponseRedirect(reverse('v11'))

def v11_1(r):
    return HttpResponse("这是V11的返回")

def v8_get(request): #测试url：http://127.0.0.1:7777/v8/?k1=daiye&k2=male
    rst = '' #result的缩写
    print(request.GET)
    print(type(request.GET))
    for k,v in request.GET.items():
        rst += k + "-->" + v
        rst += ','
    return HttpResponse("Get value of Request is {0}".format(rst))


# 通过render_to_response制作一个表单
def v9_get(request):
    #渲染一个模板并且返回
    return render_to_response("for_post.html")


def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "-->" + v
        rst += ","

    return HttpResponse("Get value of POST is {0} ".format(rst))

def render_test(request):
    # 环境变量，就是一个字典
    # c = dict()
    rsp = render(request,"render.html")
    return rsp

def render2_test(request):
    # 环境变量，就是一个字典
    c = dict()
    c["name"] = "daiye"
    c["sex"] = "man"
    rsp = render(request,"render2.html", context= c)
    return rsp

def render3_test(request):
    from django.template import loader
    # 得到模板
    t = loader.get_template("render2.html")
    r = t.render({"name" : "daiye"})
    return HttpResponse(r) #用r来实例化一个http response

def render4_test(request):

    # 反馈回模板render2.html
    rsp = render_to_response("render2.html", context = {"name" : "daiye"} )
    return rsp

def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request, Exception)