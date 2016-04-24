from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^get-user-name/$',views.get_user_name, name="get_user_name"),
url(r'^bits-line/$',views.bits_line, name="bits_line"),
url(r'^missed-call/$',views.missed_call, name="missed_call_post"),
url(r'^about/$',views.about, name="view_about"),
url(r'^accounts/logout/$',views.auth_logout, name="logout"),
url(r'^accounts/login/$',views.auth_login, name="login"),
url(r'^accounts/register/$',views.auth_register, name="register"),
url(r'^accounts/forgot/$',views.auth_forgot, name="forgot-pass"),
url(r'^accounts/reset/$',views.auth_reset_pass, name="reset-pass"),
url(r'^$', views.home,name='home'),
url(r'^services/$', views.services,name='services'),
url(r'^my-services/$', views.my_services,name='myservices'),
url(r'^del-service/(?P<service_id>\d+)/$', views.del_service,name='delservice'),
url(r'^del-ad/(?P<ad_id>\d+)/$', views.del_classified,name='delad'),
url(r'^del-problem/(?P<p_id>\d+)/$', views.del_problem,name='delproblem'),
url(r'^problems/(?P<bhavan>[A-Z]+)/$', views.problems,name='problems'),
url(r'^problem/vote/$', views.vote_problem,name='voteproblem'),
url(r'^my-problems/(?P<bhavan>[A-Z]+)/$', views.my_problems,name='myproblems'),
url(r'^problems/(?P<bhavan>[A-Z]+)/solved$', views.problems_solved,name='problems_solved'),
url(r'^solve_problem/(?P<p_id>\d+)/$', views.solve_problem,name='solve_problem'),
url(r'^calendar/$', views.calendar,name='calendar'),
url(r'^travel/$', views.travel,name='travel'),
url(r'^my-travel/$', views.my_travel,name='mytravel'),
url(r'^del-travel/(?P<t_id>\d+)/$', views.del_travel,name='deltravel'),
url(r'^ads/$', views.classifieds,name='ads'),
url(r'^my-ads/$', views.my_classifieds,name='myads'),
url(r'^course_help/notes/(?P<course>[A-Z]+).pdf$', views.notes, name='notes')
url(r'^course_help/handout/(?P<course>[A-Z]+).pdf$', views.handout, name='handout'),
url(r'^course_help/books/(?P<course>[A-Z]+).pdf$', views.books, name='books'),
url(r'^course_help/(?P<course>[A-Z]+)/$', views.course,name='course'),
]