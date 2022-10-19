# Mail My Stocks

This script scrapes the information of stocks you own through MeroShare and scrapes the live information of those stocks from (http://nepalstock.com/todaysprice) and mails the information of the stocks from desired email to desired email.

This script can be scheduled with Windows Scheduler or in Linux to automatically run the script everyday after the market closes or as required.


# How to use the script?


## 1. Install the required dependencies
```
pip install -r requirements.txt 
or 
python3 -m pip install -r requirements.txt 
```


## 2. Edit the meroshareCredentials.txt file and add your meroshare credentials as mentioned there
```
username=MeroshareUsername
password=MerosharePassword
dpNumber=dpNumber
```

## 3. Edit the emailCredentials.txt file and add your email credentials as mentioned there
```
sender_email=email
sender_password =App-password
recipient_email=email
```
Note: Google no longer accepts password directly through SMTPLIB as it is considered as insecure. But you can use App-Passwords to access gmail. Learn how to do this through (https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjWgY74huz6AhXqt2MGHcWgA3cQFnoECA0QAQ&url=https%3A%2F%2Fsupport.google.com%2Faccounts%2Fanswer%2F185833%3Fhl%3Den&usg=AOvVaw2qwXmKRTjsa0k-q38HqJIX)

## 4. After adding credentials and email credentials run the following command from parent directory
```
python ./my_stocks.py
or
python3 ./my_stocks.py
```

I don't consider this project complete yet. I'll add more features as I get ideas on what to add.