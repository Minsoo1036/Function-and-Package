# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:18:43 2021

code by "jump to python"

@author: pc
"""

#just do iterative implementation
import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)
    
print("Start")
for i in range(5):
    long_task()
    
print("End")



#threading
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)
        
threads = []

for i in range(5):
    t=threading.Thread(target=long_task)
    threads.append(t) #not spending much time to insert 
    
for t in threads:
    t.start()
    
for t in threads:
    t.join()    

    
print("End")