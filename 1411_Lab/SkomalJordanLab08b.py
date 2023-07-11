# Jordan Skomal | 6/28/23


def month_convert(month_num: str):
    int_month = int(month_num)
    match int_month:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
        case _:
            return "Invalid Month"


def main():
    date = input("Please enter a date in MM/DD/YYYY format: ")
    month, day, year = date.split("/")
    month = month_convert(month)
    print(f"It is {month} {day}, {year}")


main()
