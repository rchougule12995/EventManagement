from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import EventPostModelForm
from .models import EventPost


def event_post_list_view(request):
    # list out objects
    # could be search
    qs = EventPost.objects.filter(status='published') # queryset -> list of python object
    #if request.user.is_authenticated:
    #my_qs = EventPost.objects.filter(user=request.user)
    #qs = (qs | my_qs).distinct()
    template_name = 'event/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


# @login_required
@staff_member_required
def event_post_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    form = EventPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = EventPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def event_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(EventPost, slug=slug)
    template_name = 'event/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def event_post_update_view(request, slug):
    obj = get_object_or_404(EventPost, slug=slug)
    form = EventPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)


@staff_member_required
def event_post_delete_view(request, slug):
    obj = get_object_or_404(EventPost, slug=slug)
    template_name = 'event/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/event")
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def event_post_archive_view(request, slug):
    obj = get_object_or_404(EventPost, slug=slug)
    print(obj.status)
    obj.status='archive'
    print("NEW STATUS")
    print(obj.status)
    obj.save()
    return redirect('/event')
