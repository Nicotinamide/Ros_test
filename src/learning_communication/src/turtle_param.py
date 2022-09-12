#! /usr/bin/python3

import rospy
import sys
from std_srvs.srv import Empty


def set_param(r, g, b):
    rospy.init_node("param_set")
    dict = {
        'background_b': b,
        'background_g': g,
        'background_r': r
    }
    rospy.set_param("/turtle1", dict)
    turtle_clear = rospy.ServiceProxy("/clear", Empty)
    turtle_clear.call()


def usage():
    return ("sys.argv[0]"+"[r g b]")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        r = eval(sys.argv[1])
        g = eval(sys.argv[2])
        b = eval(sys.argv[3])
        #print(r, g, b)
        try:
            set_param(r, g, b)
        except:
            print("unknow error")
    else:
        print(usage())
        sys.exit(1)
