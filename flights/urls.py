from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet, CityViewSet, AirportViewSet, AirplaneTypeViewSet, AirplaneViewSet,
    CrewViewSet, RouteViewSet, FlightViewSet, OrderViewSet, TicketViewSet
)

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'airports', AirportViewSet)
router.register(r'airplanetypes', AirplaneTypeViewSet)
router.register(r'airplanes', AirplaneViewSet)
router.register(r'crew', CrewViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = router.urls
