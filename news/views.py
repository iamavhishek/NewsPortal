from django.shortcuts import render

from .models import *


# Create your views here.
# news = [
#     {"id": 97, 'title': 'Breaking News: Earthquake Strikes City',
#      'content': 'A strong earthquake measuring 6.5 on the Richter scale hit the city today, causing widespread panic among residents. The epicenter was located...',
#      'author': 'John Smith', 'publishDate': '2023-05-29', 'isPublished': True,
#      'description': 'A strong earthquake measuring 6.5 on the Richter scale hit the city today, causing widespread panic among residents.'},
#     {'id': 98, 'title': 'New Study Reveals Benefits of Exercise',
#      'content': 'According to a recent study conducted by scientists at XYZ University, regular exercise has numerous benefits for overall health and well-being...',
#      'author': 'Jane Doe', 'publishDate': '2023-05-28', 'isPublished': True,
#      'description': 'According to a recent study conducted by scientists at XYZ University, regular exercise has numerous benefits for overall health and well-being.'},
#     {'id': 99, 'title': 'Tech Giant Unveils Latest Smartphone',
#      'content': 'In a much-anticipated event, tech giant ABC Corporation unveiled its latest flagship smartphone, boasting advanced features and cutting-edge technology...',
#      'author': 'David Johnson', 'publishDate': '2023-05-27', 'isPublished': False,
#      'description': 'In a much-anticipated event, tech giant ABC Corporation unveiled its latest flagship smartphone, boasting advanced features and cutting-edge technology.'},
#     {'id': 100, 'title': 'Political Leaders Gather for Peace Summit',
#      'content': 'Political leaders from around the world convened today for a peace summit aimed at resolving long-standing conflicts and promoting global harmony...',
#      'author': 'Sarah Thompson', 'publishDate': '2023-05-26', 'isPublished': True,
#      'description': 'Political leaders from around the world convened today for a peace summit aimed at resolving long-standing conflicts and promoting global harmony.'},
#     {'id': 101, 'title': 'Record-Breaking Sales for E-Commerce Giant',
#      'content': 'E-Commerce giant XYZ Inc. announced record-breaking sales for the first quarter of the year, surpassing all previous expectations and setting a new industry benchmark...',
#      'author': 'Michael Brown', 'publishDate': '2023-05-25', 'isPublished': False,
#      'description': 'E-Commerce giant XYZ Inc. announced record-breaking sales for the first quarter of the year, surpassing all previous expectations and setting a new industry benchmark.'},
#     {'id': 102, 'title': 'Entertainment Industry Celebrates Award Winners',
#      'content': 'The entertainment industry came together last night to celebrate the achievements of outstanding artists and performers at the annual awards ceremony...',
#      'author': 'Emily Wilson', 'publishDate': '2023-05-24', 'isPublished': True,
#      'description': 'The entertainment industry came together last night to celebrate the achievements of outstanding artists and performers at the annual awards ceremony.'},
#     {'id': 103, 'title': 'Sports Team Advances to Finals with Thrilling Victory',
#      'content': 'In a nail-biting match, the local sports team secured their spot in the finals after a thrilling victory over their fierce rivals...',
#      'author': 'Robert Davis', 'publishDate': '2023-05-23', 'isPublished': False,
#      'description': 'In a nail-biting match, the local sports team secured their spot in the finals after a thrilling victory over their fierce rivals.'}
# ]


def home(request):
    return render(request, 'news/home.html')


def allnews(request):
    news = News.objects.all()
    return render(request, 'news/all-news.html', {'newsCol': news})


def article(request, id):
    news = News.objects.all()
    singlenews = None
    for i in news:
        if i['id'] == int(id):
            singlenews = i
    context = {'news': singlenews}
    print("Hello")
    print(context)
    return render(request, 'news/article.html', context)


def allcategories(request):
    categories = Category.objects.all()
    return render(request, 'news/category.html', {'categories': categories})
