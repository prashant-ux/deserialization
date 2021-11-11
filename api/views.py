from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
# Create your views here.
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg'  : 'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, comtent_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, comtent_type='application/json')
