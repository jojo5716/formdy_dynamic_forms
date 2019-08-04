from django.urls import reverse
from django.views.generic.edit import FormView

from formdy_dynamic_forms.forms import dynamics as dynamics_forms
from formdy.models.api.models import ModelAPI


class ModelFormView(FormView):
    template_name = 'model_form.html'
    form_class = dynamics_forms.ModelForm
    initial = {}
    model = None

    def setup(self, request, *args, **kwargs):
        model_name = kwargs.get("model_name", None)
        if model_name:
            self.model = ModelAPI(model_name)
        else:
            self.model = None

        return super(ModelFormView, self).setup(request, *args, **kwargs)

    def get_initial(self):
        return self.initial

    def get_form(self, form_class=None):
        return self.form_class(request=self.request, model=self.model, **self.get_form_kwargs())

    def form_valid(self, form):
        # form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('formdy_dynamic_form_render_model_form', args=[self.kwargs["model_name"]])
