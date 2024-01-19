from django.contrib.auth.base_user import BaseUserManager


class SuperUser(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
