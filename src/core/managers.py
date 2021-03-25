from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, data):

        user = self.model(
            full_name=data['full_name'],
            email=self.normalize_email(data['email']),
            phone=data['phone'],
            address=data.get('address'),
            city=data.get('city'),
            state=data.get('state'),
            country=data.get('country'),
            pincode=data['pincode'],
        )
        user.set_password(data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, **data):
        user = self.create_user(data)
        user.is_admin = True
        user.save(using=self._db)
        return user
