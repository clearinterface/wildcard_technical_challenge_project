from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"words", views.CensoredWordsViewSet, basename="censored-urls")
urlpatterns = router.urls
