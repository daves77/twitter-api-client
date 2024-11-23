from twitter.account import Account

account = Account(cookies='cookies.json')

print(account.session)
print('running')
account.tweet('hi been a long minute')
print('done')