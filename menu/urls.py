from django.urls import path
from rest_framework import routers

from menu import views


router = routers.SimpleRouter()
router.register(
    r'section',
    views.SectionViewset,
    basename='section'
)
router.register(
    r'item',
    views.ItemViewset,
    basename='item'
)
router.register(
    r'modifiers',
    views.ModifiersViewset,
    basename='modifiers'
)

urlpatterns = [
	path(
        'modifier-to-item-mapping/',
        views.ModifierToItemMappingApiView.as_view(),
        name='modifier-to-item-mapping'
    ),path(
        'all-menu/',
        views.GetAllMenuListApiView.as_view(),
        name='all-menu'
    ),
]

urlpatterns += router.urls