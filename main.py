#cad2nza/Spring26COMP1020A8

import math
import os
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))
    return frames


class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")

        self.num_frames = 21
        self.frames = load_sprite('spriteImages', self.num_frames)

        self.setupUI()

    def setupUI(self):
        frame = QFrame()
        layout = QVBoxLayout()


        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        if self.frames:
            self.label.setPixmap(self.frames[0].scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))

        layout.addWidget(self.label)


        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.num_frames - 1)


        self.lcd = QLCDNumber()
        self.lcd.setMinimumHeight(60)


        self.slider.valueChanged.connect(self.update_frame)
        self.slider.valueChanged.connect(self.lcd.display)

        layout.addWidget(self.slider)
        layout.addWidget(self.lcd)

        frame.setLayout(layout)
        self.setCentralWidget(frame)


    def update_frame(self, value):
        pixmap = self.frames[value]
        self.label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))


def main():
    app = QApplication([])
    window = SpritePreview()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()