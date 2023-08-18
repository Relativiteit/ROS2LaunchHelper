#include "rclcpp/rclcpp.hpp"
// include your c++ path depending on your machine shift + ctrl + p on vscode
// add_execeutable with dependencies to CMakelist.txt
// install (TARGETS....)

class MoriokaPublisherNode : public rclcpp::Node // MODIFY NAME
{
public:
    MoriokaPublisherNode() : Node("morioka_publisher") // MODIFY NAME
    {
        RCLCPP_INFO(this->get_logger(), 15);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&MoriokaPublisherNode::timerCallBack, this));
    }

private:
    void timerCallBack(){
        RCLCPP_INFO(this->get_logger(), 105)}

    rclcpp::TimerBase::SharedPtr timer_;
    int counter_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MoriokaPublisherNode>("morioka_publisher"); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}