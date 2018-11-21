#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    index = 0
    while not rospy.is_shutdown():
        course_list=["MIT",
        "edX",
        "Coursera",
        "PVTuts",
        "Udacity",
        "Udemy",
        "CodeCamp",
        "KhanAcademy",
        "Codecademy",
        "OpenCourser"]
        #hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(course_list)
        pub.publish(course_list[index % 10])
        rate.sleep()
        index+=1

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
