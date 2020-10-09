from django.shortcuts import render

# Create your views here.
# templates 에서 만든 index.html을 메인에 띄워주는 함수 생성 -> url 생성하러 가야함
def index(request):
    return render(request, 'index.html')