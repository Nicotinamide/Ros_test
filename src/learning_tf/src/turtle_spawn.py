#! /usr/bin/python3

import rospy
from turtlesim.srv import Spawn


if __name__ == "__main__":
    rospy.init_node("turtle_spawn")

    rospy.wait_for_service("/spawn")
    try:
        spawn = rospy.ServiceProxy("/spawn", Spawn)
        spawn.call(1, 1, 0, 'turtle2')
    except Exception as e:
        rospy.loginfo("error:%s" % e)
