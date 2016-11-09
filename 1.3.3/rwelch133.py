def age_limit_output(age):
    
    AGE_LIMIT=13
    if age< AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
            print(age, 'is old enough.')
            print('Minimum age is', AGE_LIMIT)
def report_grade(percent):
    PERCENT_MASTERY= 80
    if percent>= PERCENT_MASTERY:
        print ('A grade of (percent) percent indicates mastery.')
        print ('Keep up the good work!')
    else:
            print (' A grade of (percent) does not indicate mastery.')
            print (' Seek extra practice or help.')
def vowel(letter):
    vowel = ('aeiouAEIOU')
    if letter in vowel:
        return True
    else:
        return False
        
def letter_in_word(guess, word):
    if guess in word:
        return True
    else:
        return False
def hint(color, secret):
    if color in secret:
        print ('The color', color, 'Is in the secret sequence of colors')
    else:
            print ('The color' , color, 'IS NOT in the secret sequence of colors')
        