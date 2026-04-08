#cad2nza/Spring26COMP1020A8

import math
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
        layout = QVBoxLayout()
#sprite
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_frame_display()
        layout.addWidget(self.label)
#FPS Label
        self.fps_label = QLabel("FPS: 1")
        self.fps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fps_label)
#Slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(1)
#Ticks
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
#slider value change signal
        self.slider.valueChanged.connect(self.update_fps)
        layout.addWidget(self.slider)
#start/stop button
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.toggle_animation)
        layout.addWidget(self.button)

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
            self.button.setText("Stop")
            self.is_running = True
        else:
            self.timer.stop()
            self.button.setText("Start")
            self.is_running = False


def main():
    app = QApplication([])
    window = SpritePreview()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()