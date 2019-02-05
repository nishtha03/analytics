import pandas as pd
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt;
import numpy as np
from pandas.plotting import table

plt.rcdefaults()
from collections import defaultdict
import io

plt.style.use('ggplot')
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.generic import View
from .util import render_to_pdf
from django.template.loader import get_template
import base64

# Global variable
file_data = pd.read_csv('C:\\Users\\BISP 123\\PycharmProjects\\Integration\\media\\crm1.csv',
                        delimiter=',', dtype={"Count": float},
                        usecols=['Count', 'Location', 'Experience', 'Technology', 'Company', 'Salary'],
                        na_values=['.', '??'])


# Function For crm
def crm(request):
    return render(request, 'upload/crm.html')


# Function For Question1
@csrf_exempt
def crm1(request):
    # chart_type = radio(request)
    pivot_data = file_data.pivot_table(index='Technology', values='Count', aggfunc=[sum], fill_value=0)

    # pivot_data.plot(kind=chart_type)
    pivot_data.plot(kind='bar')
    plt.tight_layout()
    print('\n')
    plt.title('Job Opening In Jan According To Technologies')
    plt.ylabel('No Of Opening')
    plt.xlabel('Technology Name')
    plt.legend().set_visible(False)

    # fig = matplotlib.pyplot.gcf()
    # plt.figure(figsize=(8, 8))
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.figure(num=None, figsize=(6, 3), dpi=50)
    # plt.rcParams["figure.figsize"] = [16, 9]
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'upload/crm.html', {'graphic': graphic})


@csrf_exempt
def crm2(request):
    pivot_data = file_data.pivot_table(index='Location', columns='Technology', values='Count', aggfunc=[sum],
                                       fill_value=0)
    # pivot_data.plot(kind=chart_type)
    pivot_data.plot(kind='bar', stacked='True')

    plt.tight_layout()
    print('\n')
    plt.title('Job Opening In Jan According To Locations')
    plt.ylabel('No Of Opening')
    plt.xlabel('Locations')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.figure(num=None, figsize=(6, 3), dpi=50)
    # plt.rcParams["figure.figsize"] = [16, 9]
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'upload/crm.html', {'graphic': graphic})


# function for Question3
@csrf_exempt
def crm3(request):
    chart_type = request.POST.get('chartType');

    pivot_data = file_data.pivot_table(index='Experience', columns='Technology', values='Count', aggfunc=[sum],
                                       fill_value=0)
    # pivot_data.plot(kind=chart_type)
    pivot_data.plot(kind='barh')
    plt.tight_layout()
    print('\n')
    plt.title('Job Opening In Jan According To Experience')
    plt.ylabel('No Of Opening')
    plt.xlabel('Experience')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.figure(num=None, figsize=(6, 3), dpi=50)
    # plt.rcParams["figure.figsize"] = [16, 9]
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'upload/crm.html', {'graphic': graphic})


# function For Question6
@csrf_exempt
def crm6(request):
    chart_type = request.POST.get('chartType');

    pivot_data = file_data.pivot_table(index='Company', values='Count', aggfunc=[sum], fill_value=0)
    pivot_data.head()
    # pivot_data.top(10)
    # sorted(pivot_data, key=lambda x: int(x))
    # pivot_data.plot(kind=chart_type)
    pivot_data.plot(kind='bar')
    plt.tight_layout()
    print('\n')
    plt.title('MicrosoftCRM Opening In Top 10 Comapany')
    plt.ylabel('No Of Opening')
    plt.xlabel('Comapany Name')
    plt.legend().set_visible(False)

    # fig = matplotlib.pyplot.gcf()
    # plt.figure(figsize=(8, 8))
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.figure(num=None, figsize=(6, 3), dpi=50)
    # plt.rcParams["figure.figsize"] = [16, 9]
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'upload/crm.html', {'graphic': graphic})


# function For Question8
@csrf_exempt
def crm8(request):
    chart_type = request.POST.get('chartType');
    file_data1 = pd.read_csv('C:\\Users\\BISP 123\\PycharmProjects\\Integration\\media\\salarycrm.csv',
                             delimiter=',', dtype={"Count": float}, usecols=['Technology', 'Count', 'Salary', ],
                             na_values=['.', '??']);
    pivot_data = file_data1.pivot_table(index='Salary', columns='Technology', values='Count', aggfunc=[sum],
                                        fill_value=0)

    pivot_data.plot(kind='bar')
    plt.tight_layout()
    print('\n')
    plt.title('Opening In Jan According To Salary')
    plt.ylabel('No Of Opening')
    plt.xlabel('Salary')
    plt.legend().set_visible(False)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.figure(num=None, figsize=(6, 3), dpi=50)
    # plt.rcParams["figure.figsize"] = [16, 9]
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'upload/crm.html', {'graphic': graphic})
