star=int(input('Enter the start name:'))
end=int(input('Enter end file #:'))
bond=[]
angle=[]
stretch=[]
atoa=[]
ou=[]
tor=[]
van=[]
for xo in range(star,end+1):
    file=str(xo)
    myfile=open(file + '.log','r')
    temp=[]
    for num1 in myfile:
        temp.append(num1)
    templist=list(range(-7,0))
    A=[]
    for num2 in templist:
        a=(temp[num2])
        A.append(a)
    tt=['1','2','3','4','5','6','7','8','9','0','.','-']
    num7=[]
    for num3 in range(1,8):
        num4=list(A[num3-1])
        num6=[]
        for num5 in num4:
            if num5 in tt:
                num6.append(num5)
            else:
                pass
        if num3!=7:
            if num6[1]=="-" and num6[0]=='-':
                num6.pop(0)
        num7.append(round(float(''.join(num6)),4))
    bond.append(num7[0])
    angle.append(num7[1])
    stretch.append((num7[2]))
    atoa.append(num7[3])
    ou.append(num7[4])
    tor.append(num7[5])
    van.append(num7[6])
my=open('./van.txt','w')
#my.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\t \n'.format('Bond Streching', 'Angle Bending', 'Strech-bend', 'Angle-Angle', 'Out of plane', 'Torsional angle', 'Van der waals'))
for num8 in range(1,end+2-star):
    if num8 in range(30,691,30):
        my.write('{}\t \n'.format(van[num8-1]))
    else:
        my.write('{}\t '.format(van[num8-1]))
my.close()
