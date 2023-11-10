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
        # 날짜를 파싱하고 요일 코드로 변환
        month, day, year = map(int, date_str.split('/'))
        weekday_code = datetime.date(year, month, day).weekday()
        return days[weekday_code]

    with open(filename2, 'w') as file2:
        for entry in uberDat:
            base_number, date_str, active_vehicles, trips = entry
            # get_uber_days 함수를 사용하여 날짜를 계산
            day_of_week = get_uber_days(date_str)
            # 출력 형식 변경 및 파일에 쓰기
            file2.write(f"{base_number},{day_of_week} {active_vehicles},{trips}\n")
