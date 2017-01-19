__author__ = 'David'


def to_binary(number):
    '''

    :param number: decimal number
    :return: binary number
    '''
    s = ''
    while number > 0:
        s += str(number % 2)
        number /= 2
    print 'Your binary: ' + s[::-1]


def to_decimal(number):
    '''

    :param number: number to convert to decimal
    :return: decimal number
    '''
    if is_binary(number):
        dec = 0
        binary_string = str(number)
        binary_string = binary_string[::-1]
        for x in range(len(binary_string)):
            dec += int(binary_string[x]) * 2 ** int(x)
        return dec
    else:
        print 'Not a valid binary'


def is_binary(number):
    '''

    :param number: get the input from user
    :return: if binary return True else False
    '''
    n = str(number)
    for x in range(len(n)):
        if int(n[x]) >= 2:
            return False
    return True

if __name__ == '__main__':
    print "------Converting Program"
    print "1. Decimal to Binary"
    print "2. Binary to Decimal"
    user_selection = int(raw_input("What to you want to convert (1 or 2):"))
    if user_selection == 1:
        dec_to_binary = int(raw_input("Input Decimal number to convert please:"))
        to_binary(dec_to_binary)
    elif user_selection == 2:
        bi_to_dec = int(raw_input("Input Binary number to convert please:"))
        print 'Your decimal: ' + str(to_decimal(bi_to_dec))
    else:
        print "1 or 2 please"