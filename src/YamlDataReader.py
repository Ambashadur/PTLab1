from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.student_name: str = ''
        self.current_subject: str = ''
        self.students: DataType = {}
        self._name: str = '- name: '
        self._subject: str = '    - subject: '
        self._score: str = '      score: '

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            for line in file:
                if line.startswith(self._name):
                    self.student_name = line.split(':', maxsplit=1)[1]
                    self.student_name = self.student_name.strip()
                    self.students[self.student_name] = []
                elif line.startswith(self._subject):
                    self.current_subject = line.split(':', maxsplit=1)[1]
                    self.current_subject = self.current_subject.strip()
                elif line.startswith(self._score):
                    score = line.split(':', maxsplit=1)[1].strip()
                    self.students[self.student_name].append(
                        (self.current_subject, int(score))
                    )

        return self.students
