# -*- coding: utf-8 -*-
#
#  XChat-DeaDBeeF  -  XChat/HexChat script for DeaDBeeF integration
#  Python 2 version
#
#  Unless indicated otherwise, files from the XChat-DeaDBeeF project 
#  are licensed under the WTFPL version 2. Full license information
#  for the WTFPL version 2 can be found in the LICENSE.txt file.
#

__module_name__ = "XChat-DeaDBeeF"
__module_author__ = "iceTwy"
__module_description__ = "DeaDBeeF integration in XChat and HexChat."
__module_version__ = "1.0"

############################
import xchat              
import subprocess            

from threading import Thread 
from time import sleep      
############################
	
def execute_deadbeef():
	calldb = subprocess.Popen("deadbeef", shell=True, stdout=subprocess.PIPE)
	calldb.communicate()[0]
	exitcode = calldb.poll()
	if exitcode == 0:
		print "DeaDBeeF closed!"
	else:
		pass
		
def exit_deadbeef_user(word, word_eol, userdata):
	exit_deadbeef = subprocess.Popen('killall deadbeef-main',shell=True,stdout=subprocess.PIPE)
	exit_deadbeef.communicate()[0]
	print "DeaDBeeF closed!"
	
	return xchat.EAT_ALL

def call_deadbeef_user(word, word_eol, userdata):
	runningornot = subprocess.Popen('ps -e | grep "deadbeef-main"',shell=True,stdout=subprocess.PIPE)
	runningornot_out = runningornot.communicate()[0]
	if len(runningornot_out) == 0:
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
	runningornot = subprocess.Popen('ps -e | grep "deadbeef-main"',shell=True,stdout=subprocess.PIPE)
	runningornot_out = runningornot.communicate()[0]
	if len(runningornot_out) == 0:
		print "DeaDBeeF is not running. Launching in 5s..."
		call_deadbeef_thread = Thread(target=call_deadbeef_script)
		call_deadbeef_thread.start()
	else:
		pass
			
def is_track_loaded():
	loadedornot = subprocess.Popen("deadbeef --nowplaying %e",shell=True,stdout=subprocess.PIPE)
	loadedornot_out = loadedornot.communicate()[0]
	if "nothing" in loadedornot_out:
		print "Track loaded!"
	else:
		print "Track resumed/reset!"

def show_track_info_script():
	show_track = subprocess.Popen('deadbeef --nowplaying "%t by %a"',shell=True,stdout=subprocess.PIPE)
	show_track_out = show_track.communicate()[0]
	print "You're listening to: %s" % str(show_track_out)

def show_track_info_user(word, word_eol, userdata):
	show_track = subprocess.Popen('deadbeef --nowplaying "%t by %a // %@:BITRATE@kbps"',shell=True,stdout=subprocess.PIPE)
	show_track_out = show_track.communicate()[0]
	print "You're listening to: %s" % str(show_track_out)
	
	return xchat.EAT_ALL
	
def deadbeef_current_track(word, word_eol, userdata):
	is_deadbeef_running()
	read_track = subprocess.Popen('deadbeef --nowplaying "%t by %a"',shell=True,stdout=subprocess.PIPE)
	read_track_out = read_track.communicate()[0]
	announce_track = str(read_track_out).strip('\n')
	xchat.command("say "+announce_track)
	
	return xchat.EAT_ALL
      
def deadbeef_next_track(word, word_eol, userdata):
	is_deadbeef_running()
	next_track = subprocess.Popen("deadbeef --next",shell=True,stdout=subprocess.PIPE)
	next_track.communicate()[0]
	print "Next track loaded!"
	sleep(0.05) # Give some time to DeaDBeeF to update accurately
	show_track_info_script()
	
	return xchat.EAT_ALL
 
def deadbeef_previous_track(word, word_eol, userdata):
	is_deadbeef_running()
	prev_track = subprocess.Popen("deadbeef --prev",shell=True,stdout=subprocess.PIPE)
	prev_track.communicate()[0]
	print "Previous track loaded!"
	sleep(0.05) # Give some time to DeaDBeeF to update accurately 
	show_track_info_script()
	
	return xchat.EAT_ALL
 
def deadbeef_play_track(word, word_eol, userdata):
	is_deadbeef_running()
	is_track_loaded()
	play_track = subprocess.Popen("deadbeef --play",shell=True,stdout=subprocess.PIPE)
	play_track.communicate()[0]
	sleep(0.05) # Give some time to DeaDBeeF to update accurately
	show_track_info_script()
	
	return xchat.EAT_ALL
 
def deadbeef_pause_track(word, word_eol, userdata):
	is_deadbeef_running()
	pause_track = subprocess.Popen("deadbeef --pause",shell=True,stdout=subprocess.PIPE)
	pause_track.communicate()[0]
	track_playing_time = subprocess.Popen("deadbeef --nowplaying '(%e/%l)'",shell=True,stdout=subprocess.PIPE)
	track_playing_time_out = track_playing_time.communicate()[0]
	print "Current track paused! %s" % track_playing_time_out
	
	return xchat.EAT_ALL
	
def deadbeef_stop_track(word, word_eol, userdata):
	is_deadbeef_running()
	stop_track = subprocess.Popen("deadbeef --stop",shell=True,stdout=subprocess.PIPE)
	stop_track.communicate()[0]
	print "Current track stopped!"
	
	return xchat.EAT_ALL
	
def unload(userdata):
	print "XChat-DeaDBeeF %s unloaded!" % (__module_version__)
	
	return xchat.EAT_ALL
	
if __name__ == '__main__':
	
	print "XChat-DeaDBeeF %s loaded successfully! - by %s" % (__module_version__,__module_author__)
	print "Protip: using /dbplay when the track is playing resets the track."
	
	is_deadbeef_running() #=> call_deadbeef_script() in new thread => execute_deadbeef() in the same thread.

#Launch/close DeaDBeeF
	xchat.hook_command('deadbeef',call_deadbeef_user) #=>  execute_deadbeef() in a new thread.
	xchat.hook_command('dbexit',exit_deadbeef_user) 
    
#Display the current track (chose one)
	xchat.hook_command('dbshow',show_track_info_user)
	xchat.hook_command('np',deadbeef_current_track)
	
#Play, pause, stop track
	xchat.hook_command('dbplay',deadbeef_play_track)
	xchat.hook_command('dbpause',deadbeef_pause_track)
	xchat.hook_command('dbstop',deadbeef_stop_track)
	
#Skip to next or previous track
	xchat.hook_command('dbnext',deadbeef_next_track)
	xchat.hook_command('dbprev',deadbeef_previous_track)
	
#Unload XChat-DeaDBeeF
	xchat.hook_unload(unload)
