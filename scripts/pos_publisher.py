#!/usr/bin/env python3

import rospy
# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose
#importing the new message from our package
from robotics_lab1.msg import Turtlecontrol
# for radians to degrees conversions
import math

ROTATION_SCALE = 180.0/math.pi

pos_msg = Turtlecontrol()

def pose_callback(data):
	global pos_msg
	# kp and xd
	pos_msg.kp = data.kp
	pos_msg.xd = data.xd
	
	
if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_publisher', anonymous = True)
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, pose_callback)
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, pose_callback)
	# add a publisher with a new topic using the Shortpos message
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		# publish the message
		#pos_pub.publish(pos_msg)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	
