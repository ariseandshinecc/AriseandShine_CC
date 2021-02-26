#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


from .models import Message
from django import forms

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender_name', 'phone_number', 'email', 'message']
