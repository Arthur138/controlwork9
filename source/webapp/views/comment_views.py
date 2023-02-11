from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView
from webapp.forms import CommentsForm
from webapp.models import Comment , Ads
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class CommentDelete(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:ad_detail', kwargs={'pk': self.object.ad.pk})




class CommentsCreate(CreateView):
    model = Comment
    form_class = CommentsForm

    def form_valid(self, form):
        ad = get_object_or_404(Ads, pk=self.kwargs.get('pk'))
        form.instance.comment_author = self.request.user
        form.instance.ad = ad
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:ad_detail', kwargs={'pk': self.object.ad.pk} )

