#cad2nza/Spring26COMP1020A8

import math
import sys
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

        self.current_frame = 0
        self.is_running = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

        self.setupUI()

    def setupUI(self):
        frame = QFrame()
        layout = QHBoxLayout()
#sprite
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_frame_display()
        layout.addWidget(self.label)
#FPS Label
        self.fps_label = QLabel("FPS: 1")
        self.fps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fps_label)
# slider
        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(1)
        self.slider.setTickPosition(QSlider.TickPosition.TicksLeft)  # ticks on the left side
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.update_fps)
        layout.addWidget(self.slider)
#Ticks
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
#slider value change signal
        self.slider.valueChanged.connect(self.update_fps)
        layout.addWidget(self.slider)

        button_layout = QVBoxLayout()
#start/stop button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.toggle_animation)
        button_layout.addWidget(self.start_button)

        frame.setLayout(layout)
        self.setCentralWidget(frame)
#pause button
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_animation)
        button_layout.addWidget(self.pause_button)
#exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(button_layout)
        frame.setLayout(layout)
        self.setCentralWidget(frame)

    def next_frame(self):
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.update_frame_display()

    def update_frame_display(self):
        pixmap = self.frames[self.current_frame]
        self.label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))

    def update_fps(self, value):
        self.fps_label.setText(f"FPS: {value}")

        if self.is_running:
            interval = int(1000 / value)  # milliseconds per frame
            self.timer.start(interval)

    def toggle_animation(self):
        if not self.is_running:
            fps = self.slider.value()
            interval = int(1000 / fps)

            self.timer.start(interval)
            self.start_button.setText("Stop")
            self.is_running = True
        else:
            self.timer.stop()
            self.start_button.setText("Start")
            self.is_running = False
            self.current_frame = 0
            self.update_frame_display()

    def pause_animation(self):
        if self.is_running:
            self.timer.stop()
            self.start_button.setText("Start")
            self.is_running = False

    def exit(self):
        sys.exit()


def main():
    app = QApplication([])
    window = SpritePreview()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()