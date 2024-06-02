from django.contrib import admin
from .models import MyNew
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm


class MyNewForm(ModelForm):
	class Meta:
		model = MyNew
		fields = '__all__'
		widgets = {
			'description': CKEditorWidget(),
		}


@admin.register(MyNew)
class MyNewAdmin(admin.ModelAdmin):
	form = MyNewForm
	
	class Media:
		js = (
			'ckeditor/ckeditor.js',
			'ckeditor/init.js',
		)
