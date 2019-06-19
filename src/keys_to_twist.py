#!/usr/bin/env python
##################### initialising the libraries and msgs we want to use 


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
#########################################
## initiating the dictionary corresponding to key we press and twist we want that is linear movement of wheels in x direction and angular in z direction 


key_mapping = {'f':[0,1],'b':[0,-1],'l':[-1,0],'r':[1,0],'s':[0,0]}

#### callback function that publish the twist corresponding to the key subscribed 


def keys_cb(msg,twist_pub):
 if len(msg.data) == 0 or not key_mapping.has_key(msg.data):
   return 
 vels = key_mapping[msg.data[0]]
 t = Twist()
 t.angular.z = vels[0]
 t.linear.x = vels[1]
 twist_pub.publish(t)


# initiating the node ,publisher and subscriber 
if __name__== '__main__':
  rospy.init_node('key_to_twist')
  twist_pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
  rospy.Subscriber('keys',String,keys_cb,twist_pub)
  rospy.spin()
