from src.Types import DataType
from src.CalcBestStudent import CalcBestStudent
import pytest


class TestCalcBestStudent:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, str]:
        data: DataType = {
            'Абрамов Петр Сергеевич':
            [
                ('математика', 89),
                ('русский язык', 76),
                ('программирование', 100)
            ],
            'Петров Игорь Владимирович':
            [
                ('математика', 90),
                ('русский язык', 90),
                ('программирование', 90),
                ('литература', 90),
            ],
            'Минаков Дмитрий Александрович':
            [
                ('математика', 90),
                ('русский язык', 90),
                ('программирование', 90),
                ('литература', 90),
            ]
        }

        best_student: str = 'Петров Игорь Владимирович'

        return data, best_student

    def test_init_calc_best_student(
            self, input_data: tuple[DataType, str]) -> None:
        calc_best_student = CalcBestStudent(input_data[0])
        assert input_data[0] == calc_best_student.data

    def test_calc(self, input_data: tuple[DataType, str]) -> None:
        student = CalcBestStudent(input_data[0]).calc()
        assert student == input_data[1]
