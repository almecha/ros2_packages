#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from std_msgs.msg import Bool


class MyNode(Node):
    def __init__(self):
        super().__init__("reset_node")
        self.pose_subscriber = self.create_subscription(Pose, "/pose",self.reset_callback,10)
        self.reset_publisher = self.create_publisher(Bool, "/reset",10)
        self.reset_msg = Bool()
    
    def reset_callback(self,msg):
        distance = (pow(msg.position.x,2) + pow(msg.position.y,2))**(1/2)
        self.reset_msg.data = distance > 6.0
        self.reset_publisher.publish(self.reset_msg)
        self.get_logger().info(f"Reset : {self.reset_msg.data}")



def main(args = None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()