from django.db import models
from django.core.validators import MaxValueValidator

MONSTER_TYPE = (
    ("abberation", "Абберация"),
    ("beast", "Зверь"),
    ("celestial", "Небожитель"),
)

class EntityMixin(models.Model):
    name = models.CharField(verbose_name="Имя персонажа",max_length=50, blank=True)
    speed_walk = models.PositiveSmallIntegerField(verbose_name="Скорость ходьбы", blank=True)
    speed_swim = models.PositiveSmallIntegerField(verbose_name="Скорость плавания", blank=True)
    speed_fly = models.PositiveSmallIntegerField(verbose_name="Скорость полета", blank=True)
    dark_vision = models.PositiveSmallIntegerField(verbose_name="Тёмное зрение", blank=True)
    conditions = models.ManyToManyField("Condition", verbose_name="Состояния")
    class Meta:
        abstract = True

class CharList(EntityMixin, models.Model):
    player_name = models.CharField(verbose_name="Имя игрока",max_length=50, blank=True)
    level = models.PositiveSmallIntegerField(verbose_name="Уровень", blank=True, validators=[MaxValueValidator(20)])

   
class Monster(EntityMixin, models.Model):
    monster_type = models.CharField(choices=MONSTER_TYPE, max_length=50, blank=True)
    source = models.ForeignKey("Source", verbose_name="Источник", on_delete=models.CASCADE)

class Condition(models.Model):
    name = models.CharField(verbose_name="Состояние",max_length=50, blank=True)
    properties = models.JSONField()
    
class Source(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50, blank=True)
    abbriviature = models.CharField(verbose_name="Сокращенно", max_length=10, blank=True)