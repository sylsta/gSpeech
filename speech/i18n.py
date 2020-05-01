import gettext
import sys
from os.path import dirname, join

from .debug import is_debug_mode

if is_debug_mode():
    LOCAL_PATH = join(dirname(dirname(__file__)), 'locale')
else:
    LOCAL_PATH = join(
        dirname(sys.modules['speech'].__file__),
        '..', '..', '..', '..', 'share', 'locale'
    )

gettext.bindtextdomain('gSpeech', LOCAL_PATH)
gettext.textdomain('gSpeech')
_ = gettext.gettext

_tooltip = _('SVOX Pico simple GUI')
_read_clipboard = _('Read clipboard content')
_read_selected = _('Read selected text')
_comment = _(
    'A little script to read SVOX Pico texts selected with the mouse.'
)
_developpers = _('Developers :')
_languages = _('Languages')
_play = _('Play')
_pause = _('Pause')
_stop = _('Stop')
_save = _('Save')
_multimedia_window = _('Multimedia window')
_refresh = _('Refresh')
_about = _('About')
_options = _('Options')
_quit = _('Quit')
