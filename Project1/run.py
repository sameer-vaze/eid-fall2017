#!/usr/bin/env python
"""run.py: This is the python code to run the DHT22 sensor.

The interface has the following interactive elements:

1. Refresh: To update the values of the temperature and humidity from the DHT22 sensor
2. Set Alarm: There are two alarms that cater to the temperature and humidity values
3. Quit: To exit the UI

The non-interactive elements include:

1. Label for temperature
2. Label for humidity
3. Set alarm value for temperature
4. Set alarm value for humidity
5. System time display

"""

import sys
import os
import time
import Adafruit_DHT

from PyQt4 import QtCore, QtGui
from Project1 import Ui_Form

__author__ = "Sameer Vaze"
__copyright__ = "Copyright (C) 2017 by Sameer Vaze"
#
# Redistribution, modification or use of this software in source or binary
# forms is permitted as long as the files maintain this copyright. Users are
# permitted to modify this and use it to learn about the field of embedded
# software. Sameer Vaze the University of Colorado are not liable for any 
# misuse of this material.
#

set_clear = True 									#Global flags for set vs clear for both entry fields
set_clear_2 = True
check_alarm = float(500)							#Gobal flags for the alarm values, set to a very large value by default to prevent issues
check_alarm_2 = float(500)

class Main(QtGui.QMainWindow):						#class definition and declaration for the UI window
	def __init__(self):								#constructor for the window class
		super(Main, self).__init__()

		# build ui
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(1000)
		self.timer1 = QtCore.QTimer(self)
		self.timer1.setInterval(5000)
		self.timer.timeout.connect(self.set_current_time)
		self.timer1.timeout.connect(self.get_t_h)
		self.timer.start()
		self.timer1.start()
		self.ui.qui.clicked.connect(exit)
		self.ui.ref.clicked.connect(self.get_t_h)
		self.ui.ala.clicked.connect(self.set_alarm)
		self.ui.ala_2.clicked.connect(self.set_alarm_2)

	def set_current_time(self):														#Function to set up current time
		self.ui.tim_v.setText(QtCore.QDateTime.currentDateTime().toString())

	def get_t_h(self):																#Function to get time and humidity
		humidity, temperature = Adafruit_DHT.read_retry(22, 4)
		self.ui.hum_v.setText(str(humidity))										#Set value of temperature and humidity
		self.ui.temp_v.setText(str(temperature))
		
		if temperature > check_alarm:												#Alarm for temperature
			self.ui.temp_v.setStyleSheet('color : red')
		else:
			self.ui.temp_v.setStyleSheet('color : black')

		if humidity > check_alarm_2:												#Alarm for humidity
			self.ui.hum_v.setStyleSheet('color : red')
		else:
			self.ui.hum_v.setStyleSheet('color : black')


	def set_alarm(self):															#Set alarm for temperature
		global set_clear
		global check_alarm

		if set_clear:
			alarm_val = self.ui.ala_enter.text()
			check_alarm = float(alarm_val)
			self.ui.t_ala_v.setText(str(alarm_val))
			self.ui.ala_enter.clear()
			self.ui.ala.setText("Clear T Alarm")
			set_clear = False
		else:
			alarm_val = self.ui.ala_enter.text()
			check_alarm = float(500)
			self.ui.t_ala_v.setText(str(0.00))
			self.ui.ala.setText("Set T Alarm")
			set_clear = True

	def set_alarm_2(self):															#Set alarm for humidity
		global set_clear_2
		global check_alarm_2

		if set_clear_2:
			alarm_val_2 = self.ui.ala_enter_2.text()
			check_alarm_2 = float(alarm_val_2)
			self.ui.h_ala_v.setText(str(alarm_val_2))
			self.ui.ala_enter_2.clear()
			self.ui.ala_2.setText("Clear H Alarm")
			set_clear_2 = False
		else:
			alarm_val_2 = self.ui.ala_enter_2.text()
			check_alarm_2 = float(500)
			self.ui.h_ala_v.setText(str(0.00))
			self.ui.ala_2.setText("Set H Alarm")
			set_clear_2 = True


if __name__ == '__main__':															#Main function
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())
