# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    ct=0
    a = sorted([i for i in source_array if i%2==1])
    for i in range(len(source_array)):
        if source_array[i] in a:
            source_array[i]=a[ct]
            ct+=1
    return source_array
