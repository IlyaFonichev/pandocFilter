from panflute import *
import sys

headers = {}


def action(element, doc):
    if type(element) == Header:
        if stringify(element) in headers.keys():
            if headers.get(stringify(element)) == element.level:
                sys.stderr.write(
                    "Повторяющиеся заголовки. Уровень: " + str(element.level) + ", текст: " + stringify(element))
        else:
            headers[stringify(element)] = element.level

    if type(element) == Str:
        if str(element.text).lower() == "bold":
            name = [Str(element.text)]
            return Strong(*name)

    if type(element) == Header:
        if element.level <= 3:
            name = [Str(stringify(element).upper())]
            return Header(*name, level=element.level)


def main(file=None):
    return run_filter(action, doc=file)


if __name__ == "__main__":
    main()
