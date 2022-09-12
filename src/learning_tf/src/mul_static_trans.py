#! /usr/bin/python3

import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
import tf

if __name__ == "__main__":
    rospy.init_node("mul_trans")

    #
    pub = rospy.Publisher("/point", tf2_geometry_msgs.PointStamped)
    # transform listener set
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)

    # a point transform in turtle1
    ps = tf2_geometry_msgs.PointStamped()

    # time must set
    ps.header.stamp = rospy.Time()
    ps.header.frame_id = "son1"
    ps.point.x = 1
    ps.point.y = 1
    ps.point.z = 0

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # solve the error
        try:
            # ts = TransformStamped()

            ts = buffer.lookup_transform("son2", "son1", rospy.Time())
            eular = tf.transformations.euler_from_quaternion([ts.transform.rotation.x,
                                                             ts.transform.rotation.y,
                                                             ts.transform.rotation.z,
                                                             ts.transform.rotation.w]
                                                             )
            ps_out = buffer.transform(ps, "son2")
            pub.publish(ps_out)
            rospy.loginfo("print( %.2f, %.2f, %.2f),frame :%s",
                          ps_out.point.x,
                          ps_out.point.y,
                          ps_out.point.z,
                          ps_out.header.frame_id
                          )
            rospy.loginfo("relative %.02f,%.02f,%.02f,%.02f,%.02f,%.02f,father frame:%s",
                          ts.transform.translation.x,
                          ts.transform.translation.y,
                          ts.transform.translation.z,
                          #   ts.transform.rotation.x,
                          #   ts.transform.rotation.y,
                          #   ts.transform.rotation.z,
                          eular[0],
                          eular[1],
                          eular[2],
                          ts.header.frame_id
                          )
            rate.sleep()
        except Exception as e:
            rospy.loginfo("error:%s", e)
