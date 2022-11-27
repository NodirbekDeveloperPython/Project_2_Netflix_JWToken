from django.contrib import admin
from django.urls import path, include
from filmapp.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('kinolar', KinolarViewSet)
router.register('aktyorlar', AktyorlarViewSet)



urlpatterns = [
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(router.urls)),

    path('admin/', admin.site.urls),

    path('commentlar/', CommentlarAPIView.as_view()),

    # path('kinolar/', KinolarAPIView.as_view()),

    # path('aktyorlar/', AktyorlarAPIView.as_view()),
]
