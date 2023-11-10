import sys
import datetime

if len(sys.argv) < 3:
    print("실행 방법: python uberstudent20210773.py <filename1> <filename2>")
    sys.exit(1)
else:
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    with open(filename1, 'r') as file1:
        uberDat = [line.strip().split(",") for line in file1.readlines()]

    def get_uber_days(date_str):
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        month, day, year = map(int, date_str.split('/'))
        weekday_code = datetime.date(year, month, day).weekday()
        return days[weekday_code]

    with open(filename2, 'w') as file2:
        for entry in uberDat:
            base_number, date_str, active_vehicles, trips = entry
            day_of_date = get_uber_days(date_str)
            file2.write(f"{base_number},{day_of_date} {active_vehicles},{trips}\n")
