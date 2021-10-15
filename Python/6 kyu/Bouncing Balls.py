# https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncing_ball(h, bounce, window):
    if h>window and h>0 and 1>bounce>0:
        result=1
        while h>window:
            h=h*bounce
            if h>window:
                result+=2
        return result
    else:
        return -1
