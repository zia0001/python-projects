"""
patient_name = "John Smith"
age= 50
is_new = True

"""
#------------------------------------------------------------------
"""
# name = input('what is your name? ')
# favourite_color = input('what is your favourite color ')
# print(name + ' likes ' + favourite_color)
"""
#------------------------------------------------------------------
                    # convert user weight in pounds to kgs
"""
weight_lbs = (input('what is yout weight in pounds: '))
weight_kgs = round(int(weight_lbs) * 0.453592,2)
print('your weight in kgs = ' +str(weight_kgs) + ' kgs' )

                    # OR
try:

    weight = int(input('what is yout weight in pounds: '))
    weight_kgs = round(weight * 0.453592, 2)

    print(f'your weight is {weight_kgs} kgs')
          
except ValueError:
    print('please enter a valid number for weight')

    """
# -------------------------------------------------------------------