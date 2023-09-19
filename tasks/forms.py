from django import forms
from .models import Task  # Import your Task model


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'aircraft_registration',
            'client',
            'unit_description',
            'unit_part_number',
            'unit_serial_number',
            'reported_snag',
            'work_done',
        ]

        labels = {
            'aircraft_registration': 'Aircraft Registration',
            'client': 'Client',
            'unit_description': 'Unit Description',
            'unit_part_number': 'Unit Part Number',
            'unit_serial_number': 'Unit Serial Number',
            'reported_snag': 'Reported Snag',
            'work_done': 'Work Done',
        }

    def clean_reported_snag(self):
        reported_snag = self.cleaned_data['reported_snag']
        if not reported_snag:
            raise forms.ValidationError('Reported Snag cannot be empty.')
        return reported_snag

    def clean(self):
        cleaned_data = super().clean()
        # Perform additional custom validation if needed

        # Example: Ensure that certain fields are not empty
        for field_name in ['unit_description', 'unit_part_number', 'unit_serial_number']:
            field_value = cleaned_data.get(field_name)
            if not field_value:
                self.add_error(
                    field_name, f'{field_name.replace("_", " ").title()} cannot be empty.')
