from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

from .forms import SignUpForm, ContactForm
from .models import SignUp


def home(request):
    title = 'Join Us Now'
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

    if request.user.is_authenticated() and request.user.is_staff:
        # print SignUp.objects.all()
        # for item in SignUp.objects.all():
        #    print item.full_name
        queryset = SignUp.objects.all().order_by('-timestamp') # .filter(full_name__icontains='Markus')
        # print SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains='Markus').count()
        context = {
            'queryset': queryset
        }

    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'
    title_align_center = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data.get(key)
        form_full_name = form.cleaned_data.get('full_name')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        # print form_full_name
        # print form_email
        # print form_message
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourotheremail@email.com']
        contact_message = '%s: %s via %s' %(form_full_name, form_message, form_email)
        send_mail(subject, contact_message, from_email, [to_email], fail_silently=False)
    context = {
        'form': form,
        'title': title,
        'title_align_center': title_align_center,
    }

    return render(request, "forms.html", context)