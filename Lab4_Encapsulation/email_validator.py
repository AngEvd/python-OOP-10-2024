class EmailValidator:
    def __init__(self, min_length: int, mails: list[str], domains: list[str]) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        name, account = email.split("@")
        mail, domain = account.split(".")
        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)
