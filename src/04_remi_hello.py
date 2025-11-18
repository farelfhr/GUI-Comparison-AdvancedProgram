# Library: Remi
# Baris kode: 26
# Instalasi: pip install remi

from remi import gui, start, App


class RemiHello(App):
    def main(self):
        box = gui.VBox(width=500, height=300,
                       style="margin:auto; padding:24px; background:#f8fafc; "
                             "justify-content:center; align-items:center;")
        label = gui.Label("Hello World!", style="font-size:32px; font-weight:700; color:#1f2933;")
        button = gui.Button("Press Me", style="font-size:18px; padding:10px 24px;")
        status = gui.Label("Ready to capture the screen ✨", style="margin-top:10px; color:#4b5563;")
        button.onclick.do(lambda *_: status.set_text("Great screenshot!"))
        box.append(label)
        box.append(button)
        box.append(status)
        return box


if __name__ == "__main__":
    start(RemiHello, address="0.0.0.0", port=0, multiple_instance=False,
          start_browser=True, debug=False)

