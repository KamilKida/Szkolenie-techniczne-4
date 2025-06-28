from MetaClasses.UnderscoreToCamelCaseMeta import UnderscoreToCamelCaseMeta as utc
from Classes.Patient import Patient as p

import datetime
import os
import pandas as pd

class BaseMethods(metaclass = utc):
    log_path = "logs/"
    filter_path = "filter/"

    @classmethod
    def get_log_path(cls):
        return cls.log_path
    
    @classmethod
    def get_filter_path(cls):
        return cls.filter_path
    
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def get_patient_data(exel_path):
        
        def inner_of_get_patient_data():
            data = pd.read_excel(exel_path)

            patients = [ 
                p(row["Imię"], row["Nazwisko"], row["Wiek"], row["Lekarz"], row["Diagnoza"])
                            for _, row in data.iterrows()
                            ]
            return patients
        return inner_of_get_patient_data()
    
    @staticmethod
    def save_filtered_patient_data(filter_path,filter_type, filter_value,filtered_patients):
        from Decorators.LogDecorator import log_decorator
        @log_decorator
        def innef_of_save_filtered_patient_data():
            try:
                if not os.path.exists(filter_path):
                    os.makedirs(filter_path)

                now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_path = f"{filter_path}/{now} {filter_type}_{filter_value}.xlsx"

                df = pd.DataFrame([patient.toDict() for patient in filtered_patients])
                df.to_excel(file_path, index=False)
            except Exception as e:
                print(f"Wystąpił błąd podczas zapisu pliku. {e}")

        return innef_of_save_filtered_patient_data()