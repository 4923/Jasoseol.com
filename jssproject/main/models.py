from django.db import models

# Create your models here.

# class 이름은 첫글자 대문자, 의미단위
class Jasoseol(models.Model):
# Model을 상속받아 model 만든다
  title = models.CharField(max_length = 50)
  # CharField는 항상 max_length를 정해줘야한다
  content = models.TextField()
  # TextField()는 max_length를 필수인자로 받지 않는다.
  updated_at = models.DateTimeField(auto_now=True)
  # auto_now=True: 업데이트 된 시간과 날짜를 자동으로 updated_at에 저장함
  
