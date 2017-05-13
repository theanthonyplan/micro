from django.conf.urls import include, url

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# from spyrit.views import ProfileViewSet


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'Comments': reverse('comment-list', request=request, format=format),
#         'Topics': reverse('topic-list', request=request, format=format),
#         'Profiles': reverse('userprofile-list', request=request, format=format),
#         'Category': reverse('category-list', request=request, format=format),
    })



urlpatterns = [
    url(r'^$', api_root),
    # url(r'^spyrit/', include('spyrit.urls')),       # spyrit
]
