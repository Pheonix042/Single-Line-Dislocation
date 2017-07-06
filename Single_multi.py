h=int(input('Horizontal hexagon(even#) as if perfect lattice:'))
v=int(input('Vertical hexagon(even#) as if perfect lattice:'))
vd=int(input('Position of pentagone in hexagon number from bottom(Should always be odd#):'))
for xxx in range(5,35):
    # Single line dislocation
    
    hd=xxx
    
    atomno=[]
    vv=list(range(1,v+2))
    for li in vv:
        if li==1:
            num1=2+h*2
        elif li<vd:
            num1=h*2+atomno[li-2]
        elif li==vd:
            num1=h*2+atomno[li-2]+1
        else:
            num1=h*2+atomno[li-2]+2
        atomno.append(num1)
    SrNo=[]
    Xco=[]
    Yco=[]
    for num2 in vv:
    #line-1 calculation
        if num2==1: 
            templist=list(range(1,atomno[0]+1))
            for num3 in templist:
                if num3==1:#atom-no-1
                    x1=1.212435
                    y1=2.1
                else:
                    num4=hd*2+2
                    num5=hd*2+3
                    if num3!=num4 and num3!=num5:
                        x1=1.212435+x2
                    else:
                        x1=x2+1.212435*2
                    if num3%2==0:
                        y1=0.7
                    else:
                        y1=0
                if num3==1:
                    x2=0
                else:
                    x2=x1
                SrNo.append(num3)    
                Xco.append(round(x1,6))
                Yco.append(round(y1,6))
#lines above affected heptagone            
        elif num2>vd: 
            templist=list(range(atomno[num2-2]+1,atomno[num2-1]+1))
            if num2%2==0:
                for num6 in templist:
                    if num6==templist[0]:
                        x1=Xco[num6-2]
                    else:
                        x1=Xco[num6-2]-1.212435
                    if num6%2==0:
                        y1=(num2-1)*2.1
                    else:
                        y1=(num2-1)*2.1+0.7
                    SrNo.append(num6)
                    Xco.append(round(x1,6))
                    Yco.append(round(y1,6))
            else:
                for num7 in templist:
                    if num7==templist[0]:
                        x1=Xco[num7-2]
                    else:
                        x1=Xco[num7-2]+1.212435
                    if num7%2==0:
                        y1=(num2-1)*2.1
                    else:
                        y1=(num2-1)*2.1+0.7
                    SrNo.append(num7)
                    Xco.append(round(x1,6))
                    Yco.append(round(y1,6))
# lines below the affected heptagone line                
        elif num2<vd:
            templist=list(range(atomno[num2-2]+1,atomno[num2-1]+1))
        #print(templist)
            if num2%2==1:
                for num8 in templist:
                    rad1=templist[0]+(hd-1)*2+1
                    rad2=templist[0]+(hd-1)*2+2
                    if num8==templist[0]:
                        x1=Xco[num8-2]
                    elif num8<rad1:
                        x1=Xco[num8-2]+1.212435
                    elif num8==rad1:
                        x1=Xco[num8-2]+1.212435*2
                    elif num8==rad2:
                        x1=Xco[num8-2]+1.212435*2
                    else:
                        x1=Xco[num8-2]+1.212435
                    if num8%2==0:
                        y1=(num2-1)*2.1+0.7
                    else:
                        y1=(num2-1)*2.1
                    SrNo.append(num8)
                    Xco.append(round(x1,6))
                    Yco.append(round(y1,6))
            else:
                for num8 in templist:
                    rad1=atomno[num2-1]-(hd-1)*2-1
                    rad2=atomno[num2-1]-(hd-1)*2
                    if num8==templist[0]:
                        x1=Xco[num8-2]
                    elif num8<rad1:
                        x1=Xco[num8-2]-1.212435
                    elif num8==rad1:
                        x1=Xco[num8-2]-1.212435*2
                    elif num8==rad2:
                        x1=Xco[num8-2]-1.212435*2
                    else:
                        x1=Xco[num8-2]-1.212435
                    if num8%2==0:
                        y1=(num2-1)*2.1+0.7
                    else:
                        y1=(num2-1)*2.1
                    SrNo.append(num8)
                    Xco.append(round(x1,6))
                    Yco.append(round(y1,6))
#affected heptagone line
        else:
            templist=list(range(atomno[num2-2]+1,atomno[num2-1]+1))
        #print(templist)
            rad3=atomno[num2-2]+1+hd*2
        #print(rad3)
            for num9 in templist:
                if num9==templist[0]:
                    x1=Xco[num9-2]
                elif num9<rad3:
                    x1=Xco[num9-2]+1.212435
                elif num9==rad3:
                    x1=Xco[num9-2]+2*1.212435
                else:
                    x1=Xco[num9-2]+1.212435
                if num9==rad3:
                    y1=num2*2.1-1.4
                elif num9==rad3-1:
                    y1=num2*2.1-1.4
                elif num9%2==0:
                    if num9<rad3:
                        y1=num2*2.1-1.4
                    else:
                        y1=(num2-1)*2.1
                else:
                    if num9<rad3:
                        y1=(num2-1)*2.1
                    else:
                        y1=(num2-1)*2.1+0.7
                SrNo.append(num9)
                Xco.append(round(x1,6))
                Yco.append(round(y1,6))
    genlist=list(range(1,atomno[v]+1))
#for num10 in genlist:
#    print(SrNo[num10-1], Xco[num10-1], Yco[num10-1])
# Loop far neighbour assigning
    R=[]
    M=[]
    L=[]
    for line in vv:
# Neighbor of line-1    
        if line==1:
            neigh=list(range(1,atomno[0]+1))
        #print(neigh)
            for atom in neigh:
                if atom==1:
                    r=atomno[line]
                    m=2
                    l=""
                elif atom%2==0:
                    if atom==2:
                        r=3
                        m=1
                        l=""
                    else:
                        r=atom+1
                        l=atom-1
                        if atom!=atomno[line-1]:
                            m=atomno[line-1]*2-atom+1
                        else:
                            m=""
                else:
                    r=atom+1
                    l=atom-1
                    m=""
                R.append(r)
                M.append(m)
                L.append(l)
# neighbor of all the lines below the affected heptagone
        elif (line<(vd)):
            neigh=list(range(atomno[line-2]+1,1+atomno[line-1]))
            for atom in neigh:
            # line 2 neighbor
                if line==2:
                    a1=atomno[0]+1
                    a2=atomno[1]
                    if atom==a1:
                        r=""
                        m=atom-1
                        l=atom+1
                    elif atom==a2:
                        r=atom-1
                        m=atom+1
                        l=1
                    else:
                        if atom%2==0:
                            m=(atomno[line-1]-atom)*2+1+atom
                        else:
                            m=atom-(atom-(atomno[line-2]+1))*2-1
                        r=atom-1
                        l=atom+1
            # odd line neighbour
                elif line%2==1:
                    a3=atomno[line-2]+1
                    a4=atomno[line-1]
                    if atom==a3:
                        r=atom+1
                        m=atom-1
                        l=""
                    elif atom==a4:
                        r=""
                        m=atom+1
                        l=atom-1
                    else:
                        r=atom+1
                        l=atom-1
                        if atom%2==0:
                            m=atom+(atomno[line-1]-atom)*2+1
                        else:
                            m=atom-(atom-atomno[line-2]-1)*2-1
                else:
                    a5=atomno[line-2]+1
                    a6=atomno[line-1]
                    if atom==a5:
                        r=""
                        m=atom-1
                        l=atom+1
                    elif atom==a6:
                        r=atom-1
                        m=atom+1
                        l=""
                    else:
                        r=atom-1
                        l=atom+1
                        if line!=(vd-1):
                            if atom%2==0:
                                m=atom+(atomno[line-1]-atom)*2+1
                            else:
                                m=atom-(atom-atomno[line-2]-1)*2-1
                        else:
                            if atom%2==1:
                                m=atom-(atom-atomno[line-2]-1)*2-1
                            else:
                                rad1=atomno[line-1]-hd*2
                            #print(rad1)
                                if (atom<=rad1):
                                    m=atom+(atomno[line-1]-atom)*2+2
                                else:
                                    m=atom+(atomno[line-1]-atom)*2+1
            #print('R',r, 'M',m, 'L',l)
                R.append(r)
                M.append(m)
                L.append(l)
# neighbor of all the lines above the heptagone
        elif (line>vd):
           neigh=list(range(atomno[line-2]+1,atomno[line-1]+1))
           for atom in neigh:
           # for all the line not last
                if line!=v+1:
                    if line%2==0:
                        a7=atomno[line-2]+1
                        a8=atomno[line-1]
                        if atom==a7:
                            r=""
                            m=atom-1
                            l=atom+1
                        elif atom==a8:
                            r=atom-1
                            m=atom+1
                            l=""
                        else:
                            if line!=vd+1:
                                if atom%2==0:
                                    m=atom-(atom-(atomno[line-2]+1))*2-1
                                else:
                                    m=atom+(atomno[line-1]-atom)*2+1
                            else:
                                rad2=atomno[line-1]-2*hd
                                if atom>rad2:
                                    if atom%2==0:
                                        m=atom-(atom-(atomno[line-2]+1))*2
                                    else:
                                        m=atom+(atomno[line-1]-atom)*2+1
                                else:
                                    if atom%2==0:
                                        m=atom-(atom-(atomno[line-2]+1))*2-1
                                    else:
                                        m=atom+(atomno[line-1]-atom)*2+1
                            r=atom-1
                            l=atom+1
                    else:
                        a9=atomno[line-2]+1
                        a10=atomno[line-1]
                        if atom==a9:
                            r=atom+1
                            m=atom-1
                            l=""
                        elif atom==a10:
                            r=""
                            l=atom-1
                            m=atom+1
                        else:
                            if atom%2==0:
                                m=atom-(atom-atomno[line-2]-1)*2-1
                            else:
                                m=atom+(atomno[line-1]-atom)*2+1
                            r=atom+1
                            l=atom-1
                else:
                    if atom%2==0:
                        m=atom-(atom-atomno[line-2]-1)*2-1
                    else:
                        m=""
                    if ((atom+1)<=atomno[v]):
                        r=atom+1
                        rad3=atomno[v-1]+1
                        if atom!=rad3:
                            l=atom-1
                        else:
                            l=""
                    else:
                        r=""
                        l=atom-1
                R.append(r)
                M.append(m)
                L.append(l)
# Neighbor of the affected line having heptagone
        else:
            neigh=list(range(atomno[line-2]+1,atomno[line-1]+1))
            #print(neigh)
            for atom in neigh:
                a11=atomno[line-2]+1
                a12=atomno[line-1]
                if atom==a11:
                    r=atom+1
                    l=""
                    m=atom-1
                elif atom==a12:
                    r=""
                    m=atom+1
                    l=atom-1
                else:
                    rad1=1+atomno[vd-2]+hd*2
                #print(rad1)
                    r=atom+1
                    l=atom-1
                    if (atom<rad1):
                        if atom%2==0:
                            m=atom+(atomno[line-1]-atom)*2+2
                        else:
                            m=atom-(atom-atomno[line-2]-1)*2-1
                    else:
                        if atom%2==1:
                            m=atom+(atomno[line-1]-atom)*2+1
                        else:
                            m=atom-(atom-atomno[line-2]-1)*2
                R.append(r)
                M.append(m)
                L.append(l)
    for mn in genlist:
        if M[mn-1]=="":
            M[mn-1]=L[mn-1]
            L[mn-1]=""
        else:
            pass
        if R[mn-1]=="":
            R[mn-1]=M[mn-1]
            M[mn-1]=L[mn-1]
            L[mn-1]=""
        else:
            pass
    Atom_no=atomno[v]
    xxxx=str(xxx+656)
    myfile=open(xxxx + '.xyz','w')
    myfile.write('{}\t \n'.format(Atom_no))
    for nn in genlist:
        myfile.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t \n'.format(SrNo[nn-1], 'C', Xco[nn-1], Yco[nn-1], 0, 2, R[nn-1], M[nn-1], L[nn-1]))
    myfile.close()
