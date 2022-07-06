from libqtile import widget
from libqtile.widget import base
from libqtile.lazy import lazy

colors = [
          ["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
] 


widget_defaults = dict(
    font='Cantarell',
    fontsize=32,
    padding=3,
)
extension_defaults = widget_defaults.copy()


class VolumeIcon(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        self.draw()


class VolumeText(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        self.text = ': ' + str(self.volume) + '%'
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        self.text = ': ' + str(self.volume) + '%'
        self.draw()


class PowerProfile(base._TextBox):
    defaults = [
        ("padding", 3, "Padding left and right. Calculated if None."),
        ("update_interval", 0.2, "Update time in seconds."),
        ("balanced_char", "", "Character used for balanced profile"),
        ("low_power_char", "", "Character used for low-power profile"),
        ("update_interval", 2, "Update time in seconds"),
    ]

    def __init__(self, **config):
        base._TextBox.__init__(self, "0", **config)
        self.add_defaults(PowerProfile.defaults)
        self.profile = ''
        #self.add_callbacks({"Button1": self._toggle_mode})

    def _check_power_profile(self):
        with open('/sys/firmware/acpi/platform_profile') as f:
            return f.read().strip('\n')

    def _toggle_mode(self):
        profile = self._check_power_profile()
        if profile == 'balanced':
            lazy.spawn('xdotool XF86WakeUp+L')
        elif profile == 'low-power':
            lazy.spawn('xdotool XF86WakeUp+M')

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.timeout_add(self.update_interval, self.update)

    def update(self):
        profile = self._check_power_profile()
        if self.profile != profile:
            self.profile = profile
            self._update_drawer()
            self.bar.draw()
        self.timeout_add(self.update_interval, self.update)

    def _update_drawer(self):
        if self.profile == 'balanced':
            self.text = self.balanced_char
        elif self.profile == 'low-power':
            self.text = self.low_power_char
        else:
            self.text = self.profile


class DynamicBattery(widget.Battery):
    def _configure(self, qtile, bar):
        widget.Battery._configure(self, qtile, bar)
        self.disp = 0
        self.format = '{char} {percent:2.0%}'
        self.add_callbacks({"Button1": self._toggle_format})

    def _toggle_format(self):
        if self.disp == 0:
            self.disp = 1
            self.format = '{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W'
        else:
            self.disp = 0
            self.format = '{char} {percent:2.0%}'
        self.update(self.poll())
        self.bar.draw()
