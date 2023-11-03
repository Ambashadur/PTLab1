import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path",
                        type=str, required=True, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    file_extension = path.split('.')[-1]

    reader = None

    if file_extension == 'txt':
        reader = TextDataReader()
    elif file_extension == 'yaml':
        reader = YamlDataReader()

    if reader is None:
        print('Unsopperted file extension!')

    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)


if __name__ == "__main__":
    main()
