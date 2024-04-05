from django import forms
from .models import Student


def phone_number_validator(value):
    if value:
        if not value.isnumeric():
            raise forms.ValidationError("This field can only contain digits.")

    return value


class StudentForm(forms.ModelForm):
    # rollNumber = forms.IntegerField()
    # name = forms.CharField(required=False, label="username", label_suffix="     ")
    name = forms.CharField(required=False, help_text="It should be only alphabet not digit.", label='username', label_suffix=" ")
    phoneNumber = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Student
        # fields = ('')
        # exclude = ('phoneNumber',)
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("This field can't contain digits.")
        return name

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        print("photo data==> ", photo)
        print("photo length==> ", len(photo))
        # Check if a file was provided
        if photo is None:
            return photo

        # file length
        if len(photo) > 10 * 1024 * 1024:  # 10 MB in bytes
            print("error occured on file size")

            raise forms.ValidationError("The file size should not exceed 10MB.")

        # Check file extension
        allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
        ext = photo.name.split('.')[-1].lower()
        print('ext=> ', ext)
        if ext not in allowed_extensions:
            print("error occured on file extension")
            raise forms.ValidationError("File type is not supported. Only JPG, JPEG, PNG, and GIF are allowed.")

        return photo

    # def save(self, commit=True):
    #     data = self.cleaned_data()
    #     return obj


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phoneNumber = forms.CharField()
    url = forms.URLField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        data = super().clean()
        print("data in form clean method==> ", data)
        name = data.get('name')
        errors = {}
        if name and not name.isalpha():
            errors['name'] = "This field can't contain digits"
            # raise forms.ValidationError()

        phone_number = data.get('phoneNumber')
        if phone_number and not phone_number.isnumeric():
            errors['phoneNumber'] = "This field can contain only digits."

        if errors:
            raise forms.ValidationError(errors)
        return data

