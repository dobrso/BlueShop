from django.shortcuts import render

from reviews.models import Review


def review_list(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'reviews/review_list.html', context)