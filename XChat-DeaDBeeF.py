#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  XChat-DeaDBeeF  -  XChat plugin for DeaDBeeF integration
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
__module_description__ = "DeaDBeeF integration in XChat."
__module_version__ = "0.3"
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

def call_deadbeef():
	sleep(5)
	print "DeadBeeF lauched!"
	subprocess.call("deadbeef")

def is_deadbeef_running():
	runningornot = os.popen("ps -e | grep deadbeef-main").read()
	if len(runningornot) == 0:
		print "DeaDBeeF is not running. Launching in 5s..."
		call_deadbeef_thread = Thread(target=call_deadbeef)
		call_deadbeef_thread.start()
	else:
		pass
		
def is_song_loaded():
	loadedornot = os.popen("deadbeef --nowplaying %e").read()
	if "nothing" in loadedornot:
		print "Track loaded!"
	else:
		print "Track resumed!"

def deadbeef_current_song(word, word_eol, userdata):
	is_deadbeef_running()
	read_song = os.popen('deadbeef --nowplaying "%a - %t - %b% (%y) // %@:BITRATE@kbps"').read().strip()
	nickname = "♪ NP @ %s ♪ - " % xchat.get_info("nick")
	announce_song = nickname + str(read_song)
	xchat.command("say "+announce_song)
	return xchat.EAT_ALL
      
def deadbeef_next_song(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --next")
	print "Next track loaded!"
	sleep(0.001) # DeaDBeeF shows the initial track if isn't given some time to update
	read_song = os.popen('deadbeef --nowplaying "%t by %a - from %b (%y)"').read()
	print "You are listening to: %s" % str(read_song)
	return xchat.EAT_ALL
 
def deadbeef_previous_song(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --prev")
	print "Previous track loaded!"
	sleep(0.001) # DeaDBeeF shows the initial track if isn't given some time to update 
	read_song = os.popen('deadbeef --nowplaying "%t by %a - from %b% (%y)"').read()
	print "You are listening to: %s" % str(read_song)
	return xchat.EAT_ALL
 
def deadbeef_play_song(word, word_eol, userdata):
	is_deadbeef_running()
	is_song_loaded()
	os.system("deadbeef --play")
	return xchat.EAT_ALL
 
def deadbeef_pause_song(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --pause")
	print "Current track paused!"
	return xchat.EAT_ALL
	
def deadbeef_stop_song(word, word_eol, userdata):
	is_deadbeef_running()
	os.system("deadbeef --stop")
	print "Current track stopped!"
	return xchat.EAT_ALL
	
if __name__ == '__main__':
	
	is_deadbeef_running()
	
	xchat.hook_command('currentsong',deadbeef_current_song) 
	xchat.hook_command('nextsong',deadbeef_next_song)
	xchat.hook_command('prevsong',deadbeef_previous_song)
	xchat.hook_command('playsong',deadbeef_play_song)
	xchat.hook_command('pausesong',deadbeef_pause_song)
	xchat.hook_command('stopsong',deadbeef_stop_song)
	
	print "XChat-DeaDBeeF %s plugin loaded successfully! - by %s" % (__module_version__,__module_author__)
	print "Protip: use /playsong to play a song or resume playback (if paused)."
