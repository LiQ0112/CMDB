from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from .models import *
from django.http import JsonResponse,FileResponse

# Create your views here.

from .forms import *
# Create your views here.
#添加用户
def reg(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ''}
        # print("Group:",request.POST.get("group"))
        form_obj = RegForm(request.POST)
        # print(form_obj.is_valid())
        # print(form_obj.errors)

        if form_obj.is_valid():
            print("yes ***********")
            # print(form_obj.cleaned_data)
            #group = Group.objects.get(pk=form_obj.cleaned_data["group"])
            #form_obj.cleaned_data["group"] = group
            # print(111)
            # print(form_obj.cleaned_data["group"],type(form_obj.cleaned_data["group"]))
            # print(form_obj.cleaned_data["depart"],type(form_obj.cleaned_data["depart"]))
           # depart = Department.objects.get(pk=form_obj.cleaned_data["depart"])
            #print(depart)
            #form_obj.cleaned_data["depart"] = depart
            UserInfo.objects.create_user(**form_obj.cleaned_data)
            ret["msg"] = "/index/"
            return JsonResponse(ret)
        else:
            # print("no ***********")
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            return JsonResponse(ret)
    form_obj = RegForm()
    return render(request,'reg.html',locals())
#注销
def logout(request):
    auth.logout(request)
    return redirect("/login/")
#检查新用户名
def check_user(request):
    if request.method == "POST":
        ret = {"status":0,"msg":""}
        username = request.POST.get("username")
        user = UserInfo.objects.filter(username=username)
        if user:
            ret["status"] = 1
            ret["msg"] = "用户名已存在"

        return JsonResponse(ret)
#登陆界面
def login(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/index/')
        else:
            error = "用户名或密码错误！"

    return render(request,'login.html',locals())
#主页
def index(request):
    return render(request,'index.html')
# 基础信息
def equipinfo(request):
    equip_list = EquipInfo.objects.all()
    # print(equip_list)
    depart_list = Department.objects.all()
    classes_list = EquipClass.objects.all()
    ret = {'status':0,'msg':[]}

    # print(request.POST)
    if request.method == 'POST':
        condition = request.POST.get("condition")
        # print(condition,type(condition))
        if condition == '1':
            #按部门查询
            ret['status'] = 1
            depart_id = request.POST.get('depart')
            equip_list = EquipInfo.objects.filter(depart_id=depart_id).values()
            # print(equip_list.first())
            for i in equip_list:
                depart = Department.objects.filter(pk=i['depart_id']).values('title').first()['title']
                i['depart_id'] = depart
                supplier = SupplierInfo.objects.filter(pk=i['supllier_id']).values('title').first()['title']
                i['supllier_id'] = supplier
                classes = EquipClass.objects.filter(pk=i['classes_id']).values('title').first()['title']
                i['classes_id'] = classes
                print(depart,type(depart))
                ret['msg'].append(i)

            # print(equip_list)
        elif condition =='2':
            #按分类查询
            ret['status'] = 1
            classes_id = request.POST.get('classes')
            equip_list = EquipInfo.objects.filter(classes_id=classes_id).values()
            # print(equip_list.first())
            for i in equip_list:
                depart = Department.objects.filter(pk=i['depart_id']).values('title').first()['title']
                i['depart_id'] = depart
                supplier = SupplierInfo.objects.filter(pk=i['supllier_id']).values('title').first()['title']
                i['supllier_id'] = supplier
                classes = EquipClass.objects.filter(pk=i['classes_id']).values('title').first()['title']
                i['classes_id'] = classes
                # print(depart, type(depart))
                ret['msg'].append(i)

        elif condition =='3':
            #按SN查询,需要验证SN码是否存在

            ret['status'] = 1
            sn = request.POST.get('sn')
            print(sn)
            equip_list = EquipInfo.objects.filter(SN=sn).values()
            # print(equip_list.first())
            for i in equip_list:
                depart = Department.objects.filter(pk=i['depart_id']).values('title').first()['title']
                i['depart_id'] = depart
                supplier = SupplierInfo.objects.filter(pk=i['supllier_id']).values('title').first()['title']
                i['supllier_id'] = supplier
                classes = EquipClass.objects.filter(pk=i['classes_id']).values('title').first()['title']
                i['classes_id'] = classes
                # print(depart, type(depart))
                ret['msg'].append(i)

        # print(ret)
        # ret['msg'] = equip_list
        return JsonResponse(ret)
    return render(request,'equipinfo.html',locals())
#添加设备
def equipadd(request):
    if request.method == "POST":
        '''
      
        '''
        EquipInfo.objects.create(
            classes_id=request.POST.get("equipclass"),
            name=request.POST.get("equipname"),
            brand=request.POST.get("equipbrand"),
            types=request.POST.get("equiptypes"),
            SN=request.POST.get("equipsn"),
            date=request.POST.get("equipdate"),
            depart_id=request.POST.get("equipdepart"),
            price=request.POST.get("equipprice"),
            warranty=request.POST.get("equipwarranty"),
            supllier_id=request.POST.get("equipsupplier"),
            remark=request.POST.get("equipremark"),
            contract=request.FILES.get("equipcontract"),
        )
        # print(request.FILES.get("equipcontract"),type(request.FILES.get("equipcontract")))




    class_list = EquipClass.objects.all()
    depart_list = Department.objects.all()
    supplier_list = SupplierInfo.objects.all()
    return render(request,'equipadd.html',locals())

#维修登记
def equipmaintain(request):
    info = ""
    if request.method == "POST":
        print(request.POST)
        EquipMaint.objects.create(
            classes_id=request.POST.get('classes'),
            depart_id=request.POST.get('depart'),
            name=request.POST.get('name'),
            SN=request.POST.get('SN'),
            date=request.POST.get('date'),
            error_description=request.POST.get('error_description'),
            repairs=request.POST.get('repairs'),
            service_person=request.POST.get('service_person'),
            service_result=request.POST.get('service_result'),
            service_cost=request.POST.get('service_cost'),
            service_type=request.POST.get('service_type'),
        )
        # print(123)
        info="保存成功！"
    class_list = EquipClass.objects.all()
    depart_list = Department.objects.all()
    # supplier_list = SupplierInfo.objects.all()
    return render(request,'equipmaintain.html',locals())

#设备调拔登记
def equipallot(request):
    info = ""
    if request.method == "POST":
        EquipAllot.objects.create(
            classes_id = request.POST.get("classes"),
            name = request.POST.get("name"),
            date = request.POST.get("date"),
            SN = request.POST.get("SN"),
            in_depart_id = request.POST.get("in_depart"),
            out_depart_id = request.POST.get("out_depart"),
            remark = request.POST.get("remark"),
        )
        info="保存成功！"

    depart_list = Department.objects.all()
    class_list = EquipClass.objects.all()
    return render(request,'equipallot.html',locals())

#设备报废登记
def euipscrap(request):
    info = ""
    if request.method == "POST":
        try:
            EquipScrap.objects.create(
                classes_id= request.POST.get("classes"),
                name= request.POST.get("name"),
                SN= request.POST.get("SN"),
                buy_date= request.POST.get("buy_date"),
                scrap_date= request.POST.get("scrap_date"),
                depart= request.POST.get("depart"),
                price= request.POST.get("price"),
                remark= request.POST.get("remark"),
                supllier_id= request.POST.get("supllier"),
            )
        except:pass
    supplier_list = SupplierInfo.objects.all()
    depart_list = Department.objects.all()
    class_list = EquipClass.objects.all()
    return render(request,'euipscrap.html',locals())

#厂商基础信息
def supplerinfo(request):
    supplies_list = SupplierInfo.objects.all()
    return render(request,'supplerinfo.html',locals())

#新建厂商
def suppleradd(request):
    try:
        if request.method == 'POST':
            SupplierInfo.objects.create(
                title = request.POST.get("title"),
                linkman = request.POST.get("linkmen"),
                address = request.POST.get("address"),
                pnone = request.POST.get("phone"),
            )
    except:pass
    return render(request,"suppleradd.html",locals())


#合同展示并查询
def contractlist(request):
    contract_list = ContractDetail.objects.all()
    return render(request,'contractlist.html',locals())

#新增合同
def constractadd(request):
    try:
        if request.method == "POST":
            ContractDetail.objects.create(
                classes_id=request.POST.get("constractclass"),
                title=request.POST.get("constrattitle"),
                date=request.POST.get("constractdate"),
                supplier_id=request.POST.get("supplier"),
                person=request.POST.get("constractperson"),
                contractfile=request.FILES.get("contractfile"),
            )
    except:pass
    classes_list = ContractClass.objects.all()
    supplier_list = SupplierInfo.objects.all()

    return render(request,'constractadd.html',locals())

#合同类型维护
def contractclass(request):
    #展示所有的合同类型
    classes_list = ContractClass.objects.all()

    return render(request,'contractclass.html',locals())

#添加合同分类
def classadd(request):
    # ret = {'status':0,'msg':""}
    if request.method == "POST":
        title = request.POST.get("title")
        ContractClass.objects.create(title=title)
        ret = {'status':1,'msg':""}
        return JsonResponse(ret)
pass
#合同下载
def contract_download(request,id):
    #通过设备信息表查询合同
    contract = EquipInfo.objects.filter(pk=id).values("contract").first().get("contract")
    file = open('media/'+contract,'rb')
    # print(contract,type(contract))
    filename = contract.split('/')[1]
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s'%filename
    return response

#维修查询
def maintaininfo(request):


    maintain_list = EquipMaint.objects.all()
    depart_list = Department.objects.all()
    classes_list = EquipClass.objects.all()
    ret = {'status': 0, 'msg': []}

    # print(request.POST)
    if request.method == 'POST':
        condition = request.POST.get("condition")
        # print(condition,type(condition))
        if condition == '1':
            # 按部门查询
            ret['status'] = 1
            depart_id = request.POST.get('depart')
            maintain_list = EquipMaint.objects.filter(depart_id=depart_id).values()
            # print(maintain_list.first())
            for i in maintain_list:
                depart = Department.objects.filter(pk=i['depart_id']).values('title').first()['title']
                i['depart_id'] = depart
                # supplier = SupplierInfo.objects.filter(pk=i['supllier_id']).values('title').first()['title']
                # i['supllier_id'] = supplier
                classes = EquipClass.objects.filter(pk=i['classes_id']).values('title').first()['title']
                i['classes_id'] = classes
                service_type = EquipMaint.objects.filter(service_type=i['service_type']).first().get_service_type_display()
                i['service_type'] = service_type
                # print(depart, type(depart))
                ret['msg'].append(i)

            # print(ret)
        elif condition == '2':
            # 按分类查询
            ret['status'] = 1
            classes_id = request.POST.get('classes')
            # print(classes_id)
            maintain_list = EquipMaint.objects.filter(classes_id=classes_id).values()
            print(maintain_list)
            for i in maintain_list:
                depart = Department.objects.filter(pk=i['depart_id']).values('title').first()['title']
                i['depart_id'] = depart
                # supplier = SupplierInfo.objects.filter(pk=i['supllier_id']).values('title').first()['title']
                # i['supllier_id'] = supplier
                classes = EquipClass.objects.filter(pk=i['classes_id']).values('title').first()['title']
                i['classes_id'] = classes
                # print(classes)
                # print('i',i)
                service_type = EquipMaint.objects.filter(service_type=i['service_type']).first().get_service_type_display()
                i['service_type'] = service_type
                # print(depart, type(depart))
                ret['msg'].append(i)
        elif condition == '3':
            # 按SN查询,需要验证SN码是否存在

            ret['status'] = 1
            sn = request.POST.get('sn')
            print(sn)
            maintain_list = EquipMaint.objects.filter(SN=sn).values()
            # print(equip_list.first())
            for i in maintain_list:
                depart = Department.objects.filter(pk=i['depart_id']).values('title').first()['title']
                i['depart_id'] = depart
                # supplier = SupplierInfo.objects.filter(pk=i['supllier_id']).values('title').first()['title']
                # i['supllier_id'] = supplier
                classes = EquipClass.objects.filter(pk=i['classes_id']).values('title').first()['title']
                i['classes_id'] = classes
                service_type = EquipMaint.objects.filter(
                    service_type=i['service_type']).first().get_service_type_display()
                i['service_type'] = service_type
                # print(depart, type(depart))
                ret['msg'].append(i)

        # print(ret)
        # ret['msg'] = equip_list
        return JsonResponse(ret)
    return render(request,'maintaininfo.html',locals())

def reset_password(request):
    return render(request,'base1.html')

#修改密码
def set_password(request):
    ret = {"status": 0, "msg": ""}
    if request.method == "POST":
        user = request.user
        new_password = request.POST.get("new_password")
        old_password = request.POST.get("old_password")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            ret["status"] =1
            ret["msg"] = "修改成功！"
            return JsonResponse(ret)
        else:
            ret["msg"]="原密码输入有误，请重新输入！"
    return JsonResponse(ret)

#校验原密码
def check_password(request):
    if request.method =="POST":
        ret={"status":0,"msg":""}
        user = request.user.username
        # passpword = UserInfo.objects.filter(username=user).values("password")
        # print(passpword)

        old_password = request.POST.get("ori_password")
        print()
        # print(ori_password,type(ori_password))
        # print(user,type(user))
        user1 = auth.authenticate(username=user,password=old_password)
        if user1:
            return JsonResponse(ret)
        else:
            ret["status"] =1
            ret["msg"] = "原密码输入有误！"
        # print("user:",user)
        # print(123321)
        return JsonResponse(ret)


def mi(request):
    return render(request,'mi.html')



