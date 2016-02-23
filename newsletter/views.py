from django.shortcuts import render

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        title = 'My Title %s' %(request.user)
    else:
        title = 'Welcome'
    context = {
        'title': title,
    }
    return render(request, "home.html", context)
