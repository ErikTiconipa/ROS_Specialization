#!/usr/bin/env python3
# --------------publicador de Point -suscriptor de Int32--------------

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Point

int_value_1=0
int_value_2=0
int_value_3=0
 
#se crea la funcion para recibir el mensaje del topico
def callback1(data):
	global int_value_1	
	int_value_1=data.data
	rospy.loginfo("I heard canal 1 %d", int_value_1)	

#se crea la funcion para recibir el mensaje del topico
def callback2(data):
	global int_value_2	
	int_value_2=data.data
	rospy.loginfo("I heard canal 2 %d", int_value_2)	

def funcion():
	# se crea el publicador
	pub = rospy.Publisher('ej5_random_int_point',  Point, queue_size=10)
	# se suscribe al topico
	sub = rospy.Subscriber("ej5_random_int_1", Int32, callback1) 
	# publicar a floatsub desde terminal con: 
	# rostopic pub /random_int_1 std_msgs/Int32 "data: 4"
	sub = rospy.Subscriber("ej5_random_int_2", Int32, callback2) 
	# publicar a floatsub desde terminal con: 
	# rostopic pub /random_int_2 std_msgs/Int32 "data: 4"

	rate = rospy.Rate(1) # 1hz --> 1s
	while not rospy.is_shutdown():
		int_value_3=int_value_1+int_value_2

		pointmessaje = Point(int_value_1, int_value_2, int_value_3)
		pub.publish(pointmessaje)
		rate.sleep() # delay de 1s


if __name__ == '__main__':
	rospy.init_node('ej5_cod3_int_point_sp', anonymous=True)	
	try:
		funcion()
	except rospy.ROSInterruptException:
		pass