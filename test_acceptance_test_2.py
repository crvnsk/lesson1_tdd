import subprocess
import pytest
import allure
from class_Hospital import Hospital

def read_expected_output(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

@allure.feature("=== Приёмочный тест № 2 (неизвестная команда) ===")
def test_acceptance_test(capsys):
    hospital = Hospital()
    expected_outputs = read_expected_output('expected_output_test_2.txt')

    def run_and_assert(command, *args, expected_output_index):
        print(f"\n {command}")
        captured_before = capsys.readouterr()
        hospital.execute_command(command, *args)
        captured_after = capsys.readouterr()
        actual_output = captured_after.out.strip()
        
        expected_output_cleaned = expected_outputs[expected_output_index].replace('\t', '').replace(' ', '')
        actual_output_cleaned = actual_output.replace('\t', '').replace(' ', '')
        
        assert actual_output_cleaned.startswith(expected_output_cleaned)

    # Шаг 1:
    run_and_assert("выписать всех пациентов", expected_output_index=0)
    # Шаг 2:
    run_and_assert("стоп", expected_output_index=1)