#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  XChat-DeaDBeeF  -  XChat/HexChat script for DeaDBeeF integration
#
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004
#
#  Copyright (C) 2013 iceTwy <nerorush23@gmail.com>
#
#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#
#

__module_name__ = "XChat-DeaDBeeF"
__module_description__ = "DeaDBeeF integration in XChat and HexChat."
__module_version__ = "0.3"
__module_deadbeef_version__ = "0.5.6"

__module_author__ = "Trixar_za & iceTwy"
__module_credits__ = ["Trixar_za", "iceTwy"]
__module_license__ = "WTFPL"
__module_maintainer__ = "iceTwy"
__module_email__ = "nerorush23@gmail.com"
__module_status__ = "Released"

############################
import xchat                 
import os                    
import subprocess            

from threading import Thread 
from time import sleep      
############################

def check_deadbeef_version():
	read_version = os.popen('deadbeef --version').read()
	if __module_deadbeef_version__ in read_version:
		pass
	else:
		print "Your DeaDBeeF version is outdated.\nPlease update to DeaDBeeF %s!" % __module_deadbeef_version__
		
def execute_deadbeef():
	calldb = subprocess.Popen("deadbeef", stdout=subprocess.PIPE)
	calldb.communicate()[0]
	exitcode = calldb.poll()
	if exitcode == 0:
		print "DeaDBeeF closed!"
	else:
		pass

def call_deadbeef_user(word, word_eol, userdata):
	runningornot = os.popen("ps -e | grep deadbeef-main").read()
	if len(runningornot) == 0:
		print "DeadBeeF launched!"
		calldb_user_thread = Thread(target=execute_deadbeef)
		calldb_user_thread.start()
	else:
		print "DeaDBeeF is already open!"
	return xchat.EAT_ALL
	
def call_deadbeef_script():
	sleep(5) # Execute 5s later to avoid bothering the user when XChat/HexChat launches.
	print "DeadBeeF launched!"
	execute_deadbeef()

def is_deadbeef_running(): 
	runningornot = os.popen("ps -e | grep deadbeef-main").read()
	if len(runningornot) == 0:
		print "DeaDBeeF is not running. Launching in 5s..."
		call_deadbeef_thread = Thread(target=call_deadbeef_script)
		call_deadbeef_thread.start()
	else:
		pass
			
def is_track_loaded():
	loadedornot = os.popen("deadbeef --nowplaying %e").read()
	if "nothing" in loadedornot:
		print "Track loaded!"
	else:
		print "Track resumed/reset!"

def deadbeef_current_track(word, word_eol, userdata):
	is_deadbeef_running()
	read_track = os.popen('deadbeef --nowplaying "%a - %t - %b% (%y) // %@:BITRATE@kbps"').read().strip()
	nickname = "♪ NP @ %s ♪ - " % xchat.get_info("nick")
	announce_track = nickname + str(read_track)
	xchat.command("say "+announce_track)
	return xchat.EAT_ALL
      
def deadbeef_next_track(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --next")
	print "Next track loaded!"
	sleep(0.05) # Give some time to DeaDBeeF to update accurately 
	read_track = os.popen('deadbeef --nowplaying "%t by %a - from %b (%y)"').read()
	print "You are listening to: %s" % str(read_track)
	return xchat.EAT_ALL
 
def deadbeef_previous_track(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --prev")
	print "Previous track loaded!"
	sleep(0.05) # Give some time to DeaDBeeF to update accurately 
	read_track = os.popen('deadbeef --nowplaying "%t by %a - from %b% (%y)"').read()
	print "You are listening to: %s" % str(read_track)
	return xchat.EAT_ALL
 
def deadbeef_play_track(word, word_eol, userdata):
	is_deadbeef_running()
	is_track_loaded()
	os.system("deadbeef --play")
	return xchat.EAT_ALL
 
def deadbeef_pause_track(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --pause")
	print "Current track paused!"
	return xchat.EAT_ALL
	
def deadbeef_stop_track(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --stop")
	print "Current track stopped!"
	return xchat.EAT_ALL
	
if __name__ == '__main__':
	
	print "XChat-DeaDBeeF %s plugin loaded successfully! - by %s" % (__module_version__,__module_author__)
	print "Protip: using /play when the track is playing resets the track."
	
	is_deadbeef_running() #=> call_deadbeef_script in new thread => execute_deadbeef() in the same thread.
	check_deadbeef_version()
	

#Launch DeaDBeeF
	xchat.hook_command('deadbeef',call_deadbeef_user) #=>  execute_deadbeef() in a new thread.
    
#Display the current track (chose one)
	#xchat.hook_command('currenttrack',deadbeef_current_track) 
	#xchat.hook_command('nowplaying',deadbeef_current_track)
	xchat.hook_command('np',deadbeef_current_track)

#Play, pause, stop track
	xchat.hook_command('dbplay',deadbeef_play_track)
	xchat.hook_command('dbpause',deadbeef_pause_track)
	xchat.hook_command('dbstop',deadbeef_stop_track)
	
#Skip to next or previous track
	xchat.hook_command('dbnext',deadbeef_next_track)
	xchat.hook_command('dbprev',deadbeef_previous_track)
