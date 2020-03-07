import random



def lottry_gam():

    ''' Function will return random 10 balls from the list of 50 balls'''

    lot = [i for i in range(1, 51)]

    lim = 10

    re_li = []

    while lim != 0:

        sel = random.choice(lot)

        if sel in re_li:

            continue

        re_li.append(sel)

        lim -= 1

    re_li.sort() # sorting the list for ascending order

  

    return re_li

 

 

 

 

if __name__ == "__main__":

    res_val = lottry_gam()

    print(res_val)
