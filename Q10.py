#NUMERIC TYPES: INT & FLOAT

users=150
conversion_arte = 0.043

revenue_per_user = 18.99 
total_revenue = users* revenue_per_user

print(total_revenue)
print(type(total_revenue))

#STRINGS TEXTUAL DATA
 
country = "India"
segment = "Enterprises"
user_id = "aditya12"

label = f"{country}--{segment}--{user_id}"
print(label)

#COLLECTIONS: LISTS & DICTIONARIES..

daily_signups = [110,123,345]

user_record= {
    "id":102,
    "country": "India",
     "is_active": True
}

#BOOLEAN VALUES

is_paying_one = True
has_overdue_invoice = False
if is_paying_one and not has_overdue_invoice:
    print("Eligible for discount")

#CODE SNIPPET COMPUTING SIMPLE FUNNEL METRICS..

visits=12_400
signups=500
purchase=300

signup_rate=signups/visits 
purchase_rate=purchase/visits

is_healthy = signup_rate> 0.03 and purchase_rate > 0.01
print(is_healthy)

#TAKING USER INPUT..

name=input("Enter your name:")
print("Your name is",name)

#OUTPUT: PRINTABLE REDABLE CODE
#THE LAST THING WHICH WE GET IS KNOWN AS OUTPUT.

