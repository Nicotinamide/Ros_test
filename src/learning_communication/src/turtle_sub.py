#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose


def callback(data):
    # print("x={},y={},theta={},l_v={},a_v={}".format(data.x, data.y,
    #       data.theta, data.linear_velocity, data.angular_velocity))
    print(data)


def sub():
    rospy.init_node("turtle_sub")
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback)
    rospy.spin()


if __name__ == "__main__":
    try:
        sub()
    except:
        print("error")
