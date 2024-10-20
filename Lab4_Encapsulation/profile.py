import re


class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str) -> None or ValueError:
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None or ValueError:
        pattern = r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"

        if re.match(pattern, password):
            self.__password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
