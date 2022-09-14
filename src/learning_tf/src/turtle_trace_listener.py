#! /usr/bin/python3

import rospy
import tf2_ros
import math
import geometry_msgs.msg
if __name__ == "__main__":
    rospy.init_node("turtle_trace_sub")
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)
    rate = rospy.Rate(10)
    cmd = geometry_msgs.msg.Twist()

    pub = rospy.Publisher("/turtle2/cmd_vel",
                          geometry_msgs.msg.Twist, queue_size=1)
    while not rospy.is_shutdown():

        try:
            ts = buffer.lookup_transform(
                'turtle2', 'turtle1', rospy.Time())
            # qtn = [0, 0, ts.transform.rotation.z, ts.transform.rotation.w]
            # ang = tf.transformations.euler_from_quaternion(qtn)
            cmd.linear.x = 0.5*math.sqrt((ts.transform.translation.x)
                                         ** 2+(ts.transform.translation.y)**2)
            cmd.angular.z = 4 * \
                math.atan2(ts.transform.translation.y,
                           ts.transform.translation.x)
            # 时间戳不相同！！
            # cmd.angular.z = ang[2]
            # rospy.loginfo(ts)
            # rospy.loginfo(cmd)
            pub.publish(cmd)
            rate.sleep()
        except Exception as e:
            rospy.loginfo("error:%s", e)
