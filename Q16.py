# program to check leap year..

#Leap year: (366 days) once in a 4 years that year is known as leap year..

#conditions for leap year: 1st: the year must be purely divisble by 400 by 100.. ex: 2000, 2004 but 1996 is not so for this there is another condition.
                #2nd condition: if we divide year by 4 it must be purely divisble but if we divide by 100 it cannot be divisble.. ex: 1996

year = int(input("Enter a year:"))

if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year")

elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year")

else: 
    print(year, "is not a leap year")