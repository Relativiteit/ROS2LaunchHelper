#include "rclcpp/rclcpp.hpp"
// include your c++ path depending on your machine shift + ctrl + p on vscode
// add_execeutable with dependencies to CMakelist.txt
// install (TARGETS....)

class MoriokaPublisherNode : public rclcpp::Node
{
public:
    MoriokaPublisherNode() : Node("morioka_publisher")
    {
        publisher_ = this->create_publisher<example_interfaces::msg::String>("morioka", 10)
                         timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&MoriokaPublisherNode::timerCallBack, this));
        RCLCPP_INFO(this->get_logger(), "The Morioka Publisher has started");
    }

private:
    void timerCallBack()
    {
        RCLCPP_INFO(this->get_logger(), 105)
    }

    void publishJajamen()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = std::string("O")
    }
    rclcpp::TimerBase::SharedPtr timer_;
    int counter_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MoriokaPublisherNode>("morioka_publisher");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}