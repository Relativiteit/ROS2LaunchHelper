cmake_minimum_required(VERSION 3.8)
project(cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(morioka_publisher src/morioka_publisher.cpp)
ament_target_dependencies(morioka_publisher rclcpp example_interfaces)

add_executable(morioka_subscriber src/morioka_subscriber)
ament_target_dependencies(morioka_subscriber rclcpp example_interfaces)

add_executable(saitama_broadcaster src/saitama_broadcaster)
ament_target_dependencies(saitama_broadcaster rclcpp example_interfaces)

add_executable(saitama_receiver src/saitama_receiver)
ament_target_dependencies(saitama_receiver rclcpp example_interfaces)


install(TARGETS
      morioka_publisher
      morioka_subscriber
      saitama_broadcaster
      saitama_broadcaster
      DESTIONATION lib/${PROJECT_NAME}
      )
ament_package()
