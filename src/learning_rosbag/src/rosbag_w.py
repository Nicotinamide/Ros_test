#! /usr/bin/python3

import rospy
import rosbag
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("rosbag_w")

    bag = rosbag.Bag("bag_record.bag", 'w')

    msg = String()
    msg.data = "hello bag!"
    bag.write("/liaotian", msg)

    bag.close()
