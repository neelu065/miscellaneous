# CONVERTER: DEC / BIN / HEX


def dec2bin(d):
    # dec -> bin
    b = bin(d)
    return b


def dec2hex(d):
    # dec -> hex
    h = hex(d)
    return h


def bin2dec(b):
    # bin -> dec
    binnumb = "{0:b}".format(b)
    d = eval(binnumb)
    return d, binnumb


def bin2hex(b):
    # bin -> hex
    h = hex(b)
    return h


def hex2dec(h):
    # hex -> dec
    d = int(h)
    return d


def hex2bin(h):
    # hex -> bin
    b = bin(h)
    return b


# TESTING NUMBERS
numb_dec = 14551221
numb_bin = 0b110111100000100010110100
numb_hex = 0x000016

# CALCULATIONS
res_dec2bin = dec2bin(numb_dec)
res_dec2hex = dec2hex(numb_dec)

res_bin2dec, bin_numb = bin2dec(numb_bin)
res_bin2hex = bin2hex(numb_bin)

res_hex2dec = hex2dec(numb_hex)
res_hex2bin = hex2bin(numb_hex)

# PRINTING
print('------- DECIMAL to BIN / HEX -------\n')
print('decimal:', numb_dec, '\nbin:    ', res_dec2bin, '\nhex:    ', res_dec2hex, '\n')

print('------- BINARY to DEC / HEX -------\n')
print('binary: ', bin_numb, '\ndec:    ', numb_bin, '\nhex:    ', res_bin2hex, '\n')

print('----- HEXADECIMAL to BIN / HEX -----\n')
print('hexadec:', hex(numb_hex), '\nbin:    ', res_hex2bin, '\ndec:    ', res_hex2dec, '\n')
