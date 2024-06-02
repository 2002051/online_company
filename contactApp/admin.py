from django.contrib import admin
from .models import Ad

admin.site.register(Ad)

# 默认的注册模式：
# from .models import Resume
# admin.site.register(Resume)

# 一种定制化后台管理系统展示列表的方法
from django.utils.safestring import mark_safe
from .models import Resume


class ResumeAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'personID', 'birth', 'edu', 'school',
	                'major', 'position', 'image_data')
	
	def image_data(self, obj):
		return mark_safe(u'<img src="%s" width="120px" />' % obj.photo.url)
	
	image_data.short_description = u'个人照片'


admin.site.register(Resume, ResumeAdmin)
