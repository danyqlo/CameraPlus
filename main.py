from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2


class CameraLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buffer = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.camera_view.texture = texture

    def capture_image(self):
        ret, frame = self.capture.read()
        if ret:
            cv2.imwrite("captured_image.png", frame)


class CameraApp(App):
    def build(self):
        return CameraLayout()


if __name__ == '__main__':
    CameraApp().run()
