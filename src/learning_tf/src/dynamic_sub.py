#! /usr/bin/python3
# # transform listener set
# buffer = tf2_ros.Buffer()
# sub = tf2_ros.TransformListener(buffer)

import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs

if __name__ == "__main__":
    rospy.init_node("dynamic_sub")

    #
    pub = rospy.Publisher("/point", tf2_geometry_msgs.PointStamped)
    # transform listener set
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)

    # a point transform in turtle1
    ps = tf2_geometry_msgs.PointStamped()

    # time must set
    ps.header.stamp = rospy.Time()
    ps.header.frame_id = "turtle1"
    ps.point.x = 1
    ps.point.y = 1
    ps.point.z = 0

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # solve the error
        try:
            ps_out = buffer.transform(ps, "world")
            pub.publish(ps_out)
            rospy.loginfo("print( %.2f, %.2f, %.2f),frame :%s",
                          ps_out.point.x,
                          ps_out.point.y,
                          ps_out.point.z,
                          ps_out.header.frame_id
                          )
            rate.sleep()
        except Exception as e:
            rospy.loginfo("error:%s", e)
