#!/usr/bin/env python
#### initialising the libraries
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = {'f':[0,1],'b':[0,-1],'l':[-1,0],'r':[1,0],'s':[0,0]}
g_last_twist = None
g_vel_scales = [0.1,0.1] # defining default velocity
                        

def keys_cb(msg, twist_pub):
   global g_last_twist, g_vel_scales
   if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
    return # unknown key

   vels = key_mapping[msg.data[0]]
   g_last_twist.angular.z = vels[0] * g_vel_scales[0] # scaling to desired vel
   g_last_twist.linear.x = vels[1] * g_vel_scales[1]
   twist_pub.publish(g_last_twist) # subscribing and publishing


if __name__ == '__main__':
  rospy.init_node('keys_to_twist')# initialising the node
  twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)#defining publisher
  rospy.Subscriber('keys', String, keys_cb, twist_pub)# defining subsriber
  g_last_twist = Twist() # initializes to zero
  if rospy.has_param('~linear_scale'): #parameter either from launch file or cl 
    g_vel_scales[1] = rospy.get_param('~linear_scale')
  else:
    rospy.logwarn("linear scale not provided; using %.1f" %\
    g_vel_scales[1])
  if rospy.has_param('~angular_scale'):
    g_vel_scales[0] = rospy.get_param('~angular_scale')
  else:
    rospy.logwarn("angular scale not provided; using %.1f" %\
    g_vel_scales[0])
  rate = rospy.Rate(10) # publishing data at rate of 10 msgs per sec
  

  while not rospy.is_shutdown():
    twist_pub.publish(g_last_twist)
    rate.sleep()
  
