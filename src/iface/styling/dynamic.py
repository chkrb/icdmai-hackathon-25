from PySide6.QtWidgets import QLabel


class ScoreLerpLabel(QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.lerp_rgb_1 = (0, 0, 0)
        self.lerp_rgb_2 = (0, 0, 0)

    def setLerpBounds(self, color1, color2):
        self.lerp_rgb_1 = color1
        self.lerp_rgb_2 = color2

    def setTextAndLerp(self, text, value):
        color_r = self.lerp_rgb_1[0] * (1 - value) + self.lerp_rgb_2[0] * value
        color_g = self.lerp_rgb_1[1] * (1 - value) + self.lerp_rgb_2[1] * value
        color_b = self.lerp_rgb_1[2] * (1 - value) + self.lerp_rgb_2[2] * value

        self.setText(text)
        self.setStyleSheet(f"color: rgb({color_r}, {color_g}, {color_b})")
