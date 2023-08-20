#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class SaitamaReceiverNode : public rclcpp::Node
{
public:
    SaitamaReceiverNode() : Node("saitama_receiver"), counter_(0)
    {
        counter_publisher_ = this->create_publisher<example_interfaces::msg::Int64>("saitama", 10);
        number_subscriber_ = this->create_subscription<example_interfaces::msg::Int64>(
            "saitama", 10, std::bind(&SaitamaReceiverNode::callbackNumber, this, std::placeholders::_1));
    }

private:
    void callbackNumber(const example_interfaces::msg::Int64::SharedPtr msg)
    {
        counter_ += msg->data;
        auto newMsg = example_interfaces::msg::Int64();
        newMsg.data = counter_;
        counter_publisher_->publish(newMsg);
    }

    int counter_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr counter_publisher_;
    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr number_subscriber_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SaitamaReceiverNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}