#! /usr/bin/python3

import rospy
import tf
import tf2_ros
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from geometry_msgs.msg import TransformStamped
import sys


def callback(msg, turtlename):
    # tf下broadcaster需要发送坐标
    tw = TransformStamped()
    '''
    rosmsg show geometry_msgs/TransformStamped 
    std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
    string child_frame_id
    geometry_msgs/Transform transform
    geometry_msgs/Vector3 translation
        float64 x
        float64 y
        float64 z
    geometry_msgs/Quaternion rotation
        float64 x
        float64 y
        float64 z
        float64 w

    '''
    tw.header.stamp = rospy.Time.now()
    tw.header.frame_id = "world"
    tw.child_frame_id = turtlename
    tw.transform.translation.x = msg.x
    tw.transform.translation.y = msg.y
    tw.transform.translation.z = 0
    # TransformStamped中姿态是以四元数形式组织，quaternion_from_euler(ai, aj, ak, axes='sxyz')，需要在空间中理解...
    qtn = tf.transformations.quaternion_from_euler(0, 0, msg.theta)
    tw.transform.rotation.x = qtn[0]
    tw.transform.rotation.y = qtn[1]
    tw.transform.rotation.z = qtn[2]
    tw.transform.rotation.w = qtn[3]
    # tf2和tf下TransformBroadcaster功能不相同
    br = tf2_ros.TransformBroadcaster()
    br.sendTransform(tw)


if __name__ == "__main__":
    rospy.init_node("turtle_trace_pub")
    print(len(sys.argv))
    if len(sys.argv) != 4:
        rospy.loginfo("参数错误")
        sys.exit(1)
    else:
        turtlename = sys.argv[1]

    # rospy.wait_for_service("/spawn")
    # try:
    #     spawn = rospy.ServiceProxy("/spawn", Spawn)
    #     spawn.call(1, 1, 0, 'turtle2')
    # except:
    #     pass

    rate = rospy.Rate(10)

    sub = rospy.Subscriber('/%s/pose' % turtlename, Pose,
                           callback, callback_args=turtlename)
    rospy.spin()
    # while not rospy.is_shutdown():
    #     sub1 = rospy.Subscriber('/turtle1/pose', Pose,
    #                             callback, callback_args='turtle1')
    #     sub2 = rospy.Subscriber('/turtle2/pose', Pose,
    #                             callback, callback_args='turtle2')
    #     rate.sleep()
    '''

    Type: geometry_msgs/Twist
    rosmsg show geometry_msgs/Twist
    geometry_msgs/Vector3 linear
    float64 x
    float64 y
    float64 z
    geometry_msgs/Vector3 angular
    float64 x
    float64 y
    float64 z

    Type: turtlesim/Pose
    rostopic type /turtle1/pose | rosmsg show 
    float32 x
    float32 y
    float32 theta
    float32 linear_velocity
    float32 angular_velocity
    '''
