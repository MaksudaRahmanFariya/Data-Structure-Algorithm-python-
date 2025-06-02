from collections import deque
class categoryNode:
    def __init__(self, name):
        self.name = name
        self.childern = []
    def insert(self, child):
        self.childern.append(child)
    def display(self, level = 0):
        print(" "* level + self.name)
        for child in self.childern:
            child.display(level+1)
root = categoryNode("Electronics")
phones = categoryNode("Phones")
phones.insert("Android")
phones.insert("Iphone")
phones.insert("Nokia")
phones.insert("Bada")
phones.insert("Windows Phone")
phones.insert("ASUS")
laptops = categoryNode("Laptop")
laptops.insert("notebooks")
laptops.insert("ultrabooks")
laptops.insert("Chromebooks")
laptops.insert("MacBooks")
laptops.insert("Gaming laptops")
televisions = categoryNode("Television")
televisions.insert("LED")
televisions.insert("OLD")
televisions.insert("QLED")
televisions.insert("LCD")
televisions.insert("plasma")
root.insert(phones)
root.insert(laptops)
root.insert(televisions)

class Solution:
    users = { }
    profile = { }
    def user_management(self, users):
        def login(user,password):
            if user in users and users[user] == password:
                print("You are valid")
            # session['username'] = username
            #return redirect(url_for('index'))
            else:
                print("Your email or password is invalid")
        def sign():
            print("Email: ")
            email = input()
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(pattern, email):
                email = email
                print("Name: ")
                Name = input()
                print("Password: ")
                password = input()
                profile['Name'] = password
                users['email'] = password
            else:
                print("Invalid")
    def product_management(self):

    def  order_management(self):
    def payment(self):
    def shipping(self):
    def recommendation(self):








