/*******************************************************************************
* Copyright 2016 ROBOTIS CO., LTD.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*******************************************************************************/

/* Authors: Yoonseok Pyo, Leon Jung, Darby Lim, HanCheol Cho, Gilbert */
#include <ros.h>
#include "turtlebot3.h"

#include <geometry_msgs/Twist.h>
ros::NodeHandle nh;
float linearm=0;
float angularm=0;


Turtlebot3MotorDriver motor_driver;

bool motor_driver.readEncoder(int32_t left,int32_t right);
void messageCb(const geometry_msgs::Twist& twist)
{
  const float linearm=twist.linear.x;
  const float angularm=twist.angular.z;   
  float goal_velocity[2]={linearm,angularm};  
  motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb);



/*******************************************************************************
* Setup function
*******************************************************************************/
void setup()
{
  
  motor_driver.init(NAME);
  nh.initNode();
  nh.subscribe(sub);
  Serial.begin(115200);
}

void loop()
{
 
 nh.spinOnce();
 Serial.println(left);
 delay(100);
}







