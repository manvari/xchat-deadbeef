#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  XChat-DeaDBeeF.py  -  XChat plugin for DeaDBeeF integration
#
#  Copyright (C) 2013 iceTwy <nerorush23@gmail.com>
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004
#
#  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
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
__module_version__ = "0.2"
__module_author__ = "Trixar_za & iceTwy"
__module_credits__ = ["Trixar_za", "iceTwy"]
__module_license__ = "WTFPL"
__module_maintainer__ = "iceTwy"
__module_email__ = "nerorush23@gmail.com"
__module_status__ = "Released"

###########################
import xchat
import os
###########################

def deadbeef_current_song(word, word_eol, userdata):
      read_song = os.popen('deadbeef --nowplaying "%a - %t - %b% (%y) // %@:BITRATE@kbps"').read().strip()
      nickname = "♪ NP @ %s ♪ - " % xchat.get_info("nick")
      announce_song = nickname + str(read_song)
      xchat.command("say "+announce_song)
      return xchat.EAT_ALL
      
def deadbeef_next_song(word, word_eol, userdata):
    os.system("deadbeef --next")
    return xchat.EAT_ALL
 
def deadbeef_previous_song(word, word_eol, userdata):
    os.system("deadbeef --prev")
    return xchat.EAT_ALL
 
def deadbeef_playpause_song(word, word_eol, userdata):
    os.system("deadbeef --play-pause")
    return xchat.EAT_ALL
 
def deadbeef_stop_song(word, word_eol, userdata):
    os.system("deadbeef --stop")
    return xchat.EAT_ALL
    
xchat.hook_command('currentsong',deadbeef_current_song) 
xchat.hook_command('nextsong',deadbeef_next_song)
xchat.hook_command('prevsong',deadbeef_previous_song)
xchat.hook_command('playpausesong',deadbeef_playpause_song)
xchat.hook_command('stopsong',deadbeef_stop_song)

print "XChat-DeaDBeeF %s plugin loaded successfully! - by %s" % (__module_version__,__module_author__)
print "Protip: use /playpausesong to play, pause and resume playback (if paused)."
