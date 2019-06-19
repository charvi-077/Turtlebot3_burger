#!/usr/bin/env python
'''#initialising the libraries and msgs we want to use 
### now in this program data will publish at 10 hz also we can set the velocity parameters in the launch file or by command line"
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
#########################################
## initiating the dictionary corresponding to key we press and twist we want that is linear movement of wheels in x direction and angular in z direction 


key_mapping = {'f':[0,1],'b':[0,-1],'l':[-1,0],'r':[1,0],'s':[0,0]}

#### callback function that publish the twist corresponding to the key subscribed 

t = None
g_vel_scales=[0.5,0.5]
def keys_cb(msg,twist_pub):
 global t
 if len(msg.data) == 0 or not key_mapping.has_key(msg.data):
   return
 vels = key_mapping[msg.data[0]]

 t.angular.z = vels[0] * g_vel_scales[0]
 t.linear.x = vels[1] * g_vel_scales[1]



# initiating the node ,publisher and subscriber 
if __name__== '__main__':
  rospy.init_node('key_to_twist')
  twist_pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
  rospy.Subscriber('keys',String,keys_cb,twist_pub)
  rate = rospy.Rate(10)
  t = Twist() # initialise with zero
  if rospy.has_param('~linear_scale'):
       g_vel_scales[1] = rospy.get_param('~linear_scale')
  else:
       rospy.logwarn("linear scale not provided")
  if rospy.has_param('~angular_scale'):
      g_vel_scales[0] = rospy.get_param('~angular_scale')
  else:
       rospy.logwarn("angular scale not provided")
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    twist_pub.publish(t)
    rate.sleep()
'''  

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = {'f':[0,1],'b':[0,-1],'l':[-1,0],'r':[1,0],'s':[0,0]}
g_last_twist = None
g_vel_scales = [0.1,0.1]

def keys_cb(msg, twist_pub):
  global g_last_twist, g_vel_scales
  if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
    return # unknown key
  vels = key_mapping[msg.data[0]]
  g_last_twist.angular.z = vels[0] * g_vel_scales[0]
  g_last_twist.linear.x = vels[1] * g_vel_scales[1]
  twist_pub.publish(g_last_twist)
if __name__ == '__main__':
  rospy.init_node('keys_to_twist')
  twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  rospy.Subscriber('keys', String, keys_cb, twist_pub)
  g_last_twist = Twist() # initializes to zero
  if rospy.has_param('~linear_scale'):
    g_vel_scales[1] = rospy.get_param('~linear_scale')
  else:
    rospy.logwarn("linear scale not provided; using %.1f" %\
    g_vel_scales[1])
  if rospy.has_param('~angular_scale'):
    g_vel_scales[0] = rospy.get_param('~angular_scale')
  else:
    rospy.logwarn("angular scale not provided; using %.1f" %\
    g_vel_scales[0])
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    twist_pub.publish(g_last_twist)
    rate.sleep()
  
