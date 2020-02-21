from time import sleep
from threading import Thread
import subprocess as sp


class job_1(Thread):
    def run(self):
         command = [ 'SU2_CFD' ,'/home/neelu/Desktop/new_wing/1/turb_ONERAM6.cfg']
         sp.call(command)
         #sleep(0.1)
         print("job_1")
         
class job_2(Thread):
    def run(self):
        command = [ 'SU2_CFD' ,'/home/neelu/Desktop/new_wing/2/turb_ONERAM6.cfg']
        sp.call(command)
        #sleep(0.1)
        print("job_2")
        
class job_3(Thread):
    def run(self):
        command = [ 'SU2_CFD' ,'/home/neelu/Desktop/new_wing/3/turb_ONERAM6.cfg']
        sp.call(command)
        #sleep(0.1)
        print("job_3")
         
t1 = job_1()
t2 = job_2()
t3 = job_3()


t1.start()
sleep(0.1)
t2.start()
sleep(0.1)
t3.start()


# join module will allow below line to get exectued 
#only after all the threads all have done with their work. 
t1.join()
t2.join()
t3.join()


print("I am done with parallel working")


