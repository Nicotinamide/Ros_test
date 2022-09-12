#! /usr/bin/python3

import rospy
import tf2_ros
import tf
from turtlesim.msg import Pose
from geometry_msgs.msg import TransformStamped


def callback(msg):
    # print(msg)
    # create pub
    pub = tf2_ros.TransformBroadcaster()
    # rebuild data class = TransformStamped
    ps = TransformStamped()
    ps.header.stamp = rospy.Time.now()
    ps.header.frame_id = "world"
    ps.child_frame_id = "turtle1"
    # translation
    ps.transform.translation.x = msg.x
    ps.transform.translation.y = msg.y
    ps.transform.translation.z = 0
    # ps.transform.rotation = tf.transformations.quaternion_from_euler(
    #     msg.theta, 0, 0)
    # rotation by quaternion
    qtn = tf.transformations.quaternion_from_euler(0, 0, msg.theta)

    ps.transform.rotation.x = qtn[0]
    ps.transform.rotation.y = qtn[1]
    ps.transform.rotation.z = qtn[2]
    ps.transform.rotation.w = qtn[3]
    # print(ps)
    # publish the transform
    pub.sendTransform(ps)


if __name__ == "__main__":
    rospy.init_node("dynamic_pub")
    # subscribe topic of pose
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback)
    # spin? or while?
    rospy.spin()
