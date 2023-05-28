#!/usr/bin/python

import rospy
from beginner_tutorials.srv import fibonacci
from beginner_tutorials.msg import Num

class AutoPoseClient:
    def __init__(self):
        rospy.init_node('autopose_client')
        rospy.Subscriber('inputNumber', Num, self.input_callback)
        #self.input_sub = rospy.Subscriber('inputNumber', Num, self.input_callback)
        self.navigator_service = rospy.ServiceProxy('n_fibonacci', fibonacci)
        self.latest_input = None
        rospy.loginfo("constructor is running")
        rospy.spin()

    def input_callback(self, msg):
        rospy.loginfo("subscriber callback is running")
        self.latest_input = msg.num
        self.process_fibonacci()

    def process_fibonacci(self):
        rospy.loginfo("fibonacci proccesing callback has started")
        if self.latest_input is not None:
            try:
                rospy.loginfo("server is being contacted")
                response = self.navigator_service(self.latest_input)
                fibonacci_num = response.n_num
                print(f"Calculated Fibonacci number for {self.latest_input}: {fibonacci_num} ")
            except rospy.ServiceException as e:
                print("Service call failed: %s", e)

if __name__ == "__main__":
    autopose_client = AutoPoseClient()

