from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('signup/,', views.signup,name='signup'),
    path('book/<int:book_id>/',views.detail,name='detail'),
    path('create/',views.createbook,name='createbook'),
    path('<int:book_id>/create/',views.createreview,name='createreview'),
    path('review/<int:review_id>/',views.updatereview,name='updatereview'),
    path('review/<int:review_id>/delete/',views.deletereview,name='deletereview'),
]
