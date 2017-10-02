import sys
import os
import time
import Adafruit_DHT

from PyQt4 import QtCore, QtGui
from Project1 import Ui_Form

set_clear = True
set_clear_2 = True
check_alarm = float(500)
check_alarm_2 = float(500)

class Main(QtGui.QMainWindow):
	def __init__(self):
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

	def set_current_time(self):
		self.ui.tim_v.setText(QtCore.QDateTime.currentDateTime().toString())

	def get_t_h(self):
		humidity, temperature = Adafruit_DHT.read_retry(22, 4)
		self.ui.hum_v.setText(str(humidity))
		self.ui.temp_v.setText(str(temperature))
		if temperature > check_alarm:
			self.ui.temp_v.setStyleSheet('color : red')
		else:
			self.ui.temp_v.setStyleSheet('color : black')

		if humidity > check_alarm_2:
			self.ui.hum_v.setStyleSheet('color : red')
		else:
			self.ui.hum_v.setStyleSheet('color : black')


	def set_alarm(self):
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

	def set_alarm_2(self):
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


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())
