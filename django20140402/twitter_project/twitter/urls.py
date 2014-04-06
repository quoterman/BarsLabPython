
from django.conf.urls import url, patterns
from twitter.views import LoginView

urlpatterns = patterns('twitter.views',
    url(r'^$', 'home', name='home'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', 'log_out', name='logout'),
    url(r'settings/$', 'settings', name='settings'),
    url(r'registration/$', 'registration', name='registration'),
)