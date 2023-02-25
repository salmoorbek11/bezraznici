def get_case(string):
    if 65 <= max([ord(i) for i in string]) <= 90:
        return 'Верхний'
    elif 97 <= min([ord(i) for i in string]) <= 122:
        return 'Нижний'
    else:
        return 'Смешанный'

if __name__ == '__main__':
    string = 'bekA'
    print(get_case(string))