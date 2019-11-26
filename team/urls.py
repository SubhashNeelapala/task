from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
url(r'^team/create$',views.TeamListViewSet.as_view(),name='cerate_team'),
url(r'^player/create$',views.PlayerListViewSet.as_view(),name='cerate_team'),
url(r'^player/by/team/(?P<team_id>[\w-]+)/$',views.PlayerListByTeam.as_view(),name='cerate_team'),
url(r'^match/fixtures$',views.MatchCreateViewSet.as_view(),name='cerate_match'),
url(r'^match_list$',views.MatchesListViewSet.as_view(),name='matches_list'),
url(r'^create/points/winner$',views.CreatPointWinnerMatches.as_view(),name='create_points_winners'),
url(r'^get/points/winner$',views.CreatPointWinnerMatches.as_view(),name='get_winner_points')




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

