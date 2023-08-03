#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist

	

Int1_value = 0.0
Int2_value = 0.0
Int3_value = 0.0
Int4_value = 0.0
Int5_value = 0.0
Int6_value = 0.0

def callback(data):
	
	global Int1_value,Int2_value,Int3_value,Int4_value
	Int1_value = data.x;
	Int2_value = data.y;
	Int3_value = data.z;
	Int4_value = data.w;

	rospy.loginfo("x: %f", Int1_value)
	rospy.loginfo("y: %f", Int2_value)
	rospy.loginfo("z: %f", Int3_value)
	rospy.loginfo("w: %f", Int4_value)

def funcion():
    global Int1_value,Int2_value,Int3_value,Int4_value,Int5_value,Int6_value
    pub = rospy.Publisher('ej5_random_int_twist', Twist, queue_size=20)
    sub = rospy.Subscriber("ej5_random_int_quat", Quaternion, callback)   

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
	        
        twistmessaje = Twist()
        twistmessaje.linear.x= Int1_value 
        twistmessaje.linear.y= Int2_value 
        twistmessaje.linear.z= Int3_value 
        twistmessaje.angular.x=Int4_value 
        Int5_value = Int1_value+Int2_value+Int3_value+Int4_value;
        twistmessaje.angular.y=Int5_value;
        Int6_value = Int5_value*Int5_value;
        twistmessaje.angular.z=Int6_value 
        pub.publish(twistmessaje)
        rate.sleep()
	    

if __name__ == '__main__':
	rospy.init_node('ej5_cod5_quat_twist_sp', anonymous=True)	
	try:
		funcion()
	except rospy.ROSInterruptException:
		pass