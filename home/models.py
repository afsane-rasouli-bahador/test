from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator



class Board(models.Model):
    class TypeBoard(models.TextChoices):
        TODO = 'Todo', 'todo'
        DOING = 'Doing', 'doing'
        DONE = 'Done', 'Done'
    title = models.CharField(max_length = 200, null=True)
    description = models.TextField(null = True)
    board_type = models.CharField(max_length = 8, choices = TypeBoard.choices, default = TypeBoard.DOING)

    def __str__(self) -> str:
        return self.title



class Todo(models.Model):
    class Degree_select(models.TextChoices):
        HIGH = 'H', 'High'
        MEDDIUME = 'M', 'Mediume'
        LOW = 'L', 'Low'


    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to='todo_pic/', null=True)
    starred = models.BooleanField(default = False)
    Degree_of_Importance = models.CharField(max_length =1 ,choices = Degree_select.choices,default = Degree_select.MEDDIUME)
    created = models.DateTimeField(auto_now_add = True)
    started = models.DateTimeField(default = timezone.now)
    updated = models.DateTimeField(auto_now = True)
    board = models.ForeignKey(Board, on_delete= models.CASCADE, related_name = 'todo', null = True)
    
    def __str__(self) -> str:
        return self.title




