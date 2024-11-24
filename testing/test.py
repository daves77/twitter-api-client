from twitter.account import Account
import time
import random

import json

# Open and read the JSON file
with open('accounts.json', 'r') as file:
    accounts = json.load(file)




print(len(accounts))
session = Account(cookies='cookies.json')

for account in accounts[100:]:
    print("now following",  account['name'])
    session.follow(account['sourceRefId'])
    time.sleep(random.randint(1, 10))

# print(account.session)
# print('running')
# # account.follow(44196397)
# print('done')