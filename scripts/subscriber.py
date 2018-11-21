#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

def callback(data):
    courses = {
        "MIT":"Many years ago, when I was struggling through a Linear Algebra course in college, MIT OCW came to my rescue. Complete courses are available online for free, and you can go through them at your own pace.",
        "edX":"edX is a provider of free college-level online courses, jointly spearheaded by MIT and Harvard University. Not only are the courses available without charge, the organization itself is non-profit, so you can rest easy knowing that you won’t be exploited by ulterior motives",
        "Coursera":"Coursera is another free online course platform, except this one’s backed by Stanford University and venture capitalists. Coursera collaborates with various universities and organizations to provide their courses, and earns revenue through its Certificate programs.",
        "PVTuts":"PVTuts is a free online repository of video courses for learning programming languages. It hasn’t been updated since 2013, but the video library is still a great resource for newbies. Just know that these courses are strictly about language syntax and nothing else.",
        "Udacity":"Udacity is yet another online course platform, but unlike MIT OCW, edX, and Coursera, Udacity strictly focuses on topics related to programming, data science, and engineering. No math, no social sciences, no humanities. It’s all about technology, and arguably better for it.",
        "Udemy":"Udemy is an online education marketplace where anyone can create (and even sell) their own courses for others to consume. This is quite the double-edged sword: it allows skilled folks to share their knowledge without an education degree, but you have to wade through a lot of crap to find it.",
        "CodeCamp":"If your goal is to become a proficient web developer, whether front-end or back-end, then I highly recommend either Free Code Camp (which teaches HTML, CSS, JavaScript, and React) or The Odin Project (which teaches HTML, CSS, JavaScript, Ruby on Rails).",
        "KhanAcademy":"Khan Academy is one of the internet’s greatest treasures. This non-profit education platform has been a wonderful source of free education for the past decade, and it’s only getting better. Want to learn Calculus? Biology? World History? How to do your taxes or invest your money? It’s all here.",
        "Codecademy":"Codecademy is a series of interactive online courses that aim to teach you the basics of a handful of programming languages and frameworks. Each course is a gamified, step-by-step process that holds your hand all the way from beginning to end.",
        "OpenCourser":"OpenCourser isn’t an education platform like the other sites listed above. Rather, it’s a search engine that aggregates thousands of free online courses from around the web and brings them to your fingertips."
   
        }
    x=courses[data.data]
    rospy.loginfo("\ncourse- %s"+" \nDescription-"+x, data.data)
    
def listener():

    
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
