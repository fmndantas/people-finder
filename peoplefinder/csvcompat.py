import xlrd, xlwt

def searcher(csv_dir):
    """Used to parser spreadsheet files
    ---------------------------------------------------
    Main purpose: find the phones column in spreadsheet
    """
    pass


def getValidatedPhone(phone):
    numbers = tuple(str(x) for x in range(10))
    validPhoneLength = 10, 11
    if type(phone) == float:
        phone = str(int(phone))
    elif type(phone) == int:
        phone = str(phone)
    filtered = list(filter(lambda char: char in numbers, phone))
    if len(filtered) in validPhoneLength:
        string = ''
        for char in filtered:
            string += char
        return string
    else:
        return None


def getPhonesAndNames(csv_dir):
    # Phone form: XX9XXXXXXXX
    wb = xlrd.open_workbook(csv_dir)
    sheet = wb.sheet_by_index(0)
    names = sheet.col_values(0)
    phones = sheet.col_values(1)
    k = 0
    while k < len(phones):
        name, phone = names[k], phones[k]
        if getValidatedPhone(phone) is not None:
            phones[k] = getValidatedPhone(phone)
            names[k] = name.split(' ')[0].capitalize()
            k += 1
        else:
            phones.remove(phone)
            names.remove(name)
            assert(len(phones) == len(names))
    return names, phones


def updateCsvFile(csv_dir):
    pass