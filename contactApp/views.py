from django.shortcuts import render


# Create your views here.
def contact(request):
	return render(request, 'contact.html', {
		'active_menu': 'contact',
		'sub_menu': 'mycontact', # 导航条的二级控件id，在/templates/xxx.html的导航条的对应链接里
	})
# active_menu的作用就是指示当前页面所属的导航菜单项，以便在页面上高亮显示该菜单项。在这里，active_menu的值为'contact'，
# 说明当前页面属于导航菜单中的联系方式（contact）部分。


from .models import Ad
from .forms import ResumeForm


def recruit(request):
	AdList = Ad.objects.all().order_by('-publishDate')
	if request.method == 'POST':
		resumeForm = ResumeForm(data=request.POST, files=request.FILES)
		if resumeForm.is_valid():
			resumeForm.save()
			return render(request, 'success.html', {
				'active_menu': 'contactus',
				'sub_menu': 'recruit',
			})
	else:
		resumeForm = ResumeForm()
	return render(
		request, 'recruit.html', {
			'active_menu': 'contactus',
			'sub_menu': 'recruit',
			'AdList': AdList,
			'resumeForm': resumeForm,
		})