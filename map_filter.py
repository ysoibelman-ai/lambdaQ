from functools import reduce
# #Map Questions
# # # question 1
# # numbers = [3,7,10,15]
# # new_list = map ( lambda numbers: numbers+10, numbers)
# # print (list(new_list))

# # # question 2
# # prices = [100,50,200,80]
# # new_price_list = map(lambda prices: prices*1.17, prices)
# # print (list(new_list))

# # # question 3
# # words = ["cat", "elephant", "dog", "python"]
# # new_words = map (lambda words: len(words, words))
# # print (list (new_words))

# # # question 4
# # names ="yaakov", "ephraim", "yishai"
# # new_names = map (lambda names: names.upper(), names)
# # print (list (new_names))

# # # question 5
# # users = ["Noa", "Adam", "Lior", "Tamar"]
# # new_users = map (lambda users: "hello " + users, users)
# # print (list(new_users))

# # # question 6
# # meters = [1.5, 2, 0.75, 3.2]
# # new_meters = map (lambda meters: meters*100, meters)
# # print (list(new_meters))

# # # question 7 
# # grades = [95, 40, 67, 88, 52]
# # new_grades = map(lambda grades : "pass" if grades >=60 else "fail", grades)
# # print (list (new_grades))

# # # question 8
# # products = [
# #     {"name": "Bread", "price": 8},
# #     {"name": "Milk", "price": 6},
# #     {"name": "Eggs", "price": 15}
# # ]

# # new_products = map (lambda products: f" {products["name"]}+ costs +{products["price"]}" , products)
# # print (list(new_products))

# # # question 9
# # players = [
# #     {"name": "Dana", "score": 70},
# #     {"name": "Yoni", "score": 85},
# #     {"name": "Rami", "score": 40}
# # ]


# # new_players = map (lambda players: {"name": players["name"], "score" : players["score"] +5 }  , players)
# # print (list(new_players))

# # # question 10 
# # orders = [
# #     {"id": 1, "item": "Book", "amount": 3, "price": 40},
# #     {"id": 2, "item": "Pen", "amount": 10, "price": 5},
# #     {"id": 3, "item": "Bag", "amount": 1, "price": 120}
# # ]

# # new_list = map (lambda orders : f"Order {orders ["id"]}: {orders["item"]} total is {orders["amount"]*orders["price"]}" , orders)
# # print (list (new_list))

# # Qestions Filter

# # question 1
# numbers = [4, 7, 10, 13, 18, 21]
# new_list = filter (lambda numbers : True if numbers % 2==0 else False, numbers)

# # question 2
# grades = [100, 55, 70, 40, 88, 59]
# new_grades = filter (lambda grades : True if grades >= 60 else False, grades )

# # question 3
# words = ["dog", "elephant", "cat", "computer", "sun"]
# new_words = filter (lambda words: True if len(words) <=3 else False, words)

# #question 4
# names = ["Adam", "Dana", "Amit", "Noa", "Alon"]
# A_words = filter (lambda names: True if names[0] == "A" else False)

# # question 5
# numbers = [-5, 3, 0, 12, -2, 8]
# pos_num = filter (lambda numbers: numbers if numbers >0 else False, numbers)

# #question 6
# products = [
#     {"name": "Book", "price": 40},
#     {"name": "Bag", "price": 120},
#     {"name": "Pen", "price": 5},
#     {"name": "Shirt", "price": 60}
# ]

# cheap_prodc = filter (lambda products: True if products["price"] < 50 else False, products)

# # question 7 
# users = [
#     {"name": "Dana", "active": True},
#     {"name": "Ron", "active": False},
#     {"name": "Maya", "active": True},
#     {"name": "Gil", "active": False}
# ]

# active_users = filter (lambda useres: True if users["acitve"] else False, users)

# # question 8
# passwords = ["abc", "hello123", "Python2026", "pass", "GoodPass99"]
# strons_pass = filter (lambda passwrods: True if len (passwords) >= 8 else False ,passwords)

# # question 9
# tasks = [
#     {"title": "Clean room", "done": True, "priority": 2},
#     {"title": "Study Python", "done": False, "priority": 1},
#     {"title": "Play game", "done": False, "priority": 5},
#     {"title": "Send email", "done": True, "priority": 1}
# ]

# new_tasks = filter (lambda tasks: True if tasks["done"] == False and tasks["proprity"] <3 else False, tasks)

# # qeustion 10
# # students = [
# #     {"name": "Noa", "grade": 90, "attendance": 95},
# #     {"name": "Dan", "grade": 55, "attendance": 100},
# #     {"name": "Rina", "grade": 80, "attendance": 70},
# #     {"name": "Eli", "grade": 75, "attendance": 85}
# # ]

# # certif_students = filter (lambda students: True if students["grade"] >=70 and students["attendance"]>=80 else False, students)

# # Reduce Questions
#  # question 1
# numbers = [5, 10, 20, 15]
# total = reduce( lambda x,y : x+y, numbers)
# # question 2
# numbers = [2, 3, 4, 5]
# total = reduce (lambda x,y: x*y, numbers)
# #question 3
# words = ["cat", "elephant", "dog", "computer"]
# long_word = reduce (lambda x, y: x if len(x) >=len(y) else y,words)
# # question 4
# words = ["Python", "is", "very", "useful"]
# sentence = reduce (lambda x, y: x+ " "+ y, words)
#question 5
students = [
    {"name": "Dana", "grade": 85},
    {"name": "Ron", "grade": 92},
    {"name": "Maya", "grade": 78},
    {"name": "Gil", "grade": 95}
]
highest_grade = reduce (lambda x, y: x if x["grade"] > y["grade"] else y ,students )
print (highest_grade)
