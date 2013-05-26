# XChat-DeaDBeeF
==============
XChat-DeaDBeeF is a Python plugin for XChat that integrates the well-known DeaDBeeF music player into XChat.
It was developed in late 2011 and came back to life in May 2013.

==============
###  How does it work?

XChat-DeaDBeeF adds a few commands that can be typed into the XChat text box at any moment.

Commands:

* **/currentsong** - displays current song in channel.
* **/nextsong**, **/prevsong** - loads next/previous track in playlist.
* **/playpausesong** - plays, pauses or resumes playback (if paused).
* **/stopsong** - stops current song.

### Requirements

Obvious programs are required:

* [Python 2.7.x](http://www.python.org/getit/ "Download Python") (or 2.6.x)
* [XChat IRC for Linux](http://sourceforge.net/projects/xchat/files/ "X-Chat - Browse Files at SourceForge.net") (2.8.8)
* [DeaDBeeF 0.5.x](http://deadbeef.sourceforge.net/download.html "DeaDBeeF - Ultimate Music Player For GNU/Linux")

Your distribution should propose packages for those programs; install them normally with your package manager. 

If not, compile and install them from scratch.

### Installation

Installing XChat-DeaDBeeF is pretty straightforward.

Clone the Git repository to any folder, then move **XChat-DeaDBeeF.py** to **$HOME/.xchat2**.

This will automatically load XChat-DeaDBeeF when XChat is launched.

### Contribution

You are welcome to modify the plugin and add some new features!

To contribute, please fork the project, make your changes on branch, then submit a Pull Request. 

Clear and accurate descriptions of changes are a must.
