from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # return LaunchDescription([
    #     Node(
    #         package='my_package',
    #         executable='my_node',
    #         name='my_node'
    #     )
    # ])
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            parameters=[{'serial_port': '/dev/ttyUSB0'}],
            remappings=[('/scan', '/scan_1')]
        ),
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            parameters=[{'serial_port': '/dev/ttyUSB1'}],
            namespace='/scanner2',
        )
    ])
