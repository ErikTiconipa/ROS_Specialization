#!/usr/bin/env python3
# --------------publicador-suscriptor de Float64--------------
# el codigo escucha al topico 'random_float'
# Y publica al topico 'random_float_pub' el cuadrado de los valores que lleguen
import rospy
from std_msgs.msg import Float64

rospy.init_node('cod2_float_sp', anonymous=True)
float_value=0.0

def callback(data):
	global float_value	
	float_value=data.data
	rospy.loginfo("Yo encuche en topic random_float : %f", float_value)

pub = rospy.Publisher('random_float_pub', Float64, queue_size=10)
sub = rospy.Subscriber("random_float", Float64, callback)

rate = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():
	valor=float_value*float_value
	pub.publish(valor)
	rate.sleep()