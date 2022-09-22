import os

dump_memory=[]
variable_values={}
register_values = [0,0,0,0,0,0,0,0]  

PC = 0

PC_list=[]
cyc=0  
h=False
JumpC=[False]   
count_line=0

pc_return = 0

def dec_to_16bin(n):
    output = ""
    while (n>0):
        digit = n%2
        n = n//2
        output = str(digit)+output
    while len(output)<=15 :
        output = "0"+ output
    return output


def dec_to_8bin(n):
    output = ""
    while (n>0):
        digit = n%2
        n = n//2
        output = str(digit)+output
    while len(output)<=7 :
        output = "0"+ output
    return output

def standard_output():   
    opcode=[]
    dic = {}
    dic["p_c"] = dec_to_8bin(PC)
    dic["register_0"] = dec_to_16bin(register_values[0])
    dic["register_1"] = dec_to_16bin(register_values[1])
    dic["register_2"] = dec_to_16bin(register_values[2])
    dic["register_3"] = dec_to_16bin(register_values[3])
    dic["register_4"] = dec_to_16bin(register_values[4])
    dic["register_5"] = dec_to_16bin(register_values[5])
    dic["register_6"] = dec_to_16bin(register_values[6])
    dic["flag"] = dec_to_16bin(register_values[7])
    
    prgram_counter = dic.get("p_c")
    r0 = dic.get("register_0")
    r1 = dic.get("register_1")
    r2 = dic.get("register_2")
    r3 = dic.get("register_3")
    r4 = dic.get("register_4")
    r5 = dic.get("register_5")
    r6 = dic.get("register_6")
    Flg = dic.get("flag")
   
    opcode=[prgram_counter,r0,r1,r2,r3,r4,r5,r6,Flg]
    print(*opcode)



def addition(ins):   
    k=2
    d=1
    R1 = int(ins[7:10+(d-1)],k) 
    R2 = int(ins[10:13+(d-1)],k)
    R3 = int(ins[13+(d-1):16],k) 
    register_values[R3] = register_values[R2] + register_values[R1]
    ab =0
    a=register_values[R3] < ab
    b=register_values[R3] >(65535+0)
    if a or b:
        register_values[R1] = register_values % (65536+ab)
        register_values[7] = (7+1)
    else:
        register_values[7] = (d-1)

    

def subtraction(ins):
    xy=2
    lp=0
    Reg1 = int(ins[7:10+lp],xy) 
    Reg2 = int(ins[10+lp:13],xy)
    Reg3 = int(ins[13:16+lp],xy)
    ef =  register_values[Reg1]
    gh = register_values[Reg2]
    register_values[Reg3] = ef - gh

    d =1
    e=0
    a = register_values[Reg2]
    b = register_values[Reg1]
    if  a>b :
        register_values[Reg3] = (d-1)
        register_values[7]= (8+e)
    else:
        register_values[7] = (d-1)



def MovI(ins):
    d=4
    e=0
    Reg1=int(ins[5:(8+e)],d-2)
    imm=int(ins[(8+e):],d-2)
    register_values[Reg1]=imm
    register_values[7]=e


def MovR(ins):
    d=4
    e=0
    Reg1=int(ins[10:13],d-2)
    Reg2=int(ins[13:],d-2)
    register_values[Reg2] = register_values[Reg1]
    register_values[7]=e



def Ld(ins):
    d=4
    e=0
    Reg1=int(ins[5:(8+e)],d-2)
    mem_add=int(ins[(8+e):],d-2)
    register_values[Reg1]=int(dump_memory[mem_add],2)
    register_values[7]=e


def St(ins):
    d=4
    e=0
    Reg1=int(ins[5:(8+e)],d-2)
    mem_add=int(ins[(8+e):],d-2)
    dump_memory[mem_add]=dec_to_16bin(register_values[Reg1])
    register_values[7]=e


def multiply(ins):
    d=4
    e=0    
    Reg1 = int(ins[7:(10+e)],d-2) 
    Reg2 = int(ins[(10+e):13],d-2)
    Reg3 = int(ins[13:(16+e)],d-2) 
    register_values[Reg3] = register_values[Reg2] * register_values[Reg1]
    print(register_values[Reg3])
    if register_values[Reg3] >(65535+e):
        temp=dec_to_16bin(register_values[Reg3])
        register_values[Reg3]=int(temp[len(temp)-(16+e):],d-2)
        register_values[7]=8+e
    else:
        register_values[7]=e


def division(ins):
    d=4
    e=0
    Reg1=int(ins[(10+e):13],d-2)
    Reg2=int(ins[(13+e):],d-2)
    register_values[0]=Reg1/Reg2
    register_values[1]=Reg1%Reg2
    register_values[7]=e


def right_shift(ins):       
    d=4
    e=0
    Reg1=int(ins[5:8],d-2)
    imm=int(ins[8:],d-2)
    register_values[Reg1] = register_values[Reg1] >> imm
    register_values[7]=e


def left_shift(ins):
    d=4
    e=0
    Reg1=int(ins[5:(8+e)],d-2)
    imm=int(ins[(8+e):],d-2)
    register_values[Reg1] = register_values[Reg1] << imm
    register_values[7]=e


def xor_1(ins):
    d=4
    e=0
    Reg1 = int(ins[7:(10+e)],d-2) 
    Reg2 = int(ins[10:(13+e)],d-2)
    Reg3 = int(ins[(13+e):16],d-2) 
    register_values[Reg3] = register_values[Reg2] ^ register_values[Reg1]


def or_1(ins):
    d=4
    e=0
    Reg1 = int(ins[7:(10+e)],d-2) 
    Reg2 = int(ins[(10+e):13],d-2)
    Reg3 = int(ins[13:(16+e)],d-2) 
    register_values[Reg3] = register_values[Reg2] | register_values[Reg1]
    register_values[7]=e


def and_1(ins):
    d=4
    e=0
    Reg1 = int(ins[7:(10+e)],d-2) 
    Reg2 = int(ins[(10+e):13],d-2)
    Reg3 = int(ins[13:(16+e)],d-2) 
    register_values[Reg3] = register_values[Reg2] & register_values[Reg1]
    register_values[7]=e


def INV(ins):
    d=4
    e=0
    Reg1=int(ins[10:(13+e)],d-2)
    Reg2=int(ins[(13+e):],d-2)
    binary=dec_to_16bin(register_values[Reg1])
    temp=""
    for j in binary:
        if j=="0":
            temp=temp+"1"
        elif j=="1":
            temp = temp +"0"
    register_values[Reg2] = int(temp,2+e)
    register_values[7]=e


def Cmp(ins):
    d=4
    e=0
    Reg1 = int(ins[10:(13+e)],d-2)
    Reg2 = int(ins[(13+e):],d-2)
    if(register_values[Reg1] == register_values[Reg2]):
        register_values[7] = e+1
    elif (register_values[Reg1] < register_values[Reg2]):
        register_values[7] = e+4
    else:
        register_values[7] = e+2

def jump(ins):
    pass


def jump_less(ins): 
    d=4
    e=0
    if register_values[7]==(4-e):
        JumpC[0]=True
    register_values[7]=e
    

def jump_great(ins):
    d=2
    e=0
    if register_values[7]==d:
        
        JumpC[0]=True
    register_values[7]=e
    


def jump_equal(ins):
    d=1
    e=0
    if register_values[7]==d:
        JumpC[0]=True
    register_values[7]=e


def halt_function(ins):    
    e=0
    halt=True
    register_values[7]=e


count=[0]
stdinp = []


while 1:              
    try:
        x=input()
        stdinp.append(x)
    except EOFError:
        break

for j in stdinp:  
    dump_memory.append(j)

while len(dump_memory) < 256:
    dump_memory.append("0"+"")

while h == False:
    if stdinp[PC][0:5] == "10000":
        e=0
        addition(stdinp[PC])
        standard_output()
        count_line += (1+e)
        PC_list.append(PC)
        PC += (1+e)
        cyc += (1+e)
        
        
    if stdinp[PC][0:5] == "10001": 
        e=0
        d=1
        subtraction(stdinp[PC])
        standard_output()
        PC_list.append(PC)
        count_line += (1+(d-1))
        PC += (1+e)
        y=e
        cyc += (1+(d-1))

    if stdinp[PC][0:5] == "10010":
        e=0 
        MovI(stdinp[PC])
        standard_output()
        count_line += (1+e)
        PC_list.append(PC)
        PC += (1+e)
        cyc += (1+e)

    if stdinp[PC][0:5] == "10011": 
        d=0
        MovR(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "10100": 
        d=0
        Ld(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "10101": 
        d=0
        St(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "10110": 
        d=0
        multiply(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
    
    if stdinp[PC][0:5] == "10111": 
        d=0
        division(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "11000": 
        d=0
        right_shift(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "11001": 
        d=0
        left_shift(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "11010": 
        d=0
        xor_1(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "11011": 
        d=0
        or_1(stdinp[PC])
        standard_output()
        count_line += (1+d)
        PC_list.append(PC)
        PC += (1+d)
        cyc += (1+d)
        
    if stdinp[PC][0:5] == "11100": 
        d=0
        and_1(stdinp[PC])
        standard_output()
        count_line+=(1+d)
        PC_list.append(PC)
        PC+=(1+d)
        cyc+=(1+d)
        
    if stdinp[PC][0:5] == "11101": 
        d=0
        INV(stdinp[PC])
        standard_output()
        count_line+=(1+d)
        PC_list.append(PC)
        PC+=(1+d)
        cyc+=(1+d)
        
    if stdinp[PC][0:5] == "11110":
        d=0
        Cmp(stdinp[PC])
        standard_output()
        count_line+=(1+d)
        PC_list.append(PC)
        PC+=(1+d)
        cyc+=(1+d)
        
    if stdinp[PC][0:5] == "11111":
        d=0
        jump(stdinp[PC])
        standard_output()
        count_line+=(1+0)
        PC_list.append(PC)
        PC=int(stdinp[PC][8:],2+d)
        cyc+=(1+d)
        
    if stdinp[PC][0:5] == "01100":
        d=2
        e=0
        jump_less(stdinp[PC])
        standard_output()
        count_line = count_line+(1+e)
        PC_list.append(PC)
        if JumpC[0]==True:
            PC=int(stdinp[PC][(8+e):],d)
        else:
            PC+=(1+e)
        JumpC[0]=False
        cyc = cyc+(1+e)
        
    if stdinp[PC][0:5] == "01101":   
        d=0 
        jump_great(stdinp[PC])
        standard_output()
        count_line+=1
        PC_list.append(PC)
        if JumpC[0]==True:
            PC=int(stdinp[PC][8:],2+d)
        else:
            PC+=(1+d)
        JumpC[0]=False
        cyc+=(1+d)
        
    if stdinp[PC][0:5] == "01111":
        d=0
        jump_equal(stdinp[PC])
        standard_output()
        count_line+=((1+d)+d)
        PC_list.append(PC)
        if JumpC[0]==True:
            PC=int(stdinp[PC][8:],2+d)
        else:
            PC+=(1+d)
        JumpC[0]=False
        cyc+=(1+d)
        
    if stdinp[PC][0:5] == "01010": 
        d=0
        halt_function(stdinp[PC])
        standard_output()
        count_line += (1+d)
        break
for i in range(len(dump_memory)):
    if i==len(dump_memory)-1:
        if(dump_memory[i]=='0'):
            dump_memory[i]='0000000000000000'
        else:
            dump_memory[i]=f'{dump_memory[i]}'
    else:
        if dump_memory[i]=="0":
            dump_memory[i]='0000000000000000\n'
        else:
            dump_memory[i]=f'{dump_memory[i]}\n'

print(*dump_memory,sep="")