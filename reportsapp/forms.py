from django import forms
from django.forms import fields, ModelForm, Form
from reportsapp.database_repository.models import Costs, FixedCosts, Documents


class DayForm(forms.Form):
    min_date_field = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),label="od daty")
    max_date_field = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),label="do daty")


class MonthForm(forms.Form):
    min_date_field = fields.DateField(input_formats=['%Y-%m'], widget=forms.widgets.DateInput(attrs={'type': 'month'}),label="od daty")
    max_date_field = fields.DateField(input_formats=['%Y-%m'], widget=forms.widgets.DateInput(attrs={'type': 'month'}),label="do daty")




class CostsForm(ModelForm):
    class Meta:
        model = Costs

        fields = ("invoice_no","date_cost", "num_items_buy", "unit_price_usd", "tax_total_usd", "shipping_total_usd",'net_total_usd')
        labels = {
            'invoice_no': 'Numer fv.',
            'date_cost': 'Data z fv.',
            'num_items_buy': 'Ilość szt. z fv.',
            'unit_price_usd': 'Cena za sztukę z fv.',
            'tax_total_usd': 'Cło w % wg. kat. towaru',
            'shipping_total_usd': 'Total transport z fv',
            'net_total_usd': 'Sub-Total z fv.'
        }
        help_texts = {'tax_total_usd': "np. drony=7.5,ramy=2.7,silnik=2.7",
                      'shipping_total_usd': "tj. total transport / il.poz.fv",'num_items_buy': "tj. ilość sztuk na fv",
                      'unit_price_usd': "tj. cena na fakturze",
                      'net_total_usd': "tj. koszt netto na fv",'date_cost': "tj. rok-miesiąc-dzień"}
    def __init__(self, *args, **kwargs):
        super(CostsForm, self).__init__(*args, **kwargs)
        self.fields["invoice_no"].required = False
        self.fields["date_cost"].required = False
        self.fields["num_items_buy"].required = False
        self.fields["unit_price_usd"].required = False
        self.fields["tax_total_usd"].required = False
        self.fields["shipping_total_usd"].required = False
        self.fields["net_total_usd"].required = False


class CurrencyForm(forms.Form):
    CHOICES = (
            ('', ''),
            ('PLN', 'PLN'),
            ('USD', 'USD'),
        )
    select = forms.CharField(widget=forms.Select(choices=CHOICES),label='Waluta rozliczenia')

class MonthQuaterYearForm(forms.Form):
    CHOICES = (
             ('dni', 'dni'),
            ('miesiące', 'miesiące'),
            ('kwartały', 'kwartały'),
            ('lata', 'lata'),
        )
    select = forms.CharField(widget=forms.Select(choices=CHOICES), label="Forma wyświetlania")



class FixedCostsForm(ModelForm):
    class Meta:
        model = FixedCosts
        fields = (
            "name", "date", "quantity", "value")
        labels = {
            'name': 'Nazwa',
            'date': 'Data',
            'quantity': 'Ilość',
            'value': 'Wartość'
        }


class StartPartneredDeliveryForm(Form):
    def __init__(self,rows_products, *args, **kwargs):
        super(StartPartneredDeliveryForm, self).__init__(*args, **kwargs)

        choices = [((products['name'],products['name']))
                   for products in rows_products]
        self.fields['name'] = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'id': 'select-state'}),choices=choices)


class DocumentForm(forms.Form):
    myfile = forms.FileField(required=False, label="Wgraj plik csv")

