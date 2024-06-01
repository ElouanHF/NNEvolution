import pyglet


class WindowManager:
    def __init__(self):
        # Window arguments
        config_kwarg = {
            "resizable": True,
            "style": pyglet.window.Window.WINDOW_STYLE_DEFAULT,
            "caption": "NN Evolution",
            "vsync": True
        }
        config_arg = [1280, 720]

        # Window setting methods
        self.window = pyglet.window.Window(*config_arg, **config_kwarg)
        icon1 = pyglet.image.load('Graphics/NNE_Icon_16.png')
        icon2 = pyglet.image.load('Graphics/NNE_Icon_16.png')
        self.window.set_icon(icon1, icon2)

        # Background Shapes
        self.scale_factor = 1.0
        self.batch = pyglet.graphics.Batch()
        back_sq_conf = {
            "x": -5000,
            "y": -5000,
            "width": 10000,
            "height": 10000,
            "color": (80, 80, 80),
            "batch": self.batch
        }
        self.field_sq_size = 500
        field_sq_conf = {
            "x": self.window.width // 2 - self.field_sq_size // 2,
            "y": self.window.height // 2 - self.field_sq_size // 2,
            "width": self.field_sq_size,
            "height": self.field_sq_size,
            "color": (200, 200, 200),
            "batch": self.batch
        }
        self.back_sq = pyglet.shapes.Rectangle(**back_sq_conf)
        self.field_sq = pyglet.shapes.Rectangle(**field_sq_conf)

        # Other set up and run
        self.set_up_event_handlers()
        pyglet.app.run()

    def set_up_event_handlers(self):
        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()

        @self.window.event
        def on_resize(width, height):
            # Re-center the square
            self.field_sq.x = width // 2 - self.field_sq_size // 2
            self.field_sq.y = height // 2 - self.field_sq_size // 2

        # Zooming in not currently implemented
        @self.window.event
        def on_mouse_scroll(x, y, scroll_x, scroll_y):
            # Update the scale factor based on the scroll direction
            if scroll_y > 0:
                self.scale_factor *= 1.1  # Zoom in
            elif scroll_y < 0:
                self.scale_factor /= 1.1  # Zoom out
