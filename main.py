from jnius import autoclass
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Tạo label
        label = Label(text="Trạng thái thiết bị")

        # Lấy trạng thái thiết bị
        screen = jnius.autoclass("android.view.Window").getDecorView().getSystemUiVisibility()

        # Kiểm tra xem màn hình đang khóa hay không
        if screen & jnius.autoclass("android.view.View").SYSTEM_UI_FLAG_LOW_PROFILE:
            label.text = "Màn hình đang khóa"
        else:
            label.text = "Màn hình đang mở"

        # Style label
        label.pos = (100, 100)
        label.halign = "left"
        label.valign = "top"
        return label

app = MyApp()
app.run()