import pytest
from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '- name: Иванов Константин Дмитриевич\n' + \
               '  subjects:\n' + \
               '    - subject: математика\n' + \
               '      score: 91\n' + \
               '    - subject: химия\n' + \
               '      score: 100\n' + \
               '- name: Петров Петр Семенович\n' + \
               '  subjects:\n' + \
               '    - subject: русский язык\n' + \
               '      score: 87\n' + \
               '    - subject: литература\n' + \
               '      score: 78\n'

        data = {
            'Иванов Константин Дмитриевич': [
                ('математика', 91), ('химия', 100)
            ],
            'Петров Петр Семенович': [
                ('русский язык', 87), ('литература', 78)
            ]
        }

        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir('datadir').join('my_data.yaml')
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YamlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
