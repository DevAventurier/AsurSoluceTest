from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings


# @login_required(login_url=settings.LOGIN_URL)
def dashboard(request, page=1):
    tempale_name = "custom_users/index.html"
    # departements_count = Department.objects.count()
    # employees_count = Employee.objects.count()
    # gymCenters_count = GymCenter.objects.count()
    # subscriptions_count = Subscription.objects.count()
    # data = {
    #     'departements_count': departements_count,
    #     'employees_count': employees_count,
    #     'gymCenters_count': gymCenters_count,
    #     'subscriptions_count': subscriptions_count,
    # }
    data = {
        "is_navbar": True,
        "is_menu": True,
    }
    return render(request, tempale_name, context=data)


