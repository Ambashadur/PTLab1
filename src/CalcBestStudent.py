from Types import DataType


class CalcBestStudent:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.best_student: str = 'No best student'

    def calc(self) -> str:
        for fio in self.data:
            subject_ninty_count = 0

            for subject in self.data[fio]:
                if subject[1] == 90:
                    subject_ninty_count += 1
                else:
                    break

            if subject_ninty_count == len(self.data[fio]):
                return fio
            
        return self.best_student
