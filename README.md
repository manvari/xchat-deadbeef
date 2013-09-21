# XChat-DeaDBeeF
XChat-DeaDBeeF is a Python script for XChat and HexChat. It implements commands to control the DeaDBeeF music player, directly from the text box.
It was initially developed in late 2011 and came back to life in May 2013.

###  How does it work?

XChat-DeaDBeeF implements a few commands that can be typed into the text box at any moment. 

Commands:

* **/deadbeef** - launches DeaDBeeF
* **/np**, **/tellnp** - displays current track / says current track in channel
* **/dbplay** - resumes playback if track is paused, plays the selected song* if a track is already playing
* **/dbpause** - pauses current track
* **/dbnext**, **/dbprev** - loads next/previous track in playlist
* **/dbstop** - stops current track
* **/dbexit** - closes DeaDBeeF

**N.B.**: the selected song is the one that is currently highlighted/clicked on in DeadBeeF.

### Requirements

XChat-DeaDBeeF only needs the bare minimum to run. However, you'll have to check the version of the Python scripting interface that came
with your XChat/HexChat package. XChat should have the Python 2 scripting interface, but newer HexChat packages (including those from Arch Linux) include the Python 3 one.

On the top-bar menu, navigate to _Window > Plugins and Scripts... > Load... > /path/to/XChat-DeaDBeeF.py_, and see whether it indicates Python 2 or 3. Depending on the version, download:

* [Python 3.3.x](http://www.python.org/getit/ "Download Python") (older 3.x versions are not supported by HexChat)
* [Python 2.7.x](http://www.python.org/getit/ "Download Python") (or 2.6.x)

And, obviously, you'll need:

* [DeaDBeeF 0.5.x](http://deadbeef.sourceforge.net/download.html "DeaDBeeF - Ultimate Music Player For GNU/Linux")
* [XChat](http://sourceforge.net/projects/xchat/files/ "X-Chat - Browse Files at SourceForge.net") or [HexChat](http://hexchat.org/downloads.html "Downloads - HexChat") for Linux

_Note: XChat is no longer being actively developed. HexChat, one of its forks, is now the main project and receives regular updates._

Your distribution should propose packages for all of those programs; install them normally with your package manager.

If not, compile and install them from scratch.

### Installation

Installing XChat-DeaDBeeF is pretty straightforward.

* For XChat:
    1. Clone the Git repository to any folder (or, alternatively, download the source tarball).
    2. Move **XChat-DeaDBeeF.py** to **$HOME/.xchat2/** (which contains all of your XChat addons).

* For HexChat:
    1. Clone the Git repository to any folder (or, alternatively, download the source tarball).
    2. Move **XChat-DeaDBeeF.py** to **~/.config/hexchat/addons/** (which contains all of your HexChat addons).

XChat-DeaDBeeF will now be automatically loaded upon launching XChat/HexChat.

_Note: if necessary, XChat-DeaDBeeF can also be (re)loaded via Window > Plugins and Scripts... > Load... > /path/to/XChat-DeaDBeeF.py._

### To-Do list

Refer to [this page](https://github.com/iceTwy/xchat-deadbeef/blob/master/TODO.md "TO-DO List").

### Contribution

You are welcome to modify the script and add some new features!

To contribute, please fork the project, make your changes on a branch, then submit a Pull Request. 

Clear and accurate descriptions of changes are a must.

### License

```
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2013 iceTwy <icetwy@icetwy.re>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
