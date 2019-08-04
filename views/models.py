from django.views.generic.edit import FormView

from formdy_dynamic_forms.forms import dynamics as dynamics_forms
from formdy.models.api.models import ModelAPI


class ModelFormView(FormView):
    template_name = 'model_form.html'
    form_class = dynamics_forms.ModelForm
    initial = {'hi': 'value'}
    model = None

    def get(self, request, *args, **kwargs):
        model_name = request.GET.get("model", None)
        self.model = ModelAPI(model_name)

        return super(ModelFormView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return super(ModelFormView, self).get_success_url()

    def get_initial(self):
        return self.initial

    def get_form(self, form_class=None):
        return self.form_class(request=self.request, model=self.model, **self.get_form_kwargs())

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
