class Hospital:
    def __init__(self):
        self.status_dict = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
        self.patients = [1] * 200  # Инициализация базы пациентов

    def execute_command(self, command, patient_id=None):
        if command == "стоп":
            print("Сеанс завершён.")
            return True

        if command in ["узнать статус пациента", "get status"]:
            self.get_status(patient_id)
        elif command in ["повысить статус пациента", "status up"]:
            self.status_up(patient_id)
        elif command in ["понизить статус пациента", "status down"]:
            self.status_down(patient_id)
        elif command in ["выписать пациента", "discharge"]:
            self.discharge_patient(patient_id)
        elif command in ["рассчитать статистику", "calculate statistics"]:
            self.calculate_statistics()
        else:
            print("Неизвестная команда! Попробуйте ещё раз")

    def get_status(self, patient_id=None):
        if not patient_id:
            patient_id = input("Введите ID пациента: ")
        valid, result = self.validate_patient_id(patient_id)
        if valid:
            status_code = self.patients[result - 1]
            print(f"Статус пациента: \"{self.status_dict[status_code]}\"")
        else:
            print(result)

    def status_up(self,  patient_id=None):
        if not patient_id:
            patient_id = input("Введите ID пациента: ")
        valid, result = self.validate_patient_id(patient_id)
        if valid:
            if self.patients[result - 1] < 3:
                self.patients[result - 1] += 1
                print(f"Новый статус пациента: \"{self.status_dict[self.patients[result - 1]]}\"")
            else:
                confirm = input("Желаете этого клиента выписать? (да/нет): ").lower()
                if confirm == 'да':
                    del self.patients[result - 1]
                    print("Пациент выписан из больницы")
                else:
                    print(f"Пациент остался в статусе \"{self.status_dict[3]}\"")
        else:
            print(result)

    def status_down(self,  patient_id=None):
        if not patient_id:
            patient_id = input("Введите ID пациента: ")
        valid, result = self.validate_patient_id(patient_id)
        if valid:
            if self.patients[result - 1] > 0:
                self.patients[result - 1] -= 1
                print(f"Новый статус пациента: \"{self.status_dict[self.patients[result - 1]]}\"")
            else:
                print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
        else:
            print(result)

    def discharge_patient(self,  patient_id=None):
        if not patient_id:
            patient_id = input("Введите ID пациента: ")
        valid, result = self.validate_patient_id(patient_id)
        if valid:
            del self.patients[result - 1]
            print("Пациент выписан из больницы")
        else:
            print(result)

    def calculate_statistics(self):
        total_patients = len(self.patients)
        status_counts = {0: 0, 1: 0, 2: 0, 3: 0}
        for status_code in self.patients:
            status_counts[status_code] += 1

        print(f"В больнице на данный момент находится {total_patients} чел., из них:")
        for status_code, count in status_counts.items():
            if count > 0:
                print(f"\t- в статусе \"{self.status_dict[status_code]}\": {count} чел.")

    def validate_patient_id(self, patient_id):
        try:
            patient_id = int(patient_id)
            if 1 <= patient_id <= len(self.patients):
                return True, patient_id
            elif patient_id > len(self.patients):
                return False, "Ошибка. В больнице нет пациента с таким ID"
            elif patient_id <= 0:
                return False, "Ошибка. ID пациента должно быть числом (целым, положительным)"
        except ValueError:
            return False, "Ошибка. ID пациента должно быть числом (целым, положительным)"
        return False, "Ошибка. ID пациента должно быть числом (целым, положительным)"

# Инициализация hospital
# для запуска работы hospital расскоментировать строки
#------------------------------------------
# hospital = Hospital()
# while not hospital.execute_command(input("Введите команду: ").lower()):
#    pass
#------------------------------------------


#   Вызов методов класса. Передается команда из списка доступных и *args.
#   Если в методе требуется параметр *args - ID пациента, и он пустой, то
#   в методе через input запрашивается ID пациента
    
#Пример использования
#hospital.execute_command("понизить статус пациента", 200)
#hospital.execute_command("status up", 5)
#hospital.execute_command("status down", 3)
#hospital.execute_command("discharge", 4)
#hospital.execute_command("рассчитать статистику")
