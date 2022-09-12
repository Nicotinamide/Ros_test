#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def circle():
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node("turtle_pub_node_p")
    twist = Twist()
    twist.linear.x = 2.0
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
