from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from short_url.models import ShortURL
from .forms import ShortURLForm


class MainView(View):

    def get(self, request, *args, **kwargs):
        form = ShortURLForm()
        context = {'form': form}
        return render(request, 'short_url.html', context)

    def post(self, request, *args, **kwargs):
        form = ShortURLForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                url = form.cleaned_data['url']
                obj = ShortURL.objects.get_or_create(url=url)[0]
                context = {'obj': obj}
                return render(request, 'short_url.html', context)
        context = {'form': form}
        return render(request, 'short_url.html', context)


def redirect_view(request, short_code=None):
    obj = get_object_or_404(ShortURL.objects.get_active_url(),
                            short_code=short_code)
    return HttpResponseRedirect(obj.url)
