from django import forms
from formdy_dynamic_forms.fields import input as input_fields

MAP_FIELDS = {
    "input": {
        "text": input_fields.input,
        "password": input_fields.input,
    }
}


class ModelForm(forms.Form):
    def __init__(self, request, model, *args, **kwargs):
        self.request = request
        self.model = model
        super(ModelForm, self).__init__(*args, **kwargs)

        if model:
            model_fields = model.fields()

            for field in model_fields:
                field_name = field["name"]
                render_field_func = MAP_FIELDS[field["element_type"]][field["field_type"]]

                self.fields[field_name] = render_field_func(field)
