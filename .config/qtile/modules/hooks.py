from libqtile import hook, qtile
import subprocess
import os
import aiomanhole
import json
import tempfile
import glob
from os import path


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


@hook.subscribe.client_managed
def systray_popup(window):
    windows = {
        "Bluetooth": (655, 800, 62, 2340),
        "ripdrag": (400, 720, 1698, 924)
        }
    wm_name = window.cmd_inspect()['name']
    if wm_name in windows:
        win = windows[wm_name]
        window.toggle_floating()
        window.cmd_set_size_floating(win[0], win[1])
        window.cmd_set_postion_floating(win[2], win[3])


@hook.subscribe.startup_complete
def set_manhole():
    aiomanhole.start_manhole(port=7113, namespace={"qtile": qtile})


# @hook.subscribe.startup_complete
# disabled for know because it crashes
def restore_layout():
    layout_files = glob.glob(path.join(tempfile.gettempdir(), "qtile_layout*"))
    if len(layout_files) == 0:
        return
    layout_filename = max(layout_files, key=lambda x: path.getmtime(x))
    with open(layout_filename, 'r') as f:
        layouts = json.load(f)
    for group in qtile.groups:
        if group.name not in layouts:
            continue
        layout_name, clients = layouts[group.name]
        if layout_name == "stack" == group.layout.name:
            # clients is a dict
            for client in group.layout.clients:
                if client.name not in clients:
                    continue
                to_stack = clients[client.name]
                for stack_num, stack in enumerate(group.layout.stacks):
                    if stack_num != to_stack and client in stack.clients:
                        stack.remove(client)
                        break
                group.layout.stacks[to_stack].append(client)
            group.layout_all()
        elif layout_name == "monadtall" == group.layout.name:
            # clients is a list
            group_clients = group.layout.clients.clients.copy()
            for client in group_clients:
                index = clients.index(client.name)
                group.layout.remove(client)
                group.layout.clients.add_client(client, offset_to_current=index)
            group.layout_all()


@hook.subscribe.screen_change
def configure_screens(event):
    script = os.path.expanduser('~/.screenlayout/set_screenlayout.sh')
    subprocess.call([script])
    qtile.restart()


@hook.subscribe.restart
def save_layout():
    layouts ={}
    for group in qtile.groups:
        clients = None
        layout = group.layout
        if layout.name == "stack":
            clients = {}
            for stack_num, stack in enumerate(layout.stacks):
                for client in stack.clients:
                    clients[client.name] = stack_num
            layouts[group.name] = (layout.name, clients)
        elif layout.name == "monadtall":
            clients = [client.name for client in layout.clients]
            layouts[group.name] = (layout.name, clients)

    with tempfile.NamedTemporaryFile(mode="w", prefix="qtile_layout", delete=False) as tf:
        json.dump(layouts, tf)
