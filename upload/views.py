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
file_data = pd.read_csv('C:\\Users\\BISP 123\\PycharmProjects\\Integration\\media\\january.csv',
                        delimiter=',', dtype={"Count": float},
                        usecols=['Technology', 'Count', 'Location', 'Experience', 'Comapany', 'Salary'],
                        na_values=['.', '??'])


# Homepage
class Home(TemplateView):
    template_name = 'upload/home.html'


# Function for uplaod file
@csrf_exempt
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload/upload.html', context)


# Function For DataVisualization
def question(request):
    return render(request, 'upload/question.html')


# function for changeradiobutton
def radio(request):
    chart_type = request.POST.get('chartType');

    return chart_type


# Function For file
@csrf_exempt
def file_reader(request):
    chart_type = radio(request)
    pivot_data = file_data.pivot_table(index='Technology', aggfunc=[sum], fill_value=0)

    p = pivot_data.plot(kind=chart_type)
    plt.axis('off')
    tbl = table(p, pivot_data, loc='bottom')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(14)
    plt.tight_layout()
    print('\n')
    plt.title('Job Opening In Jan According To Technologies')
    plt.ylabel('No Of Opening')
    plt.xlabel('Technology Name')
    plt.legend().set_visible(False)

    # fig = matplotlib.pyplot.gcf()
    # plt.figure(figsize=(8, 18))
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.figure(figsize=(10, 6), dpi=300)
    # plt.rcParams["figure.figsize"] = [16, 9]
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'upload/question.html', {'graphic': graphic})
    # return HttpResponse(data)


# Function For Question1
@csrf_exempt
def Answer1(request):
    chart_type = radio(request)
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

    return render(request, 'upload/question.html', {'graphic': graphic})
    # return HttpResponse(data)


# function For Question2
@csrf_exempt
def Answer2(request):
    chart_type = radio(request)

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

    return render(request, 'upload/question.html', {'graphic': graphic})


# function for Question3
@csrf_exempt
def Answer3(request):
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

    return render(request, 'upload/question.html', {'graphic': graphic})


# function For Question6
@csrf_exempt
def Answer6(request):
    chart_type = request.POST.get('chartType');

    pivot_data = file_data.pivot_table(index='Comapany', values='Count', aggfunc=[sum], fill_value=0)
    pivot_data.head()
    # pivot_data.top(10)
    # sorted(pivot_data, key=lambda x: int(x))
    # pivot_data.plot(kind=chart_type)
    pivot_data.plot(kind='bar')
    plt.tight_layout()
    print('\n')
    plt.title('Tableau Opening In Top 10 Comapany')
    plt.ylabel('No Of Opening')
    plt.xlabel('Comapany Name')
    #plt.legend().set_visible(False)

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

    return render(request, 'upload/question.html', {'graphic': graphic})


# function For Question8
@csrf_exempt
def Answer8(request):
    chart_type = request.POST.get('chartType');
    file_data1 = pd.read_csv('C:\\Users\\BISP 123\\PycharmProjects\\Integration\\media\\salary.csv',
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

    return render(request, 'upload/question.html', {'graphic': graphic})


# class For GeneratePdf
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('upload/charts.html')
        pdf = render_to_pdf('upload/charts.html')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Opening In Jan_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
    # Function For ReadFile
