from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    Custom User Manager

    This class extends the `BaseUserManager` provided by Django and includes methods for creating standard users and superusers.

    Methods:
        create_user(email, username, password=None): Create a standard user with the given email, username, and password.
        create_superuser(email, username, password=None): Create a superuser with the given email, username, and password.

    """
    def create_user(self, email, username, password=None):
        """
        Create a Standard User

        This method creates a standard user with the given email, username, and password.

        Args:
            email (str): The user's email address.
            username (str): The user's username.
            password (str, optional): The user's password.

        Returns:
            User: The created user object.

        Raises:
            ValueError: If email or username is not provided.

        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):
        """
        Create a Superuser

        This method creates a superuser with the given email, username, and password.

        Args:
            email (str): The superuser's email address.
            username (str): The superuser's username.
            password (str, optional): The superuser's password.

        Returns:
            User: The created superuser object.

        """
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user