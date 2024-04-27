from django.shortcuts import render
from .models import SiteSettings, AboutUsQuestions, SiteUsersAbout, Team
from accounts.models import Account
from contact_us.models import Contact, RateUs
from recommend_app.models import PlatformsLessons
# Create your views here.
def home(request):
    data = {
        'banners': SiteSettings.objects.all(),
        'banner_total': 3,
        'questions': AboutUsQuestions.objects.all(),
        'students': SiteUsersAbout.objects.all(),
        'teams': Team.objects.all(),
        'users': Account.objects.all(),
        'rates': RateUs.objects.all(),
        'lessons': PlatformsLessons.objects.all()


    }


    if request.method == 'POST':
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            message = request.POST.get('text')
            text = Contact.objects.create(
                full_name=full_name,
                email=email,
                text=message
            )


    return render(request, 'index.html', data)

