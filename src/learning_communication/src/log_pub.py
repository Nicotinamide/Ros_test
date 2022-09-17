#! /usr/bin/python3

import rospy

if __name__ == "__ main__":
    rospy.init_node("log_pub")

    #rate = rospy.Rate(0.3)
    rospy.loginfo("loginfo")

    while not rospy.is_shutdown():
        try:
            #rospy.logdebug("debug info")
            rospy.loginfo("loginfo")
            # rospy.logwarn("warn_info")
            # rospy.logerr("err_info")
            # rospy.logfatal("fatal_info")
        except Exception as e:
            rospy.loginfo("error:%s", e)
        # rate.sleep()
