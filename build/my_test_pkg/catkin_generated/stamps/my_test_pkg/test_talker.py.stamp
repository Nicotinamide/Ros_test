#! /usr/bin/python3
import rospy
from std_msgs.msg import String
import time
def talker():
    pub = rospy.Publisher("chat",String,queue_size=10)
    rospy.init_node('talker')

    r = rospy.Rate(30)

    while not rospy.is_shutdown():
        str = 'hello ' + time.ctime()
        pub.publish(str)
        rospy.loginfo(str)
        r.sleep()
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

