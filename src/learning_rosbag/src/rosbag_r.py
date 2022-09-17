#! /usr/bin/python3

import rosbag
import rospy
import std_msgs.msg

if __name__ == "__main__":
    rospy.init_node("rosbag_r")

    bag = rosbag.Bag("bag_record.bag", 'r')

    msgs = bag.read_messages()

    for i in msgs:
        print(i)

    bag.close()
