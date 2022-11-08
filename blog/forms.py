from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model=Firm_Comment
        fields= '__all__'


class CommentFrForm(forms.ModelForm):
    class Meta:
        model=Frp_Comment
        fields= '__all__'

class CommentCrForm(forms.ModelForm):
    class Meta:
        model=Crack_Comment
        fields= '__all__'

class CommentTrForm(forms.ModelForm):
    class Meta:
        model=Torent_Comment
        fields= '__all__'

class DeviceForm(forms.ModelForm):
    class Meta:
        model= Device
        fields= '__all__'


class FrpForm(forms.ModelForm):
    class Meta:
        model= Frp_bypass
        fields= '__all__'

class FirmForm(forms.ModelForm):
    class Meta:
        model= Firmwares
        fields= '__all__'


class CrackForm(forms.ModelForm):
    class Meta:
        model= Cracked_tools
        fields= '__all__'


class TForm(forms.ModelForm):
    class Meta:
        model= VideoTorent
        fields= '__all__'