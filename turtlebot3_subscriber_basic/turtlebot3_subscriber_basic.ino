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
#include <std_msgs/String.h>
ros::NodeHandle nh;
String var;


void messageCb(const std_msgs::String& msg)
{
  var=msg.data;
 
  if(var == "f")
   forward();
  else if(var == "b")
   backward();
  else if(var == "l")
   leftward();
  else if(var == "r")
   rightward();
  else
   stops(); 
     
}

ros::Subscriber<std_msgs::String> sub("cmd_vel", &messageCb);

Turtlebot3MotorDriver motor_driver;

/*******************************************************************************
* Setup function
*******************************************************************************/
void setup()
{
  Serial.begin(115200);
  motor_driver.init(NAME);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  //motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);
  nh.spinOnce();
  delay(200);
}
void forward()
{
  Serial.println("ff");
  float goal_velocity[2] = {0.5,0};
  motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);
  
}
void stops()
{ 
  Serial.println("ss");
  float goal_velocity[2] = {0.0,0};
  motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);
}
void backward()
{
  Serial.println("bb");
  float goal_velocity[2] = {-0.5,0};
  motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);
}
void leftward()
{
  Serial.println("ll");
  float goal_velocity[2] = {0,2};
  motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);

}
void rightward()
{
  Serial.println("rr");
  float goal_velocity[2] = {0,-2};
  motor_driver.controlMotor(WHEEL_RADIUS, WHEEL_SEPARATION, goal_velocity);
}







