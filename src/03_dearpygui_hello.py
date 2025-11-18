# Library: Dear PyGui
# Baris kode: 28
# Instalasi: pip install dearpygui

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Dear PyGui Hello GUI", width=500, height=300)

with dpg.theme() as dark_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 33, 40))
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 12)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10)

with dpg.window(label="Hello Panel", width=480, height=260, no_resize=True):
    dpg.add_spacer(height=10)
    dpg.add_text("Hello World!", color=(230, 230, 240), bullet=False)
    dpg.add_separator()
    dpg.add_button(label="Greet Me", width=160, height=40,
                   callback=lambda: dpg.configure_item("status", default_value="Stay awesome!"))
    dpg.add_text("Press the button to smile :)", tag="status", color=(160, 180, 200))

dpg.bind_theme(dark_theme)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(dpg.last_item(), True)
dpg.start_dearpygui()
dpg.destroy_context()

