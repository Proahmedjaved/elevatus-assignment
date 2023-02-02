from pydantic import EmailStr

class LowerCaseEmailStr(EmailStr):

    @classmethod
    def validate(cls, value):
        return super().validate(value.lower())