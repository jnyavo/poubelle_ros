#!/usr/bin/env python

import rospy
from projet_poubelle.msg import Poubelle
from std_msgs.msg import Bool

ETATS = ("utilisable","pleine")

class publish_poubelle:
	def __init__(self,nom_topic,id_poubelle):
		self.pub= rospy.Publisher(nom_topic,Poubelle, queue_size=10)
        	rospy.init_node('talker')
		self.id_poubelle = 1
        	self.rate = rospy.Rate(15)
		self.etat = False
       
	def run(self):
		
		#pub= rospy.Publisher("poubelles_etat",Poubelle, queue_size=10)
		my_msg = Poubelle()
                my_msg.id_poubelle.data = 1
                my_msg.etat.data = ETATS[self.etat]
		
		while not rospy.is_shutdown():
			self.listener(Bool,'button_state')
			#rospy.loginfo(my_msg)
			my_msg.etat.data = ETATS[self.etat]
			self.pub.publish(my_msg)
			self.rate.sleep()
				
			
			

				
			


	def callback(self,data):
		if (data):
			self.etat = data.data
			

	def listener(self,type_msg,topic):	
		rospy.Subscriber(topic,type_msg,self.callback)
		


if __name__ == '__main__':
	try:
		talk = publish_poubelle("etat_poubelles",1)
		talk.run()
	except rospy.ROSInterruptException:
		pass
