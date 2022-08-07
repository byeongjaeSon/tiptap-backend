from django.contrib import admin

# Register your models here.
from app.models import CheckList, RoomInfo, Room

# admin 페이지에서 확인할 모델 추가
admin.register(CheckList)
admin.register(RoomInfo)
admin.register(Room)