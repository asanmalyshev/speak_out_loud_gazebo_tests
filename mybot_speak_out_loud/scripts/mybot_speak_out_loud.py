#!/usr/bin/env python
# coding: utf-8

import rospy
import random

from speak_out_loud.msg import SpeakGoal, Priority
from fiducial_msgs.msg import FiducialArray

class MybotVoice(object) :
    """
    Simple node to send text with priority
    """

    def __init__(self):
        rospy.logwarn("turtleSay node")

        self.goal = SpeakGoal()
        self.goal.sender_node = rospy.get_name()
        self.goal.priority = Priority.TEXT 

        self.goal_debug = SpeakGoal()
        self.goal_debug.sender_node = rospy.get_name()
        self.goal_debug.priority = Priority.PROGRESS

        self.load_params()
        self.aruco_num = -1

        rospy.Subscriber("/mybot/fiducial_vertices", FiducialArray, self.aruco_detect_cb)
        self._pub = rospy.Publisher("/speak_out_loud_texts", SpeakGoal, queue_size=1)
        self._pub_debug = rospy.Publisher("/speak_out_loud_texts_debug", SpeakGoal, queue_size=1)
        rospy.Timer(rospy.Duration(5), self.debug_cb, oneshot=False)
        
        rospy.on_shutdown(self.shutdown)
        rospy.spin()

    def load_params(self):
        pass

    def aruco_detect_cb(self, msg):

        l = len(msg.fiducials)

        if self.aruco_num != l:
            self.aruco_num = l
            self.goal.text = "В дали виднеется {} аруко".format(self.aruco_num)
            self._pub.publish(self.goal)

    def debug_cb(self, event):
        r = random.randrange(0,3)
        if r == 0:
            self.goal_debug.text = "The weather is fine"
        elif r == 1:
            self.goal_debug.text = "Батарея полная"
        elif r == 2:
            self.goal_debug.text = "My name is mybot"
        elif r == 3:
            self.goal_debug.text = "У меня уже колёса отваливаются кататься"


        self._pub_debug.publish(self.goal_debug)

    def shutdown(self):
        rospy.logwarn("mybotVoice node is closed")

if __name__ == '__main__':
    try:
        rospy.init_node('mybotVoice')
        rospy.logwarn("Press Ctrl+C to shutdown node")
        mybotVoice = MybotVoice()

    except rospy.ROSInterruptException:
        pass

