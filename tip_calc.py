bill_amount = float(input('Total bill amount? $ '))
service = str(input('Level of service? '))

tip_amount = float(bill_amount)
service_good = tip_amount * .20
service_fair = tip_amount * .15
service_bad = tip_amount * .10
service_sucks = tip_amount


if service == 'good':
  print('Tip amount: $%.2f' % (service_good)) 
  print('Total amount: $%.2f' % (bill_amount + service_good))
elif service == 'fair':
  print('Tip amount: $%.2f' % (service_fair)) 
  print('Total amount: ', (bill_amount + service_fair))
elif service == 'bad':
  print('Tip amount: $%.2f' % (service_bad))
  print('Total amount: $%.2f' % (bill_amount + service_bad))