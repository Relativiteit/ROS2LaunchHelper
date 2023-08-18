#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64 
 
class yamazaki_subscriber(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("yamazaki_broadcaster") 
        self.counter_
        self.publisher_ = self.create_publisher(Int64, "yamazaki_subscriber", 10)
        self.number_timer_ = self.create_timer(1.0, self.publish_number)
        self.get_logger().info("yamazaki subscriber has been started.")

 
def main(args=None):
    rclpy.init(args=args)
    node = yamazaki_subscriber() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()