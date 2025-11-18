# Library: Kivy
# Baris kode: 26
# Instalasi: pip install "kivy[base]"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (500, 300)
Window.clearcolor = (0.95, 0.96, 0.98, 1)


class KivyHelloApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=24, spacing=18)
        layout.add_widget(Label(text="Hello World!", font_size="32sp",
                                bold=True, color=(0.1, 0.1, 0.1, 1)))
        btn = Button(text="Tap Me", size_hint=(1, None), height=60,
                     font_size="18sp", background_normal="",
                     background_color=(0.2, 0.4, 0.9, 1))
        btn.bind(on_release=lambda *_: setattr(btn, "text", "Enjoy your day!"))
        layout.add_widget(btn)
        layout.add_widget(Label(text="Centered & cozy layout", font_size="16sp",
                                color=(0.3, 0.3, 0.3, 1)))
        return layout


if __name__ == "__main__":
    KivyHelloApp().run()

