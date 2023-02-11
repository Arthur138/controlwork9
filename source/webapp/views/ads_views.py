from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Ads
from webapp.forms import AdsForm , CommentsForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class AdsList(ListView):
    template_name = 'ads/index.html'
    context_object_name = 'ads'
    model = Ads

    def get_queryset(self):
        return super().get_queryset().filter(status='published').order_by('-created_at')

class AdDetail(DetailView):
    template_name = 'ads/ads_detail.html'
    context_object_name = 'ad'
    model = Ads

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = self.object.comment.all()
        # if not self.request.user.has_perm('webapp.view_not_moderated_reviews'):
        #     reviews = reviews.filter(moderated=True)
        context['form'] = CommentsForm
        context['comments'] = comment.order_by('-created_at')
        return  context

class AdsCreate(LoginRequiredMixin, CreateView):
    form_class = AdsForm
    model = Ads
    template_name = 'ads/ad_create.html'

    def form_valid(self, form):
        author = self.request.user
        form.instance.ads_author = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:ad_detail', kwargs={'pk': self.object.pk})

class AdsUpdate(PermissionRequiredMixin, UpdateView):
    form_class = AdsForm
    model = Ads
    template_name = 'ads/ad_update.html'

    def get(self, request, *args, **kwargs):
        ad =  get_object_or_404(Ads, pk = self.kwargs.get('pk'))
        if ad.status == 'rejected':
            raise PermissionDenied()
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.status = 'for_moderation'
        return super().form_valid(form)

    def has_permission(self):
        return self.get_object().ads_author == self.request.user

    def get_success_url(self):
        return reverse('webapp:ad_detail', kwargs={'pk': self.object.pk})

class AdsDelete(PermissionRequiredMixin, DeleteView):
    model = Ads
    template_name = 'ads/ad_delete.html'
    permission_required = 'webapp.delete_review'
    context_object_name = 'ad'

    def has_permission(self):
        return self.get_object().ads_author == self.request.user

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = 'for_delete'
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('webapp:index')