import telegram

chii_token = '123456789:ABCDEDFGHIJKLMNOPQRST'
chii = telegram.Bot(token = chii_token)
updates = chii .getUpdates()
for u in updates:
    print(u.message)
import telegram


