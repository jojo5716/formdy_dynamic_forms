from django import forms


def input(input_data):
    return forms.CharField(
        label=input_data["name"],
        required=input_data["required"],
        max_length=input_data["max_length"],
        initial=input_data.get("default", ""),
        widget=forms.TextInput(
            attrs={
                "placeholder": input_data["placeholder"],
                "type": input_data["field_type"],
            })
    )
