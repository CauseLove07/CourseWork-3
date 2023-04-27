from src.utils import load_json, get_filtered_data, get_last_five, get_exchanged_data

def main():

    file = 'operations.json'

    data = load_json(file)
    filtered_data = get_filtered_data(data)
    get_five = get_last_five(filtered_data)
    complited = get_exchanged_data(get_five)

    for i in complited:
        print(i)
        print()

main()