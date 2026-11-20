from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,first_name,last_name,**extra_fields):
        print(extra_fields)
        if not email:
            raise ValueError("You must provide email")
        if not password:
            raise ValueError("You must set password")
        if not first_name:
            raise ValueError("You must provide first_name")
        if not last_name:
            raise ValueError("You must provide first_name")

        email=self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,password,first_name,last_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)


        return self.create_user(email,password,first_name,last_name,**extra_fields)