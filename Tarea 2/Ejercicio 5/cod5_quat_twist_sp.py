#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist

rospy.init_node('cod5_quat_twist_sp', anonymous=True)	

Int1_value = 0
Int2_value = 0
Int3_value = 0
Int4_value = 0
Int5_value = 0
Int6_value = 0

def callback(data):
	#rospy.loginfo("I heard %d", data.x) #como print
	global Int1_value,Int2_value,Int3_value,Int4_value,Int5_value,Int6_value
	Int1_value = data.x;
	Int2_value = data.y;
	Int3_value = data.z;
	Int4_value = data.w;

	rospy.loginfo("x: %f", Int1_value)
	rospy.loginfo("y: %f", Int2_value)
	rospy.loginfo("z: %f", Int3_value)
	rospy.loginfo("w: %f", Int4_value)

pub = rospy.Publisher('random_int_twist', Quaternion, queue_size=10)
sub = rospy.Subscriber("random_int_quat", Quaternion, callback)   
Int5_value = Int1_value+Int2_value+Int3_value+Int4_value;
Int6_value = Int5_value*Int5_value;

rate = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():
    twistmessaje = Twist()
    twistmessaje.linear.x= Int1_value 
    twistmessaje.linear.y= Int2_value 
    twistmessaje.linear.z= Int3_value 
    twistmessaje.angular.x=Int4_value 
    twistmessaje.angular.y=Int5_value
    twistmessaje.angular.z=Int6_value 
    pub.publish(twistmessaje)
    print(twistmessaje)
    rate.sleep()