name = input('Enter you name: ')
weight = float(input('Enter your weight in kgs: '))
height = float(input('Enter your height in cms: '))
bmi = (weight/(height**2))
print ('your bmi is ', bmi)
if bmi>0:
        if (bmi<16):
            print (name + ', you are severely underweight. You should be more cautious about your health more.')
        elif (bmi<18.5):
            print (name + ', you are underweight.')
        elif (bmi<=24.9):
            print (name + ', you are normal weight. Congrats!')
        elif (bmi<34.9):
            print (name + ', you are overweight. You should start caring more about what you eat')
        elif (bmi<39.9):
            print (name + ', you are obese. You should check a doctor to have a better quailty life.')
        else:
           print (name + 'you are morbidly obese. You should get an appoinment for a dietician for sure, for your health.')
else:
        print ('Enter valid input.')
input('press any key to close the window')