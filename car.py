car = input('drive or not?')
if car != 'yes' and car != 'Yes' and car != 'YES' and car != 'No' and car != 'NO' and car != 'no':
    print ('Oh no')
    raise SystemExit
    
age = input('How old are you?')
age = int (age)
if car == 'yes' or car == 'Yes' or car == 'YES':
    if age >= 18:
        print('Good')
    else:
        print('Police')
elif car == 'No' or car == 'NO' or car == 'no':
    print('OKAY')