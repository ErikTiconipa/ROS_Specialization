#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('float_sub', anonymous=True)	

float_value=0

#se crea la funcion para recibir el mensaje del topico
def callback(data):	
    global float_value
    float_value=data.data
    rospy.loginfo("Yo encuche %f", float_value)
    

# se suscribe al topico
sub = rospy.Subscriber("random_float", Float64, callback)
# el codigo cod2_float_pub.py publica al topico 'random_float'

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo