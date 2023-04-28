from django.shortcuts import render
from django.views import View
from .models import News


class NewsListView(View):
    template_name = 'news/news_list.html'

    def get(self, request):
        # получаем список новостей из базы данных
        news = News.objects.all()

        # передаем список новостей в шаблон
        context = {
            'news': news
        }
        return render(request, self.template_name, context)


class NewsDetailsView(View):
    template_name = 'news/news_details.html'

    def get(self, request, news_id):
        # получаем объект новости из базы данных
        news = News.objects.get(id=news_id)

        # передаем объект новости в шаблон
        context = {
            'news': news
        }
        return render(request, self.template_name, context)
