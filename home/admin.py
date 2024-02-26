from django.contrib import admin
from .models import Todo, Board

@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):
    list_display = ['title', 'starred', 'created', 'Degree_of_Importance', 'description']
    list_filter = ['title', 'description', 'Degree_of_Importance']
    list_editable = ['starred', 'Degree_of_Importance']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Board)
class AdminBoard(admin.ModelAdmin):
    list_display = ['title', 'description', 'board_type']
    list_filter = ['title', 'description']
    list_editable = ['board_type']