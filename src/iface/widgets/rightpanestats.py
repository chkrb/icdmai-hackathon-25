from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QFrame, QGraphicsOpacityEffect, QGridLayout, \
                              QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout


class RightPaneStats(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_anim = QPropertyAnimation(self.opacity_effect, b'opacity')

        self.opacity_anim.setDuration(400)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.setGraphicsEffect(self.opacity_effect)

        self.wlayout = QVBoxLayout(self)

        self.title_label = QLabel(self)
        self.title_label.setObjectName("rpane-title")
        self.title_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.wlayout.addWidget(self.title_label)

        self.subtitle_label = QLabel(self)
        self.subtitle_label.setObjectName("rpane-subtitle")
        self.subtitle_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.wlayout.addWidget(self.subtitle_label)

        # Includes the following statistics:
        #  - A device health score out of 10.
        #  - Upcoming maintenance date recommended (with estimated cost).
        self.content_frame = QFrame(self)
        self.wlayout.addWidget(self.content_frame)
        self.content_layout = QGridLayout(self.content_frame)

        self.score_frame = QFrame(self.content_frame)
        self.score_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.score_layout = QHBoxLayout(self.score_frame)
        self.content_layout.addWidget(self.score_frame, 2, 0)

        self.score_label = QLabel(self.score_frame)
        self.score_label.setObjectName("rpane-score")
        self.score_layout.addWidget(self.score_label)

        self.score_oot_label = QLabel("/10", self.score_frame)
        self.score_oot_label.setObjectName("rpane-score-oot")
        self.score_layout.addWidget(self.score_oot_label)

        self.serv_frame = QFrame(self.content_frame)
        self.serv_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.serv_layout = QVBoxLayout(self.serv_frame)
        self.content_layout.addWidget(self.serv_frame, 2, 1)

        self.serv_label = QLabel("<h1>Recommended Service</h1>", self.serv_frame)
        self.serv_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.serv_layout.addWidget(self.serv_label)

        self.serv_label = QLabel(self.serv_frame)
        self.serv_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.serv_layout.addWidget(self.serv_label)

    def setDeviceName(self, name):
        self.title_label.setText(name)

    def setDeviceType(self, name):
        self.subtitle_label.setText(name)

    def setDeviceScore(self, score):
        self.score_label.setText(str(score).zfill(2))

    def setDeviceService(self, date):
        self.serv_label.setText("in around " + date)

    def applyToStackedLayout(self):
        self.parent().layout().setCurrentWidget(self)

        # Start a fading-in animation.
        self.opacity_anim.setStartValue(0.0)
        self.opacity_anim.setEndValue(0.999)
        self.opacity_anim.start()
