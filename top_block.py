#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
import numpy as np
import time
import threading

from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.probe = probe = 0
        self.partyModeDirection = partyModeDirection = int(int(np.real(probe)*127)%7)
        self.vector = vector = 1
        self.variable_qtgui_label_1 = variable_qtgui_label_1 = partyModeDirection
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = probe
        self.variable_qtgui_check_box_0 = variable_qtgui_check_box_0 = 0
        self.symbol_duration = symbol_duration = 0.302e-3
        self.stopCar = stopCar = [0]
        self.samp_rate = samp_rate = 2000000
        self.right = right = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        self.reverseRight = reverseRight = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        self.reverseLeft = reverseLeft = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        self.reverse = reverse = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
        self.partyIntensity = partyIntensity = 4
        self.left = left = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        self.forwardRight = forwardRight = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        self.forwardLeft = forwardLeft = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        self.forward = forward = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        self.center_freq = center_freq = 27146000

        ##################################################
        # Blocks
        ##################################################
        # Create the options list
        self._vector_options = [0, 1, 2, 3, 4, 5, 6]
        # Create the labels list
        self._vector_labels = ['Forward (0)', 'Stop Car (1)', 'Reverse (2)', 'Forward Right (3)', 'Forward Left (4)', 'Reverse Right (5)', 'Reverse Left (6)']
        # Create the combo box
        # Create the radio buttons
        self._vector_group_box = Qt.QGroupBox('Choose Direction' + ": ")
        self._vector_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._vector_button_group = variable_chooser_button_group()
        self._vector_group_box.setLayout(self._vector_box)
        for i, _label in enumerate(self._vector_labels):
            radio_button = Qt.QRadioButton(_label)
            self._vector_box.addWidget(radio_button)
            self._vector_button_group.addButton(radio_button, i)
        self._vector_callback = lambda i: Qt.QMetaObject.invokeMethod(self._vector_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._vector_options.index(i)))
        self._vector_callback(self.vector)
        self._vector_button_group.buttonClicked[int].connect(
            lambda i: self.set_vector(self._vector_options[i]))
        self.top_grid_layout.addWidget(self._vector_group_box)
        _variable_qtgui_check_box_0_check_box = Qt.QCheckBox('Enable Party Mode')
        self._variable_qtgui_check_box_0_choices = {True: 1, False: 0}
        self._variable_qtgui_check_box_0_choices_inv = dict((v,k) for k,v in self._variable_qtgui_check_box_0_choices.items())
        self._variable_qtgui_check_box_0_callback = lambda i: Qt.QMetaObject.invokeMethod(_variable_qtgui_check_box_0_check_box, "setChecked", Qt.Q_ARG("bool", self._variable_qtgui_check_box_0_choices_inv[i]))
        self._variable_qtgui_check_box_0_callback(self.variable_qtgui_check_box_0)
        _variable_qtgui_check_box_0_check_box.stateChanged.connect(lambda i: self.set_variable_qtgui_check_box_0(self._variable_qtgui_check_box_0_choices[bool(i)]))
        self.top_grid_layout.addWidget(_variable_qtgui_check_box_0_check_box)
        self.signalProbe = blocks.probe_signal_c()
        self._partyIntensity_range = Range(1, 10, 1, 4, 200)
        self._partyIntensity_win = RangeWidget(self._partyIntensity_range, self.set_partyIntensity, 'Party Intensity', "counter_slider", float)
        self.top_grid_layout.addWidget(self._partyIntensity_win)
        self._variable_qtgui_label_1_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_1_formatter = None
        else:
            self._variable_qtgui_label_1_formatter = lambda x: str(x)

        self._variable_qtgui_label_1_tool_bar.addWidget(Qt.QLabel('Party Mode Current Direction' + ": "))
        self._variable_qtgui_label_1_label = Qt.QLabel(str(self._variable_qtgui_label_1_formatter(self.variable_qtgui_label_1)))
        self._variable_qtgui_label_1_tool_bar.addWidget(self._variable_qtgui_label_1_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_1_tool_bar)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: repr(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Amplitude' + ": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            center_freq, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            False, #plotwaterfall
            True, #plottime
            False #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        def _probe_probe():
            while True:

                val = self.signalProbe.level()
                try:
                    self.set_probe(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (partyIntensity))
        _probe_thread = threading.Thread(target=_probe_probe)
        _probe_thread.daemon = True
        _probe_thread.start()

        self.blocks_vector_source_x_0_0_0_1 = blocks.vector_source_c(stopCar, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0_0_0_0 = blocks.vector_source_c(reverse, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0_0_0 = blocks.vector_source_c(forward, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0_0 = blocks.vector_source_c(reverseLeft, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0 = blocks.vector_source_c(forwardRight, True, 1, [])
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_c(reverseRight, True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c(forwardLeft, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_selector_2 = blocks.selector(gr.sizeof_gr_complex*1,vector,0)
        self.blocks_selector_2.set_enabled(True)
        self.blocks_selector_1 = blocks.selector(gr.sizeof_gr_complex*1,partyModeDirection,0)
        self.blocks_selector_1.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,variable_qtgui_check_box_0,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, int(samp_rate*symbol_duration))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_selector_1, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_selector_2, 0), (self.blocks_selector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.signalProbe, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_selector_1, 4))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_selector_2, 4))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_selector_1, 5))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_selector_2, 5))
        self.connect((self.blocks_vector_source_x_0_0_0_0, 0), (self.blocks_selector_1, 3))
        self.connect((self.blocks_vector_source_x_0_0_0_0, 0), (self.blocks_selector_2, 3))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0, 0), (self.blocks_selector_1, 6))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0, 0), (self.blocks_selector_2, 6))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0_0, 0), (self.blocks_selector_1, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0_0, 0), (self.blocks_selector_2, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0_0_0, 0), (self.blocks_selector_1, 2))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0_0_0, 0), (self.blocks_selector_2, 2))
        self.connect((self.blocks_vector_source_x_0_0_0_1, 0), (self.blocks_selector_1, 1))
        self.connect((self.blocks_vector_source_x_0_0_0_1, 0), (self.blocks_selector_2, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_probe(self):
        return self.probe

    def set_probe(self, probe):
        self.probe = probe
        self.set_partyModeDirection(int(int(np.real(self.probe)*127)%7))
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.probe))

    def get_partyModeDirection(self):
        return self.partyModeDirection

    def set_partyModeDirection(self, partyModeDirection):
        self.partyModeDirection = partyModeDirection
        self.set_variable_qtgui_label_1(self._variable_qtgui_label_1_formatter(self.partyModeDirection))
        self.blocks_selector_1.set_input_index(self.partyModeDirection)

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector
        self._vector_callback(self.vector)
        self.blocks_selector_2.set_input_index(self.vector)

    def get_variable_qtgui_label_1(self):
        return self.variable_qtgui_label_1

    def set_variable_qtgui_label_1(self, variable_qtgui_label_1):
        self.variable_qtgui_label_1 = variable_qtgui_label_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_1_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_1))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_variable_qtgui_check_box_0(self):
        return self.variable_qtgui_check_box_0

    def set_variable_qtgui_check_box_0(self, variable_qtgui_check_box_0):
        self.variable_qtgui_check_box_0 = variable_qtgui_check_box_0
        self._variable_qtgui_check_box_0_callback(self.variable_qtgui_check_box_0)
        self.blocks_selector_0.set_input_index(self.variable_qtgui_check_box_0)

    def get_symbol_duration(self):
        return self.symbol_duration

    def set_symbol_duration(self, symbol_duration):
        self.symbol_duration = symbol_duration
        self.blocks_repeat_0.set_interpolation(int(self.samp_rate*self.symbol_duration))

    def get_stopCar(self):
        return self.stopCar

    def set_stopCar(self, stopCar):
        self.stopCar = stopCar
        self.blocks_vector_source_x_0_0_0_1.set_data(self.stopCar, [])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_repeat_0.set_interpolation(int(self.samp_rate*self.symbol_duration))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def get_reverseRight(self):
        return self.reverseRight

    def set_reverseRight(self, reverseRight):
        self.reverseRight = reverseRight
        self.blocks_vector_source_x_0_0_0.set_data(self.reverseRight, [])

    def get_reverseLeft(self):
        return self.reverseLeft

    def set_reverseLeft(self, reverseLeft):
        self.reverseLeft = reverseLeft
        self.blocks_vector_source_x_0_0_0_0_0.set_data(self.reverseLeft, [])

    def get_reverse(self):
        return self.reverse

    def set_reverse(self, reverse):
        self.reverse = reverse
        self.blocks_vector_source_x_0_0_0_0_0_0_0.set_data(self.reverse, [])

    def get_partyIntensity(self):
        return self.partyIntensity

    def set_partyIntensity(self, partyIntensity):
        self.partyIntensity = partyIntensity

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_forwardRight(self):
        return self.forwardRight

    def set_forwardRight(self, forwardRight):
        self.forwardRight = forwardRight
        self.blocks_vector_source_x_0_0_0_0.set_data(self.forwardRight, [])

    def get_forwardLeft(self):
        return self.forwardLeft

    def set_forwardLeft(self, forwardLeft):
        self.forwardLeft = forwardLeft
        self.blocks_vector_source_x_0_0.set_data(self.forwardLeft, [])

    def get_forward(self):
        return self.forward

    def set_forward(self, forward):
        self.forward = forward
        self.blocks_vector_source_x_0_0_0_0_0_0.set_data(self.forward, [])

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)





def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
