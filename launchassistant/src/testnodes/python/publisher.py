#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64 
 
class yamazaki_broadcaster(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("yamazaki_broadcaster") 
        self.number_ = 2
        self.publisher_ = self.create_publisher(Int64, "yamazaki_broadcaster", 10)
        self.number_timer_ = self.create_timer(1.0, self.publish_number)
        self.get_logger().info("yamazaki broadcaster has been started.")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)
 
def main(args=None):
    rclpy.init(args=args)
    node = yamazaki_broadcaster() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()