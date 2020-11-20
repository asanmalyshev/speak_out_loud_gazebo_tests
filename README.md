# ROS speak_out_loud package. Some tests in Gazebo 
Repo for ROS speak_out_loud package tests.

Main repo: 
https://github.com/asanmalyshev/speak_out_loud

## Installation
Before launching:
* follow main repo instruction to install ROS package;
* download repo with tests in your workspace:
```shell
cd ~/catkin_ws/src
git clone https://github.com/asanmalyshev/speak_out_loud_gazebo_tests
```
* add gazebo model directory (speak_out_loud_gazebo_test/mybot_gazebo/models) in bashrc file.
```shell
echo "export GAZEBO_MODEL_PATH=~/catkin_ws/src/speak_out_loud_gazebo_test/mybot_gazebo/models:$GAZEBO_MODEL_PATH" >> ~/.bashrc
```
* build tests with catkin build/catkin_make
```shell
catkin build mybot*
```
or
```shell
catkin_make
```
* source bashrc:
```shell
source ~/.bashrc
```

## Launching

### ArUro detection
```shell
roslaunch mybot_speak_out_loud mybot_speak_out_loud.launch 
```
Drive a cart with 2D Nav Goal in rviz. While driving, the cart will say how many arUcos it recognizes.
```
В дали виднеется N аруко
```
Text is said only when arUcos number is changed.

### ArUro detection debug mode
```shell
roslaunch mybot_speak_out_loud mybot_speak_out_loud.launch debug:=true
```
In that mode additional debug info is said. 
Debug info is one of following phrases which is said once in 5 sec.
```
The weather is fine
Батарея полная
My name is mybot
У меня уже колёса отваливаются кататься
```

