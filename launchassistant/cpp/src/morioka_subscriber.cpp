class MoriokaSubscriberNode : public rclcpp::Node
{
public:
    MoriokaSubscriberNode() : Node("morioka_subscriber")
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::String>("morioka", 10,
                                                                                 std::bind(&MoriokaSubscriberNode::callbackMorioka, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "Morioka subscriber is online.");
    }

private:
    void callbackMorioka(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this - < get_logger(), "%s", msg->data.c_str());
    }

    rclccp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MoriokaSubscriberNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}