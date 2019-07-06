#!/usr/bin/env python
# coding: utf-8

# # Tik-Tak-Toe game Using Python By Purnendu Das
# ### das888purnendu@gmail.com
# #### Date:06-07-2019

# In[1]:


import random


# In[2]:


win=''
board=[]
free=[]
cmp=[]
usr=[]

row = col = 3 #Row Number and Column Number (Use >=3 )

board = [[None for j in range(col)] for i in range(row)]
layout = [[str(i)+str(j) for j in range(col)] for i in range(row)]


# In[3]:


def reset():
    global board
    global row
    global col
    global free
    global cmp
    global usr
    global win
    
    win=''
    free=[]
    cmp=[]
    usr=[]
    board = [[None for j in range(col)] for i in range(row)]
    print("\n \t User mark = X and Computer mark = O \n")
    print("\n \t : Positions : \n")
    
    print ("----"*col)
    for i in layout:
        c=0
        s=""
        for j in i:
            if c==0:
                s+="  "+str(j)+" "
            else:
                s+="|  "+str(j)+" "
            c+=1
        print(s)
        print ("----"*col)


# In[4]:


def user():
    global board

    inp = list(input("Please Enter The position without space or comma : "))
    ln= len(inp)
    if ln==2:
        try:
            i = int(inp[0])
            j = int(inp[1])
            if ( i>= 0 and i <= (row-1) and j>=0 and j<=(col-1)):
                if (board[i][j]== None):
                    board[i][j]= 0
                    return 1

                else:
                    print("\nPosition Already Filled Please correct !")
                    return 0
            else:
                print("\nPosition Not Found Please correct !")
                return 0

        except ValueError:
            print("\nWrong Input Please correct !")
            return 0
    else:
        print("\nWrong Input Please correct !")
        return 0


# In[5]:


def free_check():
    global board
    global free
    global cmp
    global usr
    
    free=[]
    cmp=[]
    usr=[]
   
    count_i=0
    for i in board:
        count_j=0
        for j in i:
            if j==1:
                cmp.append((count_i,count_j))
            elif j==0:
                usr.append((count_i,count_j))
            else:
                free.append((count_i,count_j))
            count_j+=1
        count_i+=1
        
    free.sort()
    cmp.sort()
    usr.sort()


# In[6]:


def rand():
    free_check()
    global free
    global board
    ln = len(free)
    
    
    if(ln==0):
        return 0
    
    elif(ln==1):
        board [free[0][0]][free[0][1]] = 1
        return 1
        
    else:
        rand = random.randint(0,ln-1)
        board [free[rand][0]][free[rand][1]] = 1
        return 2


# In[7]:


def win_chk():
    free_check()
    global win
    global usr
    global cmp
    global col
    global row
    global board
    res =0
    
    
    if(len(cmp)>2):
        temp_i = [ i[0] for i in cmp]
        temp_j = [ j[1] for j in cmp]
        p_i = list(set(temp_i))
        p_j = list(set(temp_j))
        count_i = [temp_i.count(i) for i in p_i]
        count_j = [temp_j.count(j) for j in p_j]
        




        if row in count_i or col in count_j:
            win="Computer"
            return 1
        else:
            res= 0
        

        temp=1
        count=0
        count_r=0
        for i in range(0,row):
            for j in range(0,col):
                if(i==j):
                    if(temp==board[i][j]):
                        count+=1
                if(i==(row-1)-j and j==(col-1)-i):
                    if(temp==board[i][j]):
                        count_r+=1
        if count==row or count_r==row:
            win="Computer"
            return 1
        
        else:
            res= 0
        
    
    if(len(usr)>2):
        temp_i = [ i[0] for i in usr]
        temp_j = [ j[1] for j in usr]
        p_i = list(set(temp_i))
        p_j = list(set(temp_j))
        count_i = [temp_i.count(i) for i in p_i]
        count_j = [temp_j.count(j) for j in p_j]
        
        
      
        
        if row in count_i or col in count_j:
            win="You"
            return 1
        else:
            res= 0
        
        temp=0
        count=0
        count_r=0
        for i in range(0,row):
            for j in range(0,col):
                if(i==j):
                    if(temp==board[i][j]):
                        count+=1
                if(i==(row-1)-j and j==(col-1)-i):
                    if(temp==board[i][j]):
                        count_r+=1
                        
        if count==row or count_r==row:
            win="You"
            return 1
        else:
            res= 0
            
        return res
        
    else:
        res= 0
        return res


# In[8]:


def game():
    global board
    global col
    print ("----"*col)
    for i in board:
        s=""
        c=0
        for j in i:
            if c==0:
                if j==1:
                    s+=" O "
                elif j==0:
                    s+=" X "
                else:
                    s+="   "
            else:
                if j==1:
                    s+="| O "
                elif j==0:
                    s+="| X "
                else:
                    s+="|   "
            c+=1
        print(s)
        print ("----"*col)


# In[9]:


def game_over():
    global win
    global col
    print("\nGame is Over")
    print("\n\t Draw Match !" if win=='' else "\n\t"+ win+" Win !" )
    global board
    print ("----"*col)
    
    for i in board:
        s=""
        c=0
        for j in i:
            if c==0:
                if j==1:
                    s+=" O "
                elif j==0:
                    s+=" X "
                else:
                    s+="   "
            else:
                if j==1:
                    s+="| O "
                elif j==0:
                    s+="| X "
                else:
                    s+="|   "
            c+=1
        print(s)
        print ("----"*col)


# In[10]:


def play_game():
    reset()
    
    while True:
        print("\n Computer :")
        game()
        rs = user()
        while rs!=1:
            rs = user()
        
        wn = win_chk()
        if wn:
            game_over()
            break
            
        else:
            print("\n You :")
            game()
            rn = rand()
            if rn==1:
                win_chk()
                game_over()
                break
                
            elif rn==0:
                game_over()
                break
                
            else:
                wn = win_chk()
                if wn:
                    game_over()
                    break


# In[11]:


play_game() # To Play


# #                           Thank You !
