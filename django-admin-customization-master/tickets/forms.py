from django import forms
from django.forms import ModelForm, RadioSelect

from .models import Ticket


class TicketAdminForm(ModelForm):
    first_name = forms.CharField(label="First name", max_length=32)
    last_name = forms.CharField(label="Last name", max_length=32)

    class Meta:
        model = Ticket
        fields = ["concert", "first_name", "last_name", "payment_method", "is_active"]
        widgets = {
            "payment_method": RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance")
        initial = {}

        if instance:
            customer_full_name_split = instance.customer_full_name.split(
                " ", maxsplit=1
            )
            initial = {
                "first_name": customer_full_name_split[0],
                "last_name": customer_full_name_split[1],
            }

        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.customer_full_name = (
            self.cleaned_data["first_name"] + " " + self.cleaned_data["last_name"]
        )
        return super().save(commit)
    

class TicketForm(forms.ModelForm):
    # 驗證資料正確與否
    first_name = forms.CharField(label="First name", max_length=32)
    last_name = forms.CharField(label="Last name", max_length=32)

    class Meta:
        model = Ticket
        fields = ["payment_method", "first_name", "last_name"]

        widgets = {
            "payment_method": forms.RadioSelect(),
        }
        choices = [
            ("CC", "Credit card"),
            ("DC", "Debit card"),
            ("ET", "Ethereum"),
            ("BC", "Bitcoin"),
        ]

class ConcertForm(forms.Form):
    CATEGORY_CHOICES = [
        ('concerts', 'Concerts'),
        ('tickets', 'Tickets'),
        ('venues', 'Venues'),
    ]

    category = forms.ChoiceField(label='Concert Category', choices=CATEGORY_CHOICES)


