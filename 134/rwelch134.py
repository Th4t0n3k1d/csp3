def food_id(food):
    fruits = ['apple', 'banana','orange']
    citrus = ['orange']
    starchy = [ 'banana', 'potato']
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruite'
                if food in starchy:
                    return 'Starchy, NOT Fruit'
                        else 
                return 'NOT Starchy, NOT Fruit'
                   