from libqtile.lazy import lazy
from libqtile.config import Key
import os

mod = "mod4"
terminal = "kitty"


@lazy.function
def swap_groups(qtile):
    # For swapping groups between screens
    current_screen = qtile.current_screen.index
    other_screen = (current_screen + 1) % 2 # only for 2 screens
    qtile.current_screen.group.cmd_toscreen(other_screen)


@lazy.function
def move_window_left(qtile):
    layout_id = qtile.current_screen.group.current_layout
    layout_name = qtile.current_screen.group.layouts[layout_id].name
    if layout_name == "stack":
        qtile.current_screen.group.layout.cmd_client_to_previous()
    else:
        qtile.current_screen.group.layout.cmd_shuffle_up()


@lazy.function
def move_window_right(qtile):
    layout_id = qtile.current_screen.group.current_layout
    layout_name = qtile.current_screen.group.layouts[layout_id].name
    if layout_name == "stack":
        qtile.current_screen.group.layout.cmd_client_to_next()
    else:
        qtile.current_screen.group.layout.cmd_shuffle_down()


@lazy.function
def move_left(qtile):
    layout_id = qtile.current_screen.group.current_layout
    layout_name = qtile.current_screen.group.layouts[layout_id].name
    if layout_name == "stack":
        qtile.current_screen.group.layout.previous_stack()
    else:
        qtile.current_screen.group.layout.cmd_left()


@lazy.function
def move_right(qtile):
    layout_id = qtile.current_screen.group.current_layout
    layout_name = qtile.current_screen.group.layouts[layout_id].name
    if layout_name == "stack":
        qtile.current_screen.group.layout.next_stack()
    else:
        qtile.current_screen.group.layout.cmd_right()


keys = [
    # Switch between windows
    Key([mod], "h", move_left, desc="Move focus to left"),
    Key([mod], "l", move_right, desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to next window"),
    Key([mod, "shift"], "space", lazy.layout.previous(), desc="Move focus to previous window"),

    Key([mod], "d", lazy.spawn("rofi -show combi -font 'Symbols Nerd Font 24'"), desc="spawn rofi"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle window floating"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        move_window_left,
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        move_window_right,
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Normalize window sizes"),
    Key([mod], "o", lazy.layout.maximize(), desc="Maximize current window size"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Swap groups between screens
    Key([mod], 'comma', swap_groups),

    # Go to other screen
    Key([mod], 'period', lazy.next_screen()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.client_to_previous()),
    Key([mod, "shift", "control"], "l", lazy.layout.client_to_next()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "d",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "e", lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh')), desc="Spawn the powermenu"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
]


