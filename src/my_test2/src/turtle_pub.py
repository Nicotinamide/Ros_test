#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist


def circle():
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node("turtle_pub_node_p")
    twist = Twist()
    twist.linear.x = 2.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 2.0
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(twist)
        rospy.loginfo('\n' + str(twist))
        rate.sleep()


if __name__ == "__main__":
    try:
        circle()
    except rospy.ROSInterruptException:
        print("ERROR")

# import rospy
# from geometry_msgs.msg import Twist

# if __name__ == "__main__":
#     # 2.初始化 ROS 节点
#     rospy.init_node("control_circle_p")
#     # 3.创建发布者对象
#     pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1000)
#     # 4.循环发布运动控制消息
#     rate = rospy.Rate(10)
#     msg = Twist()
#     msg.linear.x = 1.0
#     msg.linear.y = 0.0
#     msg.linear.z = 0.0
#     msg.angular.x = 0.0
#     msg.angular.y = 0.0
#     msg.angular.z = 0.5

#     while not rospy.is_shutdown():
#         pub.publish(msg)
#         rospy.loginfo(msg)
#         rate.sleep()
