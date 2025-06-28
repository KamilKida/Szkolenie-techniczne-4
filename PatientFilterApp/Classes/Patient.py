from MetaClasses.UnderscoreToCamelCaseMeta import UnderscoreToCamelCaseMeta as utc


class Patient(metaclass=utc):
    def __init__(self, name, surname, age, doctor, diagnosis):
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.doctor = doctor
        self.diagnosis = diagnosis
    
    def to_dict(self):
        from Decorators.LogDecorator import log_decorator
        @log_decorator
        def inner_of_to_dict():
            return {
                "Imię": self.name,
                "Nazwisko": self.surname,
                "Wiek": self.age,
                "Lekarz": self.doctor,
                "Diagnoza": self.diagnosis
            }
        return inner_of_to_dict()

    def introduce_yourself(self):
        from Decorators.LogDecorator import log_decorator
        @log_decorator
        def inner_of_introduce_yourself():
            return (f"{self.name} {self.surname}, Wiek: {self.age}, Doktor: {self.doctor}, Diagnoza: {self.diagnosis}")
        return inner_of_introduce_yourself()