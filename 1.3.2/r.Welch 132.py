def add_tip(total, tip_percent):
    '''Return the total amount including tip
    '''
    tip = tip_percent*total
    return total + tip

def hyp(leg1, leg2): 
    hyp = (leg1**2 + leg2**2)**0.5
    return hyp 
def mean(a, b, c) :
    mean = (a + b + c) /3.0
    return mean

def perimeter(base, height) :
    perimeter = 2*base + 2*height
    return perimeter
    