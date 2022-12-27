from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from libqtile import qtile
from modules.keys import terminal
import os
import subprocess


class MainScreen(Screen):
    num_screens = 1

    def __init__(self):
        Screen.__init__(self,
            top=bar.Bar([
                widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(
                    filename='~/.config/qtile/eos-c.png',
                    margin=3,
                    background="#2f343f",
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn("rofi -show combi -font 'Symbols Nerd Font 24'")
                    }
                ),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"),
                widget.GroupBox(
                    highlight_method='line',
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f",
                    fontsize=32
                ),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=48,
                    foreground='#2f343f'
                ),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de', fmt='{}', fontsize=32),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                ),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=48,
                    foreground='#2f343f'
                ),
                widget.Systray(
                    icon_size=55,
                    background='#2f343f'
                ),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=48,
                    foreground='#2f343f'
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    format=":{percent:2.0%} "
                ),
                DynamicBattery(
                    fontsize=32,
                    charge_char='',
                    discharge_char='',
                    full_char='',
                    empty_char=''
                ),
                widget.CPUGraph(
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('xfce4-terminal -T htop -x htop')},
                    graph_color=colors[4],
                    border_color="#2f343f",
                ),
                widget.ThermalSensor(
                    format='{tag}: {temp:.1f}{unit}',
                    threshold=80.0,
                    tag_sensor='CPU'
                ),
                PowerProfile(),
                VolumeIcon(
                    fontsize=72,
                    font='Font Awesome 5 Free',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
                ),
                VolumeText(
                    fontsize=32,
                    font='Font Awesome 5 Free',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
                ),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=48,
                    foreground='#2f343f'
                ),
                widget.Clock(
                    format=' %Y-%m-%d %a %I:%M %p',
                    background="#2f343f",
                    foreground='#9bd689',
                    fontsize=32,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("xfce4-terminal -T calendar -H -x gcalcli calm")},
                ),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=48,
                    foreground='#2f343f',
                ),
                widget.TextBox(
                    text='',
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378',
                    fontsize=64
                ), ],
                60,  # height in px
                background="#404552",  # background color
                opacity=0.70
            )
        )


class SecondScreen(MainScreen):
    def __init__(self):
        MainScreen.__init__(self)
        self.top.widgets.pop(11)
        self.top.widgets.pop(11)
        self.top.widgets.pop(11)


screens = [MainScreen()]

xrandr = subprocess.Popen('xrandr | grep " connected" | wc -l',
                              shell=True, stdout=subprocess.PIPE)
display_count = int(xrandr.communicate()[0])
screens[0].num_screens = display_count

for i in range(display_count - 1):
    screens.insert(0, SecondScreen())
