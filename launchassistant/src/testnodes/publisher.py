#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
 
class yamazaki_broadcaster(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("yamazaki_broadcaster") 
        self.publisher_ = self.create_publisher(String, "yamazaki_broadcaster")
 
 
def main(args=None):
    rclpy.init(args=args)
    node = yamazaki_broadcaster() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()