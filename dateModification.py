from datetime import timedelta
from datetime import date

beginDateString = date.today()
print(beginDateString)
days = int(input())

endDate = beginDateString+timedelta(days)
print(endDate)