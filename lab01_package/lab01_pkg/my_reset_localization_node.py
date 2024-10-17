#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from std_msgs.msg import Bool

class MyNode(Node):
    def __init__(self):
        super().__init__("reset_localization")
        self.my_subscriber = self.create_subscription(Twist, "/cmd_topic",self.subscription_callback,10)
        self.reset_subscriber = self.create_subscription(Bool,"/reset",self.reset_callback,10)
        self.pose_publisher = self.create_publisher(Pose,"/pose",10)
        self.pose_msg = Pose()
        # self.pose_x = 0
        # self.pose_y = 0
        self.my_subscriber

    def subscription_callback(self, msg):
        # self.pose_x += msg.linear.x
        # self.pose_y += msg.linear.y
        self.pose_msg.position.x += msg.linear.x
        self.pose_msg.position.y += msg.linear.y
        self.pose_publisher.publish(self.pose_msg)
        self.get_logger().info(f'Position X:{self.pose_msg.position.x}||| Y:{self.pose_msg.position.y}')

    def reset_callback(self,reset_msg):
        if reset_msg.data:
            self.pose_msg.position.x = 0.0
            self.pose_msg.position.y = 0.0

        
def main(args = None):
    rclpy.init(args = args)
    ####
    node = MyNode()
    rclpy.spin(node)
    ####
    rclpy.shutdown()

if __name__ =="__main__":
    main()