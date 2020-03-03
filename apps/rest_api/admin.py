from django.contrib import admin
from . import models

# Way 1 -----------------------------------------
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	pass

# Way 2 -----------------------------------------
class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Comment, CommentAdmin)
