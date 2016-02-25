from django.shortcuts import render

# Create your views here.

from .forms import SignUpForm, ContactForm


def home(request):
    title = 'Welcome'
    # if request.user.is_authenticated():
    #     title = 'My Title %s' %(request.user)
    # else:
    #     title = 'Welcome

    # if request.method == 'POST':
    #     print request.POST
    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = 'Markus'
        instance.save()
        context = {
            'title': 'Thank you'
        }


    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value

        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data.get(key)

        # form_full_name = form.cleaned_data.get('full_name')
        # form_email = form.cleaned_data.get('email')
        # form_message = form.cleaned_data.get('message')
        # print form_full_name
        # print form_email
        # print form_message

    context = {
        'form': form,
    }

    return render(request, "forms.html", context)