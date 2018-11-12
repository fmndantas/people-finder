def DataRegister(data, numbers, i):
    try:
        if len(numbers) != 0:
            data['numbers'] += numbers
            data['temp_numbers'] += numbers
            data.update({'last_indice':i})
        else:
            pass
    except KeyError:
        data['last_indice'] = int()
        data.update({'last_indice':i})
        data['numbers'] = list()
        data['numbers'] += numbers
        data['temp_numbers'] = list()
        data.update({'temp_numbers':numbers})
    else:
        pass
