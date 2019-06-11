from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import renderers

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#             # path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#             # path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#             # path('users/', views.UserList.as_view(), name='user-list'),
#             # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
#             # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#             # path('', views.api_root)
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
