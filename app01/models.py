from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
#用户信息表
class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11,verbose_name="手机号")

    class Meta:
        verbose_name = "用户信息表"
#设备分类表
class EquipClass(models.Model):
    title = models.CharField(unique=True,max_length=32,verbose_name="分类标题")
    code = models.IntegerField(verbose_name='分类编号')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='设备分类表'

#厂商信息表
class SupplierInfo(models.Model):
    title = models.CharField(max_length=128,verbose_name="厂商名称")
    linkman = models.CharField(max_length=32,verbose_name='联系人',null=True)
    pnone = models.CharField(max_length=11,verbose_name='联系电话')
    address = models.CharField(max_length=128,verbose_name="地址")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "厂商信息表"

#设备状态表
class EquipState(models.Model):
    code = models.IntegerField(verbose_name="状态码")
    title = models.CharField(max_length=32,verbose_name="状态标题")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "状态表"

#设备基础信息表
class EquipInfo(models.Model):
    classes = models.ForeignKey(to='EquipClass',verbose_name="设备分类")
    name = models.CharField(max_length=32,verbose_name="设备名称")
    brand = models.CharField(max_length=32,verbose_name='品牌')
    types = models.CharField(max_length=64,verbose_name="型号",null=True)
    SN = models.CharField(max_length=64,verbose_name="出厂编号")
    date = models.DateField(verbose_name="采购日期")
    depart = models.ForeignKey(to='Department', verbose_name="使用部门",default="")
    price = models.FloatField(verbose_name="采购价格")
    warranty = models.CharField(max_length=32,verbose_name="保修期")
    remark = models.CharField(max_length=64,verbose_name="备注",null=True)
    supllier = models.ForeignKey(to='SupplierInfo',verbose_name="厂商",null=True)
    contract = models.FileField(upload_to='contract/',verbose_name="合同",null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "设备基础信息表"


#设备维修表
class EquipMaint(models.Model):
    classes = models.ForeignKey(to='EquipClass',verbose_name='设备类型')
    depart = models.ForeignKey(to='Department',verbose_name="使用部门")
    name = models.CharField(max_length=32,verbose_name="设备名称",default="",unique=False)
    SN = models.CharField(max_length=128,verbose_name="出厂编号")
    date = models.DateField(verbose_name="报修时间")
    error_description = models.CharField(max_length=256,verbose_name="故障描述")
    repairs = models.CharField(max_length=32,verbose_name="报修人")
    service_person = models.CharField(max_length=32,verbose_name="维修人")
    service_result = models.CharField(max_length=128,verbose_name="维修结论")
    service_cost = models.CharField(max_length=32,verbose_name="维修费用")
    service_type_choices = (
        (1,'保内维修'),
        (2,'过保厂家收费'),
        (3,'过保自行维修'),
    )
    service_type = models.IntegerField(choices=service_type_choices,verbose_name='维修方式',default=1)
    # service_cost = models.CharField(max_length=32,verbose_name="维修费用")

    class Meta:
        verbose_name="设备维修表"

#机构信息表
class Organ(models.Model):
    title = models.CharField(max_length=32,verbose_name="机构名称")
    code = models.CharField(max_length=32,verbose_name="机构代码")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "机构信息表"

#部门信息表
class Department(models.Model):
    organ = models.ForeignKey(to="Organ",verbose_name="机构")
    title = models.CharField(max_length=32,verbose_name="部门名称")
    code = models.CharField(max_length=16,verbose_name="部门编号")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "部门信息表"

#合同分类表
class ContractClass(models.Model):
    title = models.CharField(max_length=32,verbose_name="分类标题")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "合同分类表"

#合同详情表
class ContractDetail(models.Model):
    classes = models.ForeignKey(to="ContractClass",verbose_name="分类")
    title = models.CharField(max_length=32,verbose_name="合同标题")
    date = models.DateField(verbose_name="签订时间")
    supplier = models.ForeignKey(to='SupplierInfo',verbose_name='厂商',default='')
    person = models.CharField(max_length=32,verbose_name="签订人")
    contractfile = models.FileField(upload_to='contract/',verbose_name="合同附件")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="合同详情表"

#设备调拔记录表
class EquipAllot(models.Model):
    classes = models.ForeignKey(to="EquipClass",verbose_name="设备分类",default="")
    name = models.CharField(max_length=32,verbose_name="设备名称")
    date = models.DateField(verbose_name="调拔时间",auto_now=True)
    SN = models.CharField(max_length=32,verbose_name="设备出厂编码")
    in_depart = models.ForeignKey(to="Department",verbose_name="调入部门",related_name="in_part",default='')
    out_depart = models.ForeignKey(to="Department",verbose_name="调出部门",related_name="out_part",default='')
    remark = models.CharField(verbose_name="备注",max_length=64)

#资产报废表
class EquipScrap(models.Model):
    classes = models.ForeignKey(to='EquipClass', verbose_name="设备分类")
    name = models.CharField(max_length=32, verbose_name="设备名称")
    # brand = models.CharField(max_length=32, verbose_name='品牌')
    # types = models.CharField(max_length=64, verbose_name="型号", null=True)
    SN = models.CharField(max_length=64, verbose_name="出厂编号")
    buy_date = models.DateField(verbose_name="采购日期")
    scrap_date = models.DateField(verbose_name="报废日期")
    depart = models.ForeignKey(to='Department', verbose_name="使用部门", default="")
    price = models.FloatField(verbose_name="采购价格")
    # warranty = models.CharField(max_length=32, verbose_name="保修期")
    remark = models.CharField(max_length=64, verbose_name="备注", null=True)
    supllier = models.ForeignKey(to='SupplierInfo', verbose_name="采购厂商", null=True)
    # contract = models.FileField(upload_to='contract/', verbose_name="合同", null=True)

    class Meta:
        verbose_name = "资产报废表"
# 电子价格牌信息表
class ElectronicTag(models.Model):
    pass






