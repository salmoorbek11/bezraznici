def trueNumberPhone(num):
    if num[0:1:] != '+7':
        return f'+7{num[1::]}'
    else:
        return num

print(trueNumberPhone(num='123456789'))