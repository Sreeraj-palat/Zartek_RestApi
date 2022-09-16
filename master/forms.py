from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from .models import UserRoles, SubAdmin, Customer

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        fields = ("name", )


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("name", )


    def save(self, commit=True):
        user = super().save(commit=False)

        # Set a username as email to avoid integrity error
        user.username = user.email
        name_list = user.name.split()
        user.first_name = ' '.join(name_list[0:len(name_list) - 1]) if len(name_list) > 1 else user.name
        user.last_name = name_list[-1] if len(name_list) > 1 else ""
        user.save()

        if "role" in self.data and self.data["role"]:
            role = int(self.data["role"])
            if role == UserRoles.SUPERADMIN:
                user.is_superuser = True
            elif role == UserRoles.SUBADMIN:
                SubAdmin.objects.create(user=user)
            elif role == UserRoles.CUSTOMER:
                Customer.objects.create(user=user)

        return user