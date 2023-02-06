#!/usr/bin/env python3

import rospy
# read turtlesim/Pose messages
from turtlesim.msg import Pose
# read the new message from our package
from robotics_lab1.msg import Turtlecontrol
# read twist messages
from geometry_msgs.msg import Twist

#calls Pose and Turtlecontrol.msg
control_msg = Turtlecontrol()
pos_msg = Pose()

def pose_callback(data):
	global pos_msg
	
	# gets current position of node
	pos_msg.x = data.x
	


def control_callback(data):
	global control_msg
	
	# gets xd and kp from Turtlecontrol.msg
	control_msg.xd = data.xd
	control_msg.kp = data.kp
	
	
if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_publisher', anonymous = True)
	# add subscribers to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, control_callback)
	# adding a publisher with a new topic
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	
	# initialize Twist
	twist = Twist()

	while not rospy.is_shutdown():
		# sets linear velocity
		twist.linear.x = control_msg.kp*(control_msg.xd - pos_msg.x)
		
		# publish the message using twist
		cmd_pub.publish(twist)
		
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	
