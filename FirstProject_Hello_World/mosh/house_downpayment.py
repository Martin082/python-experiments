house_price = 324572457
good_credit = True

if good_credit:
    put_down_percent = house_price * 0.10
else:
    put_down_percent = house_price * 0.20

formatted_downpayment = "{:,}".format(int(put_down_percent))

print('$' + formatted_downpayment)


