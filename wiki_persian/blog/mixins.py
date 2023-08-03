from wiki_persian.users.models import Profile
from django.http import Http404



class FormValidMixin():
	def form_valid(self ,form):
			ins = form.save(commit=False)
			ins.user = self.request.user
			ins.save()
			if self.request.user.is_special_month == False:
				query = Profile.objects.filter(user=self.request.user).update(post_status="False")
			else:
				return super().form_valid(form)
			return super().form_valid(form)
	


class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_special_month or request.user.is_admin:
			# self.fields = ['user', 'slug','name', 'text' ,'level',  'time',  'term_number',  'start_time',  'Status', 'price']
			self.fields = ("title", "slug", "desctiption", "thumbnail", "category", "status")
		elif request.user.is_active:
			self.fields = ("title", "slug", "desctiption", "thumbnail", "category")

		else:
			raise Http404("شما اجازه ورود ندارید")
		return super().dispatch(request, *args, **kwargs)
