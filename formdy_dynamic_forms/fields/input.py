from django import forms


def input(input_data):
    def get_extra_attrs():
        extra_attrs = {}
        if "regex" in input_data:
            extra_attrs["regex"] = input_data["regex"]

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
