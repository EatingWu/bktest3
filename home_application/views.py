# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context,render_json
from home_application.models import Studentinfo
from common.log import logger


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def student_manage(request):
    """
    学生管理
    """
    data = Studentinfo.objects.all()
    return render_mako_context(request, '/home_application/student_manage.html',{'data': data})

def search_student(request):
     name_info = request.POST.get('name_info')
     student = Studentinfo.objects.filter(name__icontains=name_info).values()
     result_list = []
     for stu in student:
         stu_obj = {}
         stu_obj["id"] = stu["id"]
         stu_obj["name"] = stu["name"]
         stu_obj["age"] = stu["age"]
         stu_obj["gender"] = stu["gender"]
         result_list.append(stu_obj)
     return render_json({'result': True, 'student': result_list})

def add_student(request):
    gender_info = request.POST.get('gender_info')
    name_info = request.POST.get('name_info')
    age_info = request.POST.get('age_info')
    Studentinfo.objects.create(name=name_info, gender=gender_info,
                                     age=age_info)
    return render_json({'result': True})

def edit_student(request):
    gender_info = request.POST.get('gender_info')
    name_info = request.POST.get('name_info')
    age_info = request.POST.get('age_info')
    id = request.POST.get('id')
    Studentinfo.objects.filter(id=id).update(name=name_info, gender=gender_info,age=age_info)
    return render_json({'result': True})

def del_student(request):
    id = request.POST.get('id')
    Studentinfo.objects.get(id=id).delete()
    return render_json({'result': True})

def export_student(request):
    student = Studentinfo.objects.all()
    logger.info(u"学生信息是：{}".format(student))
    result_list = []
    for i in student:
            result_list.append(i.toDic())
    return render_json({'result': True, 'student': result_list})