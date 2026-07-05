# question 1 
manager_son_price = lambda price, is_manager_son: price*0.8 if is_manager_son == True else price*1.17

# question 2
final_price = lambda price, discount: price-discount if 0< discount<= 100 else "wrong discount"

# question 3
full_name = lambda first_name, last_name: f" {first_name} {last_name}"

# question 4
grade_status = lambda grade: "pass" if grade > 55 else "fail"

# question 5 do again
larger = lambda num1, num2: num1 if num1> num2 else (num2 if num1 != num2  else num1)

#question 6
distance_from_10 = lambda num: 10 - num if num<10 else num-10

# question 7
item_total = lambda item: item["price"] * item ["amount"] if item["price"] == int and item ["amount"] == int else  "wrong input"

#question 8
shipping_cost_weight = lambda weight, express: 50 if express and weight >5 else 30 if express  else 25 if weight > 5 else 10

# quetion 9
access_message = lambda age, has_ticket, is_vip: "vip entrance" if is_vip else "regular entrance" if age>=18 and has_ticket else "buy ticket" if age >= 18 else "too young"

# question 10
def ticket_price (age, is_student):
    if age < 12: 
        return 20
    elif is_student:
        return 30
    else: return 50

# self learn targilim

# question 1 
numbers = [5, 2, 9, 1, 7]
new_list  = sorted (numbers)
print (new_list)

# question 2
students = [
    ("Dana", 85),
    ("Eli", 92),
    ("Noa", 78)
]
sorted_students = sorted (students, key =lambda students: students[1])
print (sorted_students)

# question 3
students = [
    {"name": "Dana", "grade": 85},
    {"name": "Eli", "grade": 92},
    {"name": "Noa", "grade": 78}
]
soted_students = sorted ( students, key = lambda students: students["grade"])
print (sorted_students)

# question 4
products = [
    {"name": "Pen", "price": 5, "amount": 10},
    {"name": "Book", "price": 40, "amount": 2},
    {"name": "Bag", "price": 80, "amount": 1}
]
sort_total_price = sorted (products, key = lambda products: products["price"]*products["amount"])
print (sort_total_price)