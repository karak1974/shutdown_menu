#!/bin/env python3
import gi
import os, sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):

    def act_shutdown(self, button):
        os.system("shutdown now")
    def act_reboot(self, button):
        os.system("shutdown -r now")
    def close_click(self, button):
        Gtk.main_quit()

    def __init__(self):
        Gtk.Window.__init__(self, title="Brightness")
        self.set_default_size(350, 50)
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Shutdown")
        button.connect("clicked", self.act_shutdown)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Reboot")
        button.connect("clicked", self.act_reboot)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Close")
        button.connect("clicked", self.close_click)
        hbox.pack_start(button, True, True, 0)

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
