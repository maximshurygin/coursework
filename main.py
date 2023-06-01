import json


def print_recent_executed_operations(json_file):
    with open(json_file) as file:
        data = json.load(file)

    # Фильтруем операции с состоянием "EXECUTED"
    executed_operations = [operation for operation in data if 'state' in operation and operation['state'] == 'EXECUTED']

    # Сортируем операции по дате в убывающем порядке
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

    # Выводим список последних 5 операций
    for operation in sorted_operations[:5]:
        operation_date = operation['date'][:10]
        formatted_date = operation_date[8:] + '.' + operation_date[5:7] + '.' + operation_date[:4]
        operation_description = operation['description']
        operation_from = operation.get('from')
        operation_to = operation['to']
        operation_amount = operation['operationAmount']['amount']
        operation_currency = operation['operationAmount']['currency']['name']

        masked_card_number = ''
        if operation_from:
            card_number = operation_from.split(' ')[-1]
            masked_card_number = card_number[:4] + ' ' + card_number[5:7] + 'X' * 2 + ' ' + 'X' * 4 + ' ' + card_number[-4:]

        masked_account_number = '**' + operation_to[-4:]

        print(formatted_date, operation_description)
        if masked_card_number:
            print(masked_card_number, '-> Счет', masked_account_number)
        else:
            print('Unknown -> Счет', masked_account_number)
        print(operation_amount, operation_currency)
        print()


json_file = 'operations.json'
print_recent_executed_operations(json_file)
