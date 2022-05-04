import json
from datetime import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
import random


def index(request):
    return redirect('/news/')


def news_post(request, post_id):
    with open('hypernews/news.json', 'r') as news_json:
        data = json.load(news_json)
        for item in data:
            if item['link'] == post_id:
                return render(request, "news/news_post.html", context={'item': item})
        return HttpResponseNotFound("aboba")


def main_page(request):
    with open('hypernews/news.json', 'r') as news_json:
        data = json.load(news_json)
        data.sort(key=get_sort_attr, reverse=True)
        q = request.GET.get('q')
        if q is not None:
            filtered_data = []
            for item in data:
                if q in item['title']:
                    filtered_data.append(item)
            data = filtered_data
            print(data)
        items = {}
        for item in data:
            date = item['created'].split(' ')[0]
            if date not in items:
                items[date] = []
            items[date].append(item)

        return render(request, "news/main_page.html", context={'items': items.items()})


def get_sort_attr(item):
    return item['created']


def create(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    if title and text:
        with open('hypernews/news.json', 'r') as news_json:
            data = json.load(news_json)
        links = []
        for item in data:
            links.append(item['link'])

        while True:
            link = random.randint(0, 9999999999)
            if link not in links:
                break
        new_item = {
            'created': datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
            'title': title,
            'text': text,
            'link': link,
        }
        data.append(new_item)
        with open('hypernews/news.json', 'w') as news_json:
            json.dump(data, news_json)
        return redirect('/news/')
    return render(request, "news/create.html")
