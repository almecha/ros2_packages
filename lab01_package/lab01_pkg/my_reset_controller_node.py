#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class MyNode(Node):
    def __init__(self):
        super().__init__("reset_controller")
        self.msg = Twist()
        self.my_publisher = self.create_publisher(Twist,"/cmd_topic",10)
        self.reset_subscriber = self.create_subscription(Bool,"/reset",self.reset_callback,10)
        self.state = 0
        self.duration = 1
        self.directions= ["along X","along Y","against X","against Y"]
        self.timer = self.create_timer(1, self.timer_callback)
        self.elapsed_time = -1


    def timer_callback(self):
        self.elapsed_time += 1
        if (self.elapsed_time >= self.duration):
            self.elapsed_time = 0
            self.state  = (self.state + 1) % 4

            if self.state == 0:
                self.duration += 1
        
        if self.state == 0:
            self.msg.linear.x = 1.0
            self.msg.linear.y = 0.0
        elif self.state == 1:
            self.msg.linear.x = 0.0
            self.msg.linear.y = 1.0
        elif self.state == 2:
            self.msg.linear.x = -1.0
            self.msg.linear.y = 0.0
        elif self.state == 3:
            self.msg.linear.x = 0.0
            self.msg.linear.y = -1.0

        self.my_publisher.publish(self.msg)
        self.get_logger().info(f"Move {self.directions[self.state]}     |    Time {time.ctime(time.time())}")
        
    def reset_callback(self, reset_msg):
        if reset_msg.data:
            
            self.state = 0
            self.duration = 1
            self.timer.reset()





def main(args = None):
    rclpy.init(args = args)     # Start the communication with ROS
    ## Code below ##
    node = MyNode()
    rclpy.spin(node)
    ####
    rclpy.shutdown()

if __name__ == "__main__":
    main()