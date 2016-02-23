from django.shortcuts import render

# Create your views here.

from .forms import SignUpForm


def home(request):
    title = 'Welcome'
    # if request.user.is_authenticated():
    #     title = 'My Title %s' %(request.user)
    # else:
    #     title = 'Welcome

    # if request.method == 'POST':
    #     print request.POST
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        print instance

    context = {
        'title': title,
        'form': form,
    }
    return render(request, "home.html", context)
