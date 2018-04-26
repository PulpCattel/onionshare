# -*- coding: utf-8 -*-
"""
OnionShare | https://onionshare.org/

Copyright (C) 2014-2018 Micah Lee <micah@micahflee.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from PyQt5 import QtCore, QtWidgets, QtGui

from onionshare import strings

from ..mode import Mode

class ReceiveMode(Mode):
    """
    Parts of the main window UI for receiving files.
    """
    def init(self):
        """
        Custom initialization for ReceiveMode.
        """
        # Receive mode info
        self.receive_info = QtWidgets.QLabel(strings._('gui_receive_mode_warning', True))
        self.receive_info.setMinimumHeight(80)
        self.receive_info.setWordWrap(True)

        # Layout
        self.layout.insertWidget(0, self.receive_info)

    def timer_callback(self):
        """
        This method is called regularly on a timer while receive mode is active.
        """
        pass
    
    def start_server_step2_custom(self):
        """
        Step 2 in starting the server. Nothing to do here but move on to step 3.
        """
        self.starting_server_step3.emit()
        self.start_server_finished.emit()
