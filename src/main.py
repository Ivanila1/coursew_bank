from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    FILTERED_EMPTY = True
    COUNT_LAST_VALUES = 5
    data = get_data()
    data = get_filtered_data(data, filter_empty=FILTERED_EMPTY)
    data = get_last_values(data, count_last_values=COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    for row in data:
         print(row, end='\n\n')

if __name__ == '__main__':
    main()
