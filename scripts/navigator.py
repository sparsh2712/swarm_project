#!/usr/bin/env python 

import rospy 
from beginner_tutorials.srv import fibonacci

class Navigator:
    def __init__(self):
        rospy.init_node("navigator")
        self.fibonacci_server = rospy.Service('n_fibonacci',fibonacci, self.cb_fibonacci)
        print("Ready to return the desired fiibonacci number.")
        rospy.spin()
    def cb_fibonacci(self,req): 
        rospy.loginfo("service is called")
        if req.n == 1:
            print("Returning %s fibonacci number which is 0"%(req.n))
            return 0
        if req.n == 2:
            print("Returning %s fibonacci number which is 1"%(req.n))
            return 1
        else:
            a,b = 0,1
            for _ in range(3, req.n+1):
                a,b = b, a+b
            print("Returning %s fibonacci number which is %s"%(req.n,b))
            return b

if __name__ == "__main__":
    navigator = Navigator()
