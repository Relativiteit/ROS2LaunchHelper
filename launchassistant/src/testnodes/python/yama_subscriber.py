#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64 
 
class yamazaki_subscriber(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("yamazaki_receiver") 
        self.counter_
        self.publisher_ = self.create_publisher(Int64, "yamazaki", self.callback_yamazaki, 10)
        self.get_logger().info("yamazaki subscriber has been started.")

    def callback_yamazaki(self, msg):
        self.get_logger().info(msg.data)

 
def main(args=None):
    rclpy.init(args=args)
    node = yamazaki_subscriber() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()