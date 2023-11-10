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
    
    uberDataDict = {}
    key_days =[]
    for entry in uberDat:
        base_number, date_str, active_vehicles, trips = entry
        day_of_week = get_uber_days(date_str)
        key = f"{base_number},{day_of_week}"

        if key in uberDataDict:
            uberDataDict[key][1] += int(active_vehicles)
            uberDataDict[key][2] += int(trips)  
        else:
            uberDataDict[key] = [base_number, int(active_vehicles), int(trips)]
        
        for i in key.split(',')[1].split():
            key_days.append(i)

    with open(filename2, 'w') as file2:
        for key, data in uberDataDict.items():
            file2.write(f"{data[0]},{key_days.pop(0)} {data[1]},{data[2]}\n")
