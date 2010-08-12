#encoding: utf-8
import random, time, os
import writeLED

def Test():
	print "Detta är test taggen"
def chrome():
	print "startar chrome.."
	os.system("google-chrome &")

def Alarm_off():
	os.system("killall mplayer")
	writeLED.writeLED_PWM("r", 0)
	writeLED.writeLED_PWM("g", 0)
	writeLED.writeLED_PWM("b", 0)

def Light_random():
	writeLED.writeLED_PWM("r", random.randint(0,255))
	writeLED.writeLED_PWM("g", random.randint(0,255))
	writeLED.writeLED_PWM("b", random.randint(0,255))
