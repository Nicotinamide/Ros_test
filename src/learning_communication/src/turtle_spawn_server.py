#! /usr/bin/python3

import rospy
from turtlesim.srv import Spawn


def handler_spawn(data):
    turtle_spawn = rospy.ServiceProxy("/spawn", Spawn)
    print(data.x, data.y, data.theta, data.name)
    return turtle_spawn.call(data)


def spawn_server():
    rospy.init_node("spawn_server")
    spawn = rospy.Service("turtle_spawn", Spawn, handler_spawn)
    rospy.loginfo("Spawn server is running")
    rospy.spin()


if __name__ == "__main__":
    spawn_server()
