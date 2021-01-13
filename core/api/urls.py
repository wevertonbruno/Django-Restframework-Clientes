from django.urls import path
from core.api.views import ApiGETClienteView, ApiPUTClienteView, ApiPOSTClienteView, ApiDELETEClienteView, ApiLISTClienteView

app_name="clientes"

urlpatterns = [
    path("", ApiLISTClienteView, name="list"),
    path("<name>/", ApiGETClienteView, name="detail"),
    path("<name>/update", ApiPUTClienteView, name="update"),
    path("<name>/delete", ApiDELETEClienteView, name="delete"),
    path("create", ApiPOSTClienteView, name="create"),

]