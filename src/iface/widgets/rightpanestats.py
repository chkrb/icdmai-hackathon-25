from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtWidgets import QFrame, QGraphicsOpacityEffect, QGridLayout, \
                              QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout
from src.iface.styling.dynamic import *


class RightPaneStats(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Opacity animation for fade-in effect.
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_anim = QPropertyAnimation(self.opacity_effect, b'opacity')

        self.opacity_anim.setDuration(400)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.setGraphicsEffect(self.opacity_effect)

        self.l_base = QVBoxLayout(self)

        self.initUiHeader()
        self.initUiScore()
        self.initUiInfo()

    def initUiHeader(self):
        # The header contains the title and the subtitle.
        # Title - Name of the device.
        # Subtitle - Type of the device.
        self.title_label = QLabel(self)
        self.subtitle_label = QLabel(self)

        self.title_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.subtitle_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.title_label.setObjectName("rpane-title")
        self.subtitle_label.setObjectName("rpane-subtitle")

        self.l_base.addWidget(self.title_label)
        self.l_base.addWidget(self.subtitle_label)

    def initUiScore(self):
        # An out-of-10 score is given to each device.
        base = QFrame(self)
        base.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.l_base.addWidget(base, 80, Qt.AlignCenter)

        layout = QVBoxLayout(base)
        numoot_sublayout = QHBoxLayout()

        num_label = ScoreLerpLabel(base)
        oot_label = QLabel("/10", base)
        health_label = QLabel("Health Score", base)

        # Colors used: #f38ba8 and #a6e3a1
        num_label.setLerpBounds((243, 139, 168), (166, 227, 161))

        numoot_sublayout.addWidget(num_label)
        numoot_sublayout.addWidget(oot_label)

        layout.addLayout(numoot_sublayout)
        layout.addWidget(health_label, 0, Qt.AlignCenter)

        # These widgets are important.
        self.w_rpane_score_num = num_label
        self.w_rpane_score_oot = oot_label
        self.w_rpane_score_num.setObjectName("rpane-score-num")
        self.w_rpane_score_oot.setObjectName("rpane-score-oot")


    def initUiInfo(self):
        # More information about the device's maintenance records, etc.
        # Includes the following statistics:
        #  - Upcoming maintenance date recommended.
        #  - Estimated cost of maintenance.
        base = QFrame(self)
        base.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.l_base.addWidget(base)

        layout = QGridLayout(base)

        serv_hlabel = QLabel("<h2>Recommended Service Date</h2>", base)
        cost_hlabel = QLabel("<h2>Estimated Service Cost</h2>", base)
        serv_label = QLabel(base)
        cost_label = QLabel(base)

        serv_hlabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        cost_hlabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        serv_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        cost_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout.addWidget(serv_hlabel, 0, 0)
        layout.addWidget(cost_hlabel, 0, 1)
        layout.addWidget(serv_label, 1, 0)
        layout.addWidget(cost_label, 1, 1)

        # Add some bottom stretch (in pixels)
        self.l_base.addStretch(20)

        # These widgets are important.
        self.w_info_serv = serv_label
        self.w_info_cost = cost_label

    def setDeviceName(self, name):
        self.title_label.setText(name)

    def setDeviceType(self, name):
        self.subtitle_label.setText(name)

    def setDeviceScore(self, score):
        self.w_rpane_score_num.setTextAndLerp(str(score).zfill(2), score / 10)

    def setDeviceServiceDate(self, date):
        self.w_info_serv.setText(date)

    def setDeviceServiceCost(self, cost):
        self.w_info_cost.setText(cost)

    def applyToStackedLayout(self):
        self.parent().layout().setCurrentWidget(self)

        # Start a fading-in animation.
        self.opacity_anim.setStartValue(0.0)
        self.opacity_anim.setEndValue(0.999)
        self.opacity_anim.start()
