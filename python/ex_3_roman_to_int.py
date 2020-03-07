def write_roman(num):
    ''' function to return integer to roman'''
    digits = {1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 : "L",
              40 : "XL", 10 : "X", 9 : "IX", 5 : "V", 4 : "IV", 1 : "I"}
    rom_dig = ''
    for r in digits:
        #print(num, r)
        x, y = divmod(num, r)
        yield digits[r] * x
        num -= (r * x)
        if num <= 0:
            break
        

if __name__ == "__main__":
    num = 65432
    print("Roman numeral is:"+"".join(write_roman(num)), end=" ")
