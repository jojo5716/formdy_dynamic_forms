from django import forms

EXTRA_ATTRS = ["regex"]


def input(input_data):
    def get_extra_attrs():
        extra_attrs = {}
        for extra_attr in EXTRA_ATTRS:
            if extra_attr in input_data:
                extra_attrs[extra_attr] = input_data[extra_attr]

        return extra_attrs

    return forms.CharField(
        label=input_data["name"],
        required=input_data["required"],
        max_length=input_data["max_length"],
        initial=input_data.get("default", ""),
        widget=forms.TextInput(
            attrs={
                "placeholder": input_data["placeholder"],
                "type": input_data["field_type"],
                **get_extra_attrs()
            })
    )
