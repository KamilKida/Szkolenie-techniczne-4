from MetaClasses.UnderscoreToCamelCaseMeta import UnderscoreToCamelCaseMeta as utc
from StaticClass import BaseMethods as bs
from multiprocessing import Process, Queue
from Decorators.LogDecorator import log_decorator

@log_decorator
def getPatientDataFromDiffrentProcces(queue, exel_path):
    try:
        patient_data = bs.getPatientData(exel_path)
        queue.put(patient_data)
    except Exception as e:
        queue.put(e)
        return e

@log_decorator
def saveFilterData(filter_type, value, filtered_patients):  
    save_procces = Process(target=bs.saveFilteredPatientData(bs.getFilterPath(), filter_type, value, filtered_patients))
    save_procces.start()
    save_procces.join()

class Menu(metaclass=utc):
    def __init__(self):
        self.start_menu = "Podaj ścieżkę do pliku z danymi pacjentów, których dane chcesz przeszukać."
        self.main_menu ="Filtruj po:\n" \
                        "1. Imieniu i nazwisku. \n" \
                        "2. Nazwisku lekarza. \n" \
                        "3. Diagnozie. \n" \
                        "4. Wieku pacjenta. \n" \
                        "5. Zakończ działanie aplikacji.\n"
        self.str_value_filter_menu = "Podaj szukaną wartość."
        self.patient_list = list

    @log_decorator
    def show_start_menu(self):
        bs.clearConsole()
        print(self.start_menu)
        exel_path = input("Ścieżka do pliku: ")
        bs.clearConsole()
        print("Pobieranie danych...")
        queue = Queue()
        patientsProcces = Process(target= getPatientDataFromDiffrentProcces, args=(queue, exel_path))
        patientsProcces.start()
        patientsProcces.join()

        self.patient_list = queue.get()

    @log_decorator
    def show_main_menu(self):
        
        patient_info =""
        for i,patient in enumerate(self.patient_list, start=1):
            patient_info += f"{i}. {patient.introduceYourself()}\n"

        while True:
            bs.clearConsole()

            "\n"
            print(patient_info)
            print(self.main_menu)
            choice = input("Wybór: ")
            if choice == "1":
                    self.showNameSurnameFilterMenu()
                    continue
            elif choice == "2":
                 self.showDoctorSurnameFilterMenu()
                 continue
            elif choice == "3":
                 self.showDiagnosisFilterMenu()
                 continue
            elif choice == "4":
                 self.showAgeFilterMenu()
                 continue
            elif choice == "5":
                 break
            else:
                bs.clearConsole()
                print(f"Wprowadzona opcja '{choice}' nie istnieje na liście.\n"\
                       "Aby kontynuować, naciśnij dowolny klawisz.")
                input()
                continue
                 
                 
    
    @log_decorator
    def show_name_surname_filter_menu(self):
        bs.clearConsole()
        print(self.str_value_filter_menu)
        value = input("Wartość: ")
        strint_with_info = ""

        filtered_patients = [p for p in self.patient_list if value.lower() in p.name.lower() or value.lower() in p.surname.lower()]
        bs.clearConsole()

        for i,patient in enumerate(filtered_patients, start=1):
                strint_with_info += f"{i}. {patient.introduceYourself()}\n"
        
        while True:
            bs.clearConsole()
            print(strint_with_info)
            print("\nAby przejść dalej, naciśnij 1. \n" \
                  "Aby zapisać wynik filtrowania, naciśnij 2.")
            choice = input("Wybór: ")
            
            if choice == "1":
                break
            elif choice == "2":
                print("Zapisywanie....")
                saveFilterData("Imie i nazwisko", value, filtered_patients)
                print("Zapisano. Aby kontynuować naciśnij dowolny przycisk.")

                input()
                break
            else:
                bs.clearConsole()
                print(f"Wprowadzona opcja '{choice}' nie istnieje na liście.\n"\
                       "Aby kontynuować, naciśnij dowolny klawisz.")
                input()
                continue

    @log_decorator
    def show_doctor_surname_filter_menu(self):
        bs.clearConsole()
        print(self.str_value_filter_menu)
        value = input("Wartość: ")
        strint_with_info = ""

        filtered_patients = [p for p in self.patient_list if value.lower() in p.doctor.lower()]
        bs.clearConsole()

        for i,patient in enumerate(filtered_patients, start=1):
                strint_with_info += f"{i}. {patient.introduceYourself()}\n"
        
        while True:
            bs.clearConsole()
            print(strint_with_info)
            print("\nAby przejść dalej, naciśnij 1. \n" \
                  "Aby zapisać wynik filtrowania, naciśnij 2.")
            choice = input("Wybór: ")
            
            if choice == "1":
                break
            elif choice == "2":
                print("Zapisywanie....")
                saveFilterData("Doktor", value, filtered_patients)
                print("Zapisano. Aby kontynuować naciśnij dowolny przycisk.")

                input()
                break
            else:
                bs.clearConsole()
                print(f"Wprowadzona opcja '{choice}' nie istnieje na liście.\n"\
                       "Aby kontynuować, naciśnij dowolny klawisz.")
                input()
                continue
        
    @log_decorator
    def show_diagnosis_filter_menu(self):
        bs.clearConsole()
        print(self.str_value_filter_menu)
        value = input("Wartość: ")
        strint_with_info = ""

        filtered_patients = [p for p in self.patient_list if value.lower() in p.diagnosis.lower()]
        bs.clearConsole()

        for i,patient in enumerate(filtered_patients, start=1):
                strint_with_info += f"{i}. {patient.introduceYourself()}\n"
        
        while True:
            bs.clearConsole()
            print(strint_with_info)
            print("\nAby przejść dalej, naciśnij 1. \n" \
                  "Aby zapisać wynik filtrowania, naciśnij 2.")
            choice = input("Wybór: ")
            
            if choice == "1":
                break
            elif choice == "2":
                print("Zapisywanie....")
                saveFilterData("Diagnoza", value, filtered_patients)
                print("Zapisano. Aby kontynuować naciśnij dowolny przycisk.")

                input()
                break
            else:
                bs.clearConsole()
                print(f"Wprowadzona opcja '{choice}' nie istnieje na liście.\n"\
                       "Aby kontynuować, naciśnij dowolny klawisz.")
                input()
                continue


    @log_decorator
    def show_age_filter_menu(self):
        while True:
            bs.clearConsole()
            print("Podaj wartość zakresu wieku pacjentów (od – do).")
            try:
                age_from = int(input("Od: "))
                age_to = int(input("Do: "))

                if age_from > age_to :
                    bs.clearConsole()
                    print(f"Wartość 'Od': {age_from} musi być mniejsza niż 'Do': {age_to}. \n"
                            "Aby kontynuować, naciśnij dowolny klawisz.")
                    input()
                    continue
                else:
                     break

                
            except Exception as e:
                bs.clearConsole()
                print("Podano wartość, która nie jest liczbą. \n"
                       "Aby kontynuować, naciśnij dowolny klawisz.")
                input()
                continue



        strint_with_info = ""

        filtered_patients = [p for p in self.patient_list if p.age >= age_from and p.age <= age_to]
        bs.clearConsole()

        for i,patient in enumerate(filtered_patients, start=1):
                strint_with_info += f"{i}. {patient.introduceYourself()}\n"
        
        while True:
            bs.clearConsole()
            print(strint_with_info)
            print("\nAby przejść dalej, naciśnij 1. \n" \
                  "Aby zapisać wynik filtrowania, naciśnij 2.")
            choice = input("Wybór: ")
            
            if choice == "1":
                break
            elif choice == "2":
                print("Zapisywanie....")
                value = f"{age_from} - {age_to}"
                saveFilterData("Wiek", value, filtered_patients)
                print("Zapisano. Aby kontynuować naciśnij dowolny przycisk.")

                input()
                break
            else:
                bs.clearConsole()
                print(f"Wprowadzona opcja '{choice}' nie istnieje na liście.\n"\
                       "Aby kontynuować, naciśnij dowolny klawisz.")
                input()
                continue







