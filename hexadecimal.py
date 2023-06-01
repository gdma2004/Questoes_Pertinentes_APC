cor, r, g, b = input().split(',')




r_hexa = hex(int(r)).replace('0x','')
if r_hexa == '0':
    r_hexa = '00'
else:
    r_hexa = r_hexa.upper()



g_hexa = hex(int(g)).replace('0x','')
if g_hexa == '0':
    g_hexa = '00'
else:
    g_hexa = g_hexa.upper()



b_hexa = hex(int(b)).replace('0x','')
if b_hexa == '0':
    b_hexa = '00'
else:
    b_hexa = b_hexa.upper()





print(f'{cor} #{r_hexa}{g_hexa}{b_hexa}')





