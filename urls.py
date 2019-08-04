from django.conf.urls import url

from formdy_dynamic_forms.views import models

urlpatterns = [
    url(r'model/render-form/(?P<model_name>[\w.,/_\-]+)/$',
        models.ModelFormView.as_view(),
        name='formdy_dynamic_form_render_model_form'),
]
