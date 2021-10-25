import os
from calendar import monthrange

year = 2020
month = 11
day = 2

day_steps = [1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 3, 2, 1, 4, 1, 1, 2, 10, 1, 1, 1, 1, 3, 2, 2, 3, 4, 24, 1, 1, 1, 1, 4, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 3, 2, 2, 3, 4, 24, 1, 1, 1, 1, 3, 2, 5, 1, 1, 12, 1, 1, 1, 1, 7, 7, 10, 1, 1, 1, 1, 3, 2, 2, 3, 4, 10, 1, 1, 1, 1, 3, 2, 5, 1, 1, 1, 1, 10, 1, 1, 2, 3, 2, 2, 3, 2, 1, 1, 10, 1, 1, 1, 1, 3, 2, 2, 3, 4, 0]

# Prepare yourself to wait, this is very slow
for i in day_steps:
    days_in_month = monthrange(year, month)[1]
    if day > days_in_month:
        if month == 12:
            year += 1
        month = (month % 12) + 1
        day = (day % days_in_month)
    f = open("HireMePlease.txt", "a")
    f.write("HireMePlease\n")
    f.close()
    print("commiting date: \"%d-%02d-%02dT00:00:00\"" % (year, month, day))
    date_string = "%d-%02d-%02dT10:00:00" % (year, month, day)
    os.environ["GIT_COMMITTER_DATE"] = date_string
    os.environ["GIT_AUTHOR_DATE"] = date_string
    os.system("git add .\\HireMePlease.txt")
    os.system("git commit -m \"HireMePlease\"")
    day += i