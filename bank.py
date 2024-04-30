import client_db as db
import datetime


cart_number,check_number = 0,0
def cash():
    global cart_number,check_number
    cash = int(input('value :'))
    if cash > db.client_d[cart_number]['balance']:
       print('not enough money!')
    else:
       db.client_d[cart_number]['balance'] -= cash
       check_number += 1
       time = datetime.datetime.now()
       status = 'Cash out'
       cash_list = [check_number,time,status,db.client_d[cart_number]['name'],cash]
       db.client_d[cart_number]['check'].append(cash_list)
def pay():
    global cart_number, check_number
    pay = int(input('value :'))
    if pay > db.client_d[cart_number]['balance']:
        print('not enough money!')
    else:
        db.client_d[cart_number]['balance'] -= pay
        check_number += 1
        time = datetime.datetime.now()
        status = 'Pay'
        pay_list = [check_number,time,status,db.client_d[cart_number]['none'],pay]
        db.client_d[cart_number]['check'].append(pay_list)

def tup_up():
    global cart_number,check_number
    tup = int(input('money :'))
    db.client_d[cart_number]['balance'] += tup
    check_number += 1
    time = datetime.datetime.now()
    status = 'Top up'
    tup_list = [check_number,time,status,db.client_d[cart_number]['name'],tup]
    db.client_d[cart_number]['check'].append(tup_list)

def balance():
    print('\n')
    print(f"{db.client_d[cart_number]['balance']}.TMT")

def check_history():
    global cart_number
    check_lst = ['Check #','Date','Status','Name','Sum']
    for i in db.client_d[cart_number]['check']:
        check_dict = dict(zip(check_lst,i))
        for k,v in check_dict.items():
            print(f'{k},{v}')
        print('\n')

def bank():
    global cart_number
    while True:
       tryes = 3
       cart_number = int(input('cart_number :'))
       if cart_number in db.client_d and bool(db.client_d[cart_number]['status']):
           while True:
                if tryes == 0:
                   db.client_d[cart_number]['status'] = False 
                   print('your cart is blocked:')
                   break
                pin_code == int(input('pin code :'))
                if pin_code == db.client_d[cart_number]['pin']:
                    while True:
                       function = int(input('1.Cash\n2.Pay\n3.Balance\n4.Check history\n5.Tup up\n6.Exit\n    :'))
                       if function >= 6:
                        break
                       def f_list():
                        f_list = [cash,pay,balance,check_history,tup_up]
                        return f_list[function-1]()
                       f_list()
                    else:
                       print('wrong pin code!')
                    tryes -= 1
                break
bank()



