#! /usr/bin/python3

import rospy
from turtlesim.srv import *
import sys


def spawn_client(data):
    rospy.wait_for_service("/turtle_spawn")
    rospy.init_node("spawn_client")
    try:
        # print(data)
        turtle_spawn = rospy.ServiceProxy("/turtle_spawn", Spawn)
        return turtle_spawn.call(data)

    except rospy.ServiceException:
        print("error")


def usage():
    print("%s [x y theta 'name']" % sys.argv[0])


if __name__ == "__main__":
    data_list = SpawnRequest()
    list = []
    if len(sys.argv) == 5:
        data_list.x = float(sys.argv[1])
        data_list.y = float(sys.argv[2])
        data_list.theta = float(sys.argv[3])
        data_list.name = sys.argv[4]
        # for i in sys.argv[1:-1]:
        #     list.append(float(eval(i)))
        # list.append(sys.argv[-1])
        # print(data_list)
        # spawn_client(float(sys.argv[1]), float(
        #     sys.argv[2]), float(sys.argv[3]), sys.argv[4])
        response = spawn_client(data_list)
        rospy.loginfo(response)
    else:
        usage()
        sys.exit(1)
