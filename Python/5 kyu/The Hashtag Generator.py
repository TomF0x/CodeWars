# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    if s=='' or len(s.replace(' ',''))>140: return False
    return '#'+''.join([a.capitalize() for a in s.split(' ') if a!=' '])
