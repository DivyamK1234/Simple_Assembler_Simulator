import sys



A={"add":"10000", "sub":"10001", "mul":"10110", "xor":"11010", "or":"11011", "and":"11100"}
B={"rs":"11000", "ls":"11001"}
C={"div":"10111", "not":"11101", "cmp":"11110"}
D={"ld":"10100","st":"10101"}
E={"jmp":"11111", "jlt":"01100", "jgt":"01101","je":"01111"}
F={"hlt":"01010"}
R={"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4":"100", "R5":"101", "R6":"110", "FLAGS":"111"}
var={}
label={}


keyvar=var.keys()
keyA=A.keys()
keyB=B.keys()
keyC=C.keys()
keyD=D.keys()
keyE=E.keys()
keyF=F.keys()
keyR=R.keys()




def isfloat(s):
    for i in s:
        if i==".":
            return True
    return False

def correctbinary(s):
    s=s[1::]
    s=int(s)
    if s<=255 and s>=0:

    
        return True
    else:
        return False
def Binary(n):
    n=int(n)
    output=""
    
    
    while(n!=0):
        digit=n%2
        output=str(digit)+output
        n=n//2
    length=len(output)
    output="0"*(8-length)+output
    

    return output


list_of_lines=sys.stdin.readlines()




r=-1
while list_of_lines[r]=='\n':
    list_of_lines.pop(r)
    



l1=[]
noerror=True
notypoerror=True
noundefinedvar=True
noundefinedlabel=True
noillegalflag=True
noillegalimm=True
nomisuselabel=True
nomisusevar=True
novarnotdeclaredatbegining=True
noabsenthlt=True
hltlast=True
nogenearal=True
errorlist=[]
line=[]
linenumber=1
count=0
number_of_vars=0

variablelines=[]
linen2=1
for j in list_of_lines:
    y=j.split()
    if y!=[]:
        if str(y[0])!="var":
            count+=1
            linen2+=1
        else:
            number_of_vars+=1
            variablelines.append(linen2)
            linen2+=1
v=0
for i in range(number_of_vars):
    instruction=list_of_lines[i].split()
    if instruction==[]:
        pass
    else:
        if instruction[0]!="var":
            noerror=False
            novarnotdeclaredatbegining=False
            errorlist.append("variable not decalred at begining")
            line.append(variablelines[v])
            v+=1
        else:
            v+=1
list_of_labels=[]
c1=(-1)*number_of_vars
for item in list_of_lines:
    x=item.split()
    if x==[]:
        pass
    else:

        if x[0][-1]==":":
            s=x[0][:-1:]
            label[s]=c1
        
        
        c1+=1

keylabel=label.keys()

        

            
h1=0
for i in list_of_lines:
    x=i.split()
    
    if x!=[]:
        if x[0]=='hlt':
            h1+=1
        if x[0][-1]==":" and x[1::]!=[]:
            if x[1]=="hlt":
                h1+=1
if h1>1:
    noerror=False
    hltlast=False
else:
    if 'hlt\n' not in list_of_lines:
        noerror=False
        noabsenthlt=False
        l2=list_of_lines[-1].split()
        if l2[0][-1]==":"and l2[1::]!=[] and l2[1]=="hlt":
            noerror=True
            noabsenthlt=True
    else:
        if list_of_lines[-1]!='hlt\n' or list_of_lines.count('hlt\n')>1:
            noerror=False
            hltlast=False
    
    
counter=0  
for i in list_of_lines:
    
    x=i.split()
    
    
    
    if x==[]:
        continue
    else:
        if (x[0] not in keyA ) and (x[0] not in keyB) and (x[0] not in keyC) and (x[0] not in keyD) and (x[0] not in keyE )and (x[0] not in  keyF) and (x[0]!="mov") and (x[0]!="var") and (x[0][-1]!=":"):
            if x[0] not in label:
                noerror=False
                noundefinedlabel=False
                notypoerror=False
                errorlist.append("Typo and undefined error")
                line.append(linenumber)
            
        if x[0] in keyA:
            if len(x)!=4:
                noerror=False
                notypoerror=False
                errorlist.append("typo error")
                line.append(linenumber)
            else:
                if x[1] not in keyR:
                    noerror=False
                    notypoerror=False
                    errorlist.append("typo error")
                    line.append(linenumber)

                else:
                    if x[1]=="FLAGS":
                        noerror=False
                        noillegalflag=False
                        errorlist.append("Illegal flag error")
                        line.append(linenumber)
                    if x[2] not in keyR:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typo error")
                        line.append(linenumber)

                    else:
                        if x[2]=="FLAGS":
                            noerror=False
                            noillegalflag=False
                            errorlist.append("Illegal flag")
                            line.append(linenumber)

                        if x[3] not in keyR:
                            noerror=False
                            notypoerror=False
                            errorlist.append("Typo error")
                            line.append(linenumber)
                        else:
                            if x[3]=="FLAGS":
                                noerror=False
                                noillegalflag=False
                                errorlist.append("Illegal flag")
                                line.append(linenumber)
            if noerror==True:
                output=f"{A.get(x[0])}00{R.get(x[1])}{R.get(x[2])}{R.get(x[3])}"
                l1.append(output)
 
        elif x[0] in keyB:
            if len(x)!=3:
                noerror=False
                notypoerror=False
                errorlist.append("typoerror")
                line.append(linenumber)
            else:
                if x[1] not in keyR:
                    noerror=False
                    notypoerror=False
                    errorlist.append("typoerror")
                    line.append(linenumber)
                else:
                    if x[1]=="FLAGS":
                        noerror=False
                        noillegalflag=False
                        errorlist.append("Illegal flags")
                        line.append(linenumber)
                    if isfloat(x[2]):
                        noerror=False
                        errorlist.append("incorrect immediate value")
                        line.append(linenumber)
                    else:
                        if(not(correctbinary(x[2]))):
                            noerror=False
                            noillegalimm=False
                            errorlist.append("immediate value more than 8 bits")
                            line.append(linenumber)
            if noerror==True:
                s=str(x[2])
                s=s[1::]
                s=int(s)
                output=f"{B.get(x[0])}{R.get(x[1])}{Binary(s)}"
                l1.append(output)

        elif x[0]=="mov":
            if len(x)!=3:
                noerror=False
                notypoerror=False
                errorlist.append("typoerror")
                line.append(linenumber)
            else:
                if x[1] not in keyR:
                    noerror=False
                    notypoerror=False
                    errorlist.append("typoerror")
                    line.append(linenumber)

                else:
                    
                    if (True):
                        
                        if x[2][0]=="$":
                            if isfloat(x[2]) or not(correctbinary(x[2])):
                                noerror=False
                                noillegalimm=False
                                errorlist.append("incorrect immediate value")
                                line.append(linenumber)
                        elif(x[2] in keyR ):
                            if x[2]=="FLAGS":
                                noerror=False
                                errorlist.append("illegal flag used")
                                line.append(linenumber)
                        else:
                            noerror=False
                            errorlist.append("typo error")
                            line.append(linenumber)
            if noerror==True:
                if x[2] in keyR:
                    output=f"1001100000{R.get(x[1])}{R.get(x[2])}"
                    l1.append(output)
                else:
                    s=x[2]
                    s=s[1::]
                    s=int(s)
                    output=f"10010{R.get(x[1])}{Binary(s)}"
                    l1.append(output)

        elif x[0] in keyC:
            if len(x)!=3:
                if x[1] not in keyR:
                    noerror=False
                    notypoerror=False
                    errorlist.append("typoerror")
                    line.append(linenumber)
                else:
                    if x[1]=="FLAGS":
                        noerror=False
                        noillegalflag=False
                        errorlist.append("Illegal flags")
                        line.append(linenumber)
                    if x[2] not in keyR:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typo error")
                        line.append(linenumber)
                    else:
                        if x[2]=="FLAGS":
                            noerror=False
                            noillegalflag=False
                            errorlist.append("Illegal flags")
                            line.append(linenumber)
            if noerror:
                output=f"{C.get(x[0])}00000{R.get(x[1])}{R.get(x[2])}"
                l1.append(output)

        elif x[0] in keyD:
            if len(x)!=3:
                noerror=False
                notypoerror=False
                errorlist.append("typoerror")
                line.append(linenumber)
            else:
                if x[1] not in keyR:
                    noerror=False
                    notypoerror=False
                    errorlist.append("typoerror")
                    line.append(linenumber)
                else:
                    if x[1]=="FLAGS":
                        noerror=False
                        noillegalflag=False
                        errorlist.append("illegal flags")
                        line.append(linenumber)

                        
                    if x[2] not in keyvar:
                        if x[2] in keylabel:
                            noerror=False
                            nomisuselabel=False
                            errorlist.append("misuse of label")
                            line.append(linenumber)
                    

                        else:
                            noerror=False
                            noundefinedvar=False
                            errorlist.append("undefined variable used")
                            line.append(linenumber)
            if noerror==True:
                output=f"{D.get(x[0])}{R.get(x[1])}{Binary(var.get(x[2]))}"
                l1.append(output)
                
        elif x[0] in keyE:
            if len(x)!=2:
                noerror=False
                notypoerror=False
                errorlist.append("typo error")
                line.append(linenumber)
            else:
                
                
                if x[1] not in keylabel:
                    
                    if x[1] in keyvar:
                            noerror=False
                            nomisusevar=False
                            errorlist.append("misuse of variables")
                            line.append(linenumber)
                    else:
                        
                        noerror=False
                        noundefinedlabel=False
                        errorlist.append("undefined label")
                        line.append(linenumber)
            if noerror==True:
                
                output=f"{E.get(x[0])}000{Binary(label.get(x[1]))}"
                l1.append(output)
                line.append(linenumber)

        elif x[0] in keyF:
            if len(x)!=1:
                noerror=False
                notypoerror=False
                errorlist.append("typo error")
                line.append(linenumber)
            else:
                output=f"{F.get(x[0])}00000000000"
                l1.append(output)

        elif x[0]=="var":
            if len(x)!=2:
                noerror=False
                notypoerror=False
                errorlist.append("typo error")
                line.append(linenumber)
            elif x[1] in keyA or x[1] in keyB or x[1] in keyC or x[1] in keyD or x[1] in keyD or x[1] in keyE or x[1] in keyF or x[1]=="mov" or x[1]=="var":
                noerror=False
                errorlist.append("opperands used as variable")
                line.append(linenumber)
            elif x[1] in keyR:
                noerror=False
                errorlist.append("register  used as variables")
                line.append(linenumber)



            else:
                var[x[1]]=count+len(keyvar)

        

        elif x[0][-1]==":":
            
            x=i.split()
            list_of_labels.append(x[0])
            if list_of_labels.count(x[0])>1:
                noerror=False
                errorlist.append("same label used again")
                line.append(linenumber)
            
            elif x[1::]==[]:
                noerror=False
                nogenearal=False
                errorlist.append("general syntax error")
                line.append(linenumber)
            

            else:
                
                if (x[1] not in keyA ) and (x[1] not in keyB) and (x[1] not in keyC) and (x[1] not in keyD) and (x[1] not in keyE ) and (x[1] not in  keyF) and (x[1]!="mov") and (x[1]!="var") and (x[1][-1]!=":"):
                    if x[1] not in label:
                        noerror=False
                        noundefinedlabel=False
                        notypoerror=False
                        errorlist.append("typo error")
                        line.append(linenumber)
                    
                elif x[1] in keyA:
                    if len(x[1::])!=4:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typoerror")
                        line.append(linenumber)
                        
                    else:
                        if x[2] not in keyR:
                            noerror=False
                            notypoerror=False
                            errorlist.append("typo error")
                            line.append(linenumber)

                        else:
                            if x[2]=="FLAGS":
                                noerror=False
                                noillegalflag=False
                                errorlist.append("illegal flag")
                                line.append(linenumber)
                            if x[3] not in keyR:
                                noerror=False
                                notypoerror=False
                                errorlist.append("typoerror")
                                line.append(linenumber)

                            else:
                                if x[3]=="FLAGS":
                                    noerror=False
                                    noillegalflag=False
                                    errorlist.append("illegal flag")
                                    line.append(linenumber)

                                if x[4] not in keyR:
                                    noerror=False
                                    notypoerror=False
                                    errorlist.append("typoerror")
                                    line.append(linenumber)
                                else:
                                    if x[4]=="FLAGS":
                                        noerror=False
                                        noillegalflag=False
                                        errorlist.append("illegal flag")
                                        line.append(linenumber)
                    if noerror==True:
                        output=f"{A.get(x[1])}00{R.get(x[2])}{R.get(x[3])}{R.get(x[4])}"
                        l1.append(output)
                        
        
                elif x[1] in keyB:
                    if len(x[1::])!=3:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typoerror")
                        line.append(linenumber)
                    else:
                        if x[2] not in keyR:
                            noerror=False
                            notypoerror=False
                            errorlist.append("typoerror")
                            line.append(linenumber)
                        else:
                            if x[2]=="FLAGS":
                                noerror=False
                                noillegalflag=False
                                errorlist.append("illegal flag")
                                line.append(linenumber)
                            if(isfloat(x[3])):
                                noerror=False
                                errorlist.append("incorrect immediate value")
                                line.append(linenumber)
                            else:
                                if(not(correctbinary(x[3]))):
                                    noerror=False
                                    noillegalimm=False
                                    errorlist.append("immediate value more than 8")
                                    line.append(linenumber)
                    if noerror==True:
                        s=str(x[3])
                        s=s[1::]
                        s=int(s)
                        output=f"{B.get(x[1])}{R.get(x[2])}{Binary(s)}"
                        l1.append(output)

                elif x[1]=="mov":
                    if len(x[1::])!=3:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typoerror")
                        line.append(linenumber)
                    else:
                        if x[2] not in keyR:
                            noerror=False
                            notypoerror=False
                            errorlist.append("typoerror")
                            line.append(linenumber)

                        else:
                            
                            if (True):
                        
                                if x[3][0]=="$":
                                    if isfloat(x[3]) or not(correctbinary(x[3])):
                                        noerror=False
                                        noillegalimm=False
                                        errorlist.append("incorrect immediate value")
                                        line.append(linenumber)
                                elif(x[3] in keyR ):
                                    if x[3]=="FLAGS":
                                        noerror=False
                                        errorlist.append("illegal flag used")
                                        line.append(linenumber)
                                else:
                                    noerror=False
                                    errorlist.append("typo error")
                                    line.append(linenumber)
                    if noerror==True:
                        if x[3] in keyR:
                            output=f"1001100000{R.get(x[2])}{R.get(x[3])}"
                            l1.append(output)
                        else:
                            s=x[3]
                            s=s[1::]
                            s=int(s)
                            output=f"10010{R.get(x[2])}{Binary(s)}"
                            l1.append(output)

                elif x[1] in keyC:
                    if len(x[1::])!=3:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typo error")
                        line.append(linenumber)
                    else:
                        if x[2] not in keyR:
                            noerror=False
                            notypoerror=False
                            errorlist.append("typoerror")
                            line.append(linenumber)
                        else:
                            if x[2]=="FLAGS":
                                noerror=False
                                noillegalflag=False
                                errorlist.append("illegal flag")
                                line.append(linenumber)
                            if x[3] not in keyR:
                                noerror=False
                                notypoerror=False
                                errorlist.append("typoerror")
                                line.append(linenumber)
                            else:
                                if x[3]=="FLAGS":
                                    noerror=False
                                    noillegalflag=False
                                    errorlist.append("illegal flag")
                                    line.append(linenumber)
                    if noerror:
                        output=f"{C.get(x[1])}00000{R.get(x[2])}{R.get(x[3])}"
                        l1.append(output)

                elif x[1] in keyD:
                    if len(x[1::])!=3:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typoerror")
                        line.append(linenumber)
                    else:

                        if x[2] not in keyR:
                            noerror=False
                            notypoerror=False
                            errorlist.append("typoerror")
                            line.append(linenumber)
                        else:
                            if x[2]=="FLAGS":
                                noerror=False
                                noillegalflag=False
                                errorlist.append("illegal flag")
                                line.append(linenumber)
                            if x[3] not in keyvar:
                                if x[3] in label:
                                    noerror=False
                                    nomisuselabel=False
                                    errorlist.append("misuse label")
                                    line.append(linenumber)
                                else:
                                    noerror=False
                                    noundefinedvar=False
                                    errorlist.append("undefined variable")
                                    line.append(linenumber)
                    if noerror==True:
                        output=f"{D.get(x[1])}{R.get(x[2])}{Binary(var.get(x[3]))}"
                        l1.append(output)
                        
                elif x[1] in keyE:
                    if len(x[1::])!=2:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typoerror")
                        line.append(linenumber)
                    else:
                        if x[2] not in keyvar:
                            if x[2] in label:
                                    noerror=False
                                    nomisuselabel=False
                                    errorlist.append("misuse of label")
                                    line.append(linenumber)
                            else:
                                noerror=False
                                noundefinedvar=False
                                errorlist.append("undefined var")
                                line.append(linenumber)
                    if noerror==True:
                        output=f"{E.get(x[1])}000{Binary(label.get(x[2]))}"
                        l1.append(output)

                elif x[1] in keyF:
                    if len(x[1::])!=1:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typo error")
                        line.append(linenumber)
                    if noerror:

                        output=f"{F.get(x[1])}00000000000"
                        l1.append(output)

                elif x[1]=="var":
                    if len(x[1::])!=2:
                        noerror=False
                        notypoerror=False
                        errorlist.append("typo error")
                        line.append(linenumber)
                    elif x[1] in keyA or x[1] in keyB or x[1] in keyC or x[1] in keyD or x[1] in keyD or x[1] in keyE or x[1] in keyF or x[1]=="mov" or x[1]=="var":
                        noerror=False
                        errorlist.append("opperands used as variable")
                        line.append(linenumber)
                    elif x[1] in keyR:
                        noerror=False
                        errorlist.append("register  used as variables")
                        line.append(linenumber)
                    else:
                        var[x[2]]=count+len(keyvar)
                elif x[1][-1]==":":
                    noerror=False
                    nomisuselabel=False
                    errorlist.append("misuse of label")
                    line.append(linenumber)
                    
        if(x[0])!="var":
            counter+=1
    linenumber+=1


if noerror==True:
    for i in l1:
        print(i)
        
else:
    j=0
    if noabsenthlt==False:
        print("absent hlt")
    if hltlast==False:
        print("Hlt not at last")
    for i in errorlist:
        print(f"{i} in line {line[j]} ")
        j+=1
