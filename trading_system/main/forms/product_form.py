from django import forms
from main.models import Product
from django.contrib.admin.widgets import AdminDateWidget
import pyexcel as pe
import datetime, time

def handle_uploaded_file(f):
    a = f.read()
    sheet = pe.get_sheet(file_type="xlsx", file_content=a)
    # then use it as usual
    sheet.name_columns_by_row(0)
    # respond with a json
    dates = sheet.dict["-1"][1:]
    opening = sheet.dict["-2"][1:]
    max_data = sheet.dict["-3"][1:]
    min_data = sheet.dict["-4"][1:]
    closing = sheet.dict["-5"][1:]
    volume = sheet.dict["-6"][1:]
    tmstp_date = [time.mktime(d.timetuple()) for d in dates]
    return (
        tmstp_date,
        opening,
        max_data,
        min_data,
        closing,
        volume
    )
        

class ProductForm(forms.ModelForm):
    date = forms.DateField(widget=AdminDateWidget(),required=False)
    opening_val = forms.FloatField(required=False)
    max_data_val = forms.FloatField(required=False)
    min_data_val = forms.FloatField(required=False)
    closing_val = forms.FloatField(required=False)
    volume_val = forms.FloatField(required=False)
    file_field = forms.FileField(required=False)

    def save(self, commit=True):
        file_field = self.cleaned_data.get('file_field', None)
        date_field = self.cleaned_data.get("date", False)
        opening_val_field = self.cleaned_data.get("opening_val", False)
        max_data_val_field = self.cleaned_data.get("max_data_val", False)
        min_data_val_field = self.cleaned_data.get("min_data_val", False)
        closing_val_field = self.cleaned_data.get("closing_val", False)
        volume_val_field = self.cleaned_data.get("volume_val", False)
        if file_field is not None:
            data = handle_uploaded_file(file_field)
            self.instance.dates = data[0]
            self.instance.opening = data[1]
            self.instance.max_data = data[2]
            self.instance.min_data = data[3]
            self.instance.closing = data[4]
            self.instance.volume = data[5]
        elif date_field and opening_val_field and max_data_val_field and min_data_val_field and closing_val_field and volume_val_field:
            t_date = time.mktime(date_field.timetuple())
            self.instance.dates.append(t_date)
            self.instance.opening.append(opening_val_field)
            self.instance.max_data.append(max_data_val_field)
            self.instance.min_data.append(min_data_val_field)
            self.instance.closing.append(closing_val_field)
            self.instance.volume.append(volume_val_field)
        return super(ProductForm, self).save(commit=commit)

    class Meta:
        model = Product
        fields = "__all__"