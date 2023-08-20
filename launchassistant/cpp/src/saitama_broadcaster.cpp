#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class SaitamaBroadcasterNode : public rclcpp::Node
{
public:
    SaitamaBroadcasterNode() : Node("saitama_broadcaster"), number_(2)
    {
        number_publisher_ = this->create_publisher<example_interfaces::msg::Int64>("saitama", 10);
        number_timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                                std::bind(&SaitamaBroadcasterNode::publishNumber, this));
        RCLCPP_INFO(this->get_logger(), "Saitama broadcaster has been started.");
    }

private:
    void publishNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = number_;
        number_publisher_->publish(msg);
    }

    int number_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr number_publisher_;
    rclcpp::TimerBase::SharedPtr number_timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SaitamaBroadcasterNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}