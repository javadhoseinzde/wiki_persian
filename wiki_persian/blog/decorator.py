from functools import wraps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from wiki_persian.users.models import Profile


def check_permission(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        query =  Profile.objects.get(user=request.user)
        if request.user.is_special_month == True:
            print("okey")
            # return HttpResponseRedirect(reverse_lazy("blog:create_article"))
            return view_func(request, *args, **kwargs)

        elif query.post_status == True:
            return view_func(request, *args, **kwargs)

            # return HttpResponse("this user not special but post status True")

        else:
            # You can add your redirect logic here, e.g., redirect to login page.
            # For simplicity, let's just return an HttpResponse for demonstration purposes.
            return HttpResponseRedirect(reverse_lazy("users:profile"))

    return _wrapped_view
