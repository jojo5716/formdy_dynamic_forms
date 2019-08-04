from django import forms

MAP_INPUT_TYPE = {
    "text": forms.TextInput,
    "password": forms.PasswordInput,
}


def input(input_data):
    field_widget = MAP_INPUT_TYPE[input_data["field_type"]]

    return forms.CharField(
        label=input_data["name"],
        required=input_data["required"],
        max_length=input_data["max_length"],
        widget=field_widget(
            attrs={'placeholder': input_data["placeholder"]})
    )
