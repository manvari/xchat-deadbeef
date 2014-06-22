# -*- coding: utf-8 -*-
#
#  XChat-DeaDBeeF  -  XChat/HexChat script for DeaDBeeF integration
#  Python 3 version
#
#  Unless indicated otherwise, files from the XChat-DeaDBeeF project
#  are licensed under the WTFPL version 2. Full license information
#  for the WTFPL version 2 can be found in the LICENSE.txt file.
#

__module_name__ = "XChat-DeaDBeeF"
__module_author__ = "iceTwy"
__module_description__ = "DeaDBeeF integration in XChat and HexChat."
__module_version__ = "1.0"

import xchat
import subprocess
from threading import Thread
from time import sleep

def execute_db():
    print(" DeaDBeeF launched.")
    calldb = subprocess.call("deadbeef")
    if calldb == 0 or calldb == 1:
        print(" DeaDBeeF closed.")

def exit_db_user(word, word_eol, userdata):
    check_pid = subprocess.call(["pgrep", "-f", "deadbeef"])
    if check_pid == 1:
        print(" DeaDBeeF isn't running.")
    else:
        db_pid = subprocess.check_output(["pgrep", "-f", "deadbeef"])
        exit_db = subprocess.call(["kill", str(db_pid, encoding='utf8').strip('\n')])

    return xchat.EAT_ALL

def call_db_user(word, word_eol, userdata):
    db_pid = subprocess.call(["pgrep", "-f", "deadbeef"])
    if db_pid == 1:
        calldb_user_thread = Thread(target=execute_db)
        calldb_user_thread.start()
    else:
        print(" DeaDBeeF is already running.")

    return xchat.EAT_ALL

def is_db_running():
    check_db_pid = subprocess.call(["pgrep", "-f", "deadbeef"])
    if check_db_pid == 1:
        print(" DeaDBeeF is not running. Launching...")
        call_db_thread = Thread(target=execute_db)
        call_db_thread.start()

def is_track_loaded():
    np_track = subprocess.check_output(["deadbeef", "--nowplaying", "%e"])
    if "nothing" in str(np_track):
        print(" Track loaded!")
    else:
        print(" Track resumed/reset!")

def track_info_script():
    track = subprocess.check_output(["deadbeef", "--nowplaying", "%t by %a"])
    print(" You're listening to: {}".format(str(track, encoding='utf8')))

def track_info_user(word, word_eol, userdata):
    track = subprocess.check_output(["deadbeef", "--nowplaying", "%t by %a // %@:BITRATE@kbps"])
    print(" You're listening to: {}".format(str(track, encoding='utf8')))

    return xchat.EAT_ALL

def db_current_track(word, word_eol, userdata):
    is_db_running()
    track = subprocess.check_output(["deadbeef", "--nowplaying", "%t by %a"])
    xchat.command("me is listening to: {}".format(str(track, encoding='utf8')))

    return xchat.EAT_ALL

def db_next_track(word, word_eol, userdata):
    is_db_running()
    next_track = subprocess.call(["deadbeef", "--next"])
    print(" Next track loaded!")
    sleep(0.05) # Give some time to DeaDBeeF to update accurately
    track_info_script()

    return xchat.EAT_ALL

def db_previous_track(word, word_eol, userdata):
    is_db_running()
    prev_track = subprocess.call(["deadbeef", "--prev"])
    print(" Previous track loaded!")
    sleep(0.05) # Give some time to DeaDBeeF to update accurately
    track_info_script()

    return xchat.EAT_ALL

def db_play_track(word, word_eol, userdata):
    is_db_running()
    is_track_loaded()
    play_track = subprocess.call(["deadbeef", "--play"])
    sleep(0.1) # Give some time to DeaDBeeF to update accurately
    track_info_script()

    return xchat.EAT_ALL

def db_pause_track(word, word_eol, userdata):
    is_db_running()
    pause_track = subprocess.call(["deadbeef", "--pause"])
    track_time = subprocess.check_output(["deadbeef", "--nowplaying", "%e/%l"])
    print(" Current track paused at {}.".format(str(track_time, encoding='utf8')))

    return xchat.EAT_ALL

def db_stop_track(word, word_eol, userdata):
    is_db_running()
    stop_track = subprocess.call(["deadbeef", "--stop"])
    print(" Current track stopped!")

    return xchat.EAT_ALL

def unload(userdata):
    print(" XChat-DeaDBeeF {} unloaded!".format(__module_version__))

    return xchat.EAT_ALL

if __name__ == '__main__':
    print(" XChat-DeaDBeeF {} loaded successfully! - by {}".format(__module_version__,__module_author__))
    print(" Protip: using /dbplay when the track is playing resets the track.")

    #Launch/close DeaDBeeF
    xchat.hook_command('deadbeef',call_db_user) #=>  execute_db() in a new thread.
    xchat.hook_command('dbexit',exit_db_user)

    #Display the current track
    xchat.hook_command('dbshow',track_info_user)
    xchat.hook_command('np',db_current_track)

    #Play, pause, stop track
    xchat.hook_command('dbplay',db_play_track)
    xchat.hook_command('dbpause',db_pause_track)
    xchat.hook_command('dbstop',db_stop_track)

    #Skip to next or previous track
    xchat.hook_command('dbnext',db_next_track)
    xchat.hook_command('dbprev',db_previous_track)

    #Unload XChat-DeaDBeeF
    xchat.hook_unload(unload)
