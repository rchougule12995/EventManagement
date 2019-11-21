from django.shortcuts import render

from event.models import EventPost

from .models import SearchQuery

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        event_list = EventPost.objects.search(query=query)
        context['event_list'] = event_list
    return render(request, 'searches/view.html',context)
