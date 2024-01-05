import unittest
from unittest.mock import patch
from class_Hospital import Hospital

class TestStatusUp(unittest.TestCase):
    @patch('builtins.input', return_value='да')
    def test_status_up_confirm_yes(self, mock_input):
        # Создание экземпляра класса Hospital
        hospital = Hospital()

        # Вместо ввода пользователя, мы используем фиктивный ввод 'да' из mock
        #hospital.status_up(patient_id='1')
        hospital.execute_command("status up", 1)
        hospital.execute_command("status up", 1)
        hospital.execute_command("status up", 1)

        # Проверка, что статус пациента был изменен
        self.assertEqual(hospital.patients[0], 1)  # Измените это в соответствии с ожидаемым поведением

    # Добавьте другие тесты по необходимости

if __name__ == '__main__':
    unittest.main()
