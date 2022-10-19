from stockscrapper import scrape
from meroshare import my_stocks
import smtplib

myStocks = my_stocks()

# Takes login credentials from meroshareCredentials.txt
with open("emailCredentials.txt") as userFile:
        lines = userFile.readlines()
        try:
            sender_email = lines[0].split('=')[1].strip()
            sender_password = lines[1].split('=')[1].strip()
            recepient_email = lines[2].split('=')[1].strip()
        except Exception as e:
            print("Ignored None type",e)


msg = ''
dic_of_stocks = scrape()

for script in myStocks:
    if script in dic_of_stocks:
        closing_price = dic_of_stocks[script]['closing_price']
        diff = dic_of_stocks[script]['difference']
        msg += f'{script} \nTodays Closing Price = {closing_price} \t Todays Difference = {diff}  \n\n\n'
    else:
        msg+= f'{script} not found \n\n\n'


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sender_email,sender_password)
smtpObj.sendmail(sender_email,recepient_email,
                 f'Subject:{recepient_email}, Your todays prices.\n{msg}')
smtpObj.quit()
print('Email Sent')
