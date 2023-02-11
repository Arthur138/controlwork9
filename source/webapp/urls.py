from django.contrib import admin
from django.urls import path
from webapp.views import AdsList , AdDetail , AdsCreate , AdsUpdate,AdsDelete ,  CommentsCreate , CommentDelete , ListMooderateComments , ModerYesView ,ModerNoView

app_name = 'webapp'

urlpatterns = [
    path('', AdsList.as_view() , name='index'),
    path('ad_detail/<int:pk>/', AdDetail.as_view(), name='ad_detail'),
    path('adds/add/', AdsCreate.as_view(), name='ad_create'),
    path('adds/<int:pk>/update/', AdsUpdate.as_view(), name='ad_update'),
    path('adds/<int:pk>/delete/', AdsDelete.as_view(), name='ad_delete'),
    path('adds/<int:pk>/comments_add/', CommentsCreate.as_view(), name='comments_create'),
    path('adds/<int:pk>/comments_delete/', CommentDelete.as_view(), name='comments_delete'),
    path('adds/moderation/', ListMooderateComments.as_view(), name='ad_moder_list'),
    path('adds/<int:pk>/moderation/yes/', ModerYesView.as_view(), name='moder_choose_yes'),
    path('adds/<int:pk>/moderation/no/', ModerNoView.as_view(), name='moder_choose_no'),
]