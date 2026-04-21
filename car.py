car = input('drive or not?')
if car not in ['yes', 'Yes', 'YES', 'no', 'No', 'NO']:
    print ('Oh no')
    raise SystemExit

age = int(input('How old are you?'))
if car in ['yes', 'Yes', 'YES']:
    if age >= 18:
        print('Good')
    else:
        print('Police')
elif car in ['no', 'No', 'NO']:
    print('OKAY')