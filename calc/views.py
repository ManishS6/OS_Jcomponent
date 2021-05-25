from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,'home.html',{"name":"Manish"})

def add(req):
    val1 = req.POST['text1']
    val2 = req.POST['text2']
    # val1 = req.POST.get('num1',False)
    # val2 = req.POST.get('num2',False)
    # val1 = "kou"
    # val2 = "shiki"
    result = val1+val2
    return HttpResponse(result)
    # return render(req, 'result.html' ,{'result': result})

def test(req):
    var1 = req.POST['choice'] # choice of radio button
    var2 = req.POST['text2'] # key
    tester = var1 + " " + var2
    return({'choice': tester})

# from django.shortcuts import render
# from rest_framework.views import APIView
# from . models import *
# from rest_framework.response import Response
# from . serializer import *
# # Create your views here.

# class ReactView(APIView):
	
# 	serializer_class = ReactSerializer

# 	def get(self, request):
# 		detail = [ {"name": detail.name,"detail": detail.detail}
# 		for detail in React.objects.all()]
# 		return Response(detail)

# 	def post(self, request):

# 		serializer = ReactSerializer(data=request.data)
# 		if serializer.is_valid(raise_exception=True):
# 			serializer.save()
# 			return Response(serializer.data)
