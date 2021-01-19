# written by Vinicius Queiroz
import math

emails = ['luffy@email.com','zoro@email.com',
          'sanji@email.com','nami@email.com',
          'chopper@email.com', 'usopp@email.com']

# define shopping list
shoppinglist = [['apple', 1, 100]]

# verify if list or items are not null or empty
if len(emails) <= 0 or len(shoppinglist) <= 0:
    print("please, enter at least one value in each list and run again!")
    exit()

for e in emails:
    if len(e) <= 0:
        emails.remove(e)

for i in shoppinglist:
    if len(i) != 3:
        shoppinglist.remove(i)

# calculate total shopping list price

def calculate(item):
    return item[1] * item[2]


total = math.ceil(sum(map(calculate, shoppinglist)))

# discover unit value and the rest
unit_value = math.floor(total / len(emails))
rest = total - (unit_value * len(emails))
value_by_email = []

for i in range(len(emails)):
    if rest > 0:
        value_by_email.append(unit_value + 1)
        rest -= 1
    else:
        value_by_email.append(unit_value)


## create dictionary
dic = dict(zip(emails, value_by_email))

for d in dic:
    print(d, ',', dic[d])