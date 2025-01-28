from django.contrib import admin
from .models import *

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ["monster_type"]

@admin.register(CharList)
class CharlistAdmin(admin.ModelAdmin):
    list_display = ["name", "player_name", "level", "speed_fly"]
    
@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ["name", "properties"]