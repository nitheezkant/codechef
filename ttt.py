# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:31:36 2021

@author: Rajinikanth.U
"""
ch=int(input(""))
for i in range(ch):
    f=input("")
    s=input("")
    t=input("")
    if f=="XXX" or s=="XXX" or t=="XXX" or (f[0]=="X" and s[1]=="X" and t[2]=="X") or (f[2]=="X" and s[1]=="X" and t[0]=="X") or (f[0]=="X" and s[0]=="X" and t[0]=="X") or (f[1]=="X" and s[1]=="X" and t[1]=="X") or (f[2]=="X" and s[2]=="X" and t[2]=="X"):
        if f=="OOO" or s=="OOO" or t=="OOO" or (f[0]=="O" and s[1]=="O" and t[2]=="O") or (f[2]=="O" and s[1]=="O" and t[0]=="O") or (f[0]=="O" and s[0]=="O" and t[0]=="O") or (f[1]=="O" and s[1]=="O" and t[1]=="O") or (f[2]=="O" and s[2]=="O" and t[2]=="O"):
            print(3)
        else:
            cx=0
            cy=0
            
            for i1 in f:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass
            for i1 in s:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass    
            for i1 in t:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass 
            if cx==cy+1:
                print(1)
            else:
                print(3)
    elif f=="OOO" or s=="OOO" or t=="OOO" or (f[0]=="O" and s[1]=="O" and t[2]=="O") or (f[2]=="O" and s[1]=="O" and t[0]=="O") or (f[0]=="O" and s[0]=="O" and t[0]=="O") or (f[1]=="O" and s[1]=="O" and t[1]=="O") or (f[2]=="O" and s[2]=="O" and t[2]=="O"):
        if f=="XXX" or s=="XXX" or t=="XXX" or (f[0]=="X" and s[1]=="X" and t[2]=="X") or (f[2]=="X" and s[1]=="X" and t[0]=="X") or (f[0]=="X" and s[0]=="X" and t[0]=="X") or (f[1]=="X" and s[1]=="X" and t[1]=="X") or (f[2]=="X" and s[2]=="X" and t[2]=="X"):
        
            print(3)
        else:
            cx=0
            cy=0
            
            for i1 in f:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass
            for i1 in s:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass    
            for i1 in t:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass 
            if cx==cy:
                print(1)
            else:
                print(3)            
    elif "_" not in (f+s+t):
            for i1 in f:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass
            for i1 in s:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass    
            for i1 in t:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass 
            if cx==cy+1:
                print(1)
            else:
                print(3)
                
        
    else:
            cx=0
            cy=0
            
            for i1 in f:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass
            for i1 in s:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass    
            for i1 in t:
                if i1=="X":
                    cx=cx+1
                elif i1=="O":
                    cy=cy+1
                else:
                    pass 
            if cx==cy or cx==cy+1:
                print(2)
            else:
                print(3)
                
                
        
            
                
