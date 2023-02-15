from pcconfig import config
import pynecone as pc
from duvbolone_site.pages import index, about

def toggleColor():
        pc.toggle_color_mode

class State(pc.State):
    theme = "light"

    def toggleColor(self):
        pc.toggle_color_mode
        #self.theme = not self.theme


app = pc.App(
    state=State
    )

# Add state and page to the app.
app.add_page(index.index, route="/", title="Matt3o0's Website", image="/M27.png", description="My website. Caution, it's very questionable 💀", on_load=toggleColor)
app.add_page(about.about, route="/about", title="Matt3o0's Website", image="/M27.png", description="My website. Caution, it's very questionable 💀", on_load=toggleColor)
app.compile()
