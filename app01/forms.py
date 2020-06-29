from django import forms
from .models import *

class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        error_messages={
            "required":"用户名不能为空",
            "max_length":"用户名不能超过16位"
        },
        widget=forms.widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "用户名"
            }
        )
    )

    password = forms.CharField(
        min_length=6,
        label="密码",
        error_messages={
            "required":"密码不能为空",
            "min_length":"密码不能少于6位"
        },
        widget=forms.widgets.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "密码"
            }
        )
    )



    phone = forms.CharField(
        max_length=11,
        label="手机号",
        error_messages={
            "required":"手机号不能为空",
            "max_length":"手机号长度有误"
        },
        widget=forms.widgets.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"手机号"
            }
        )
    )

