from django.shortcuts import render

from users.models import Profile


def profile(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)
