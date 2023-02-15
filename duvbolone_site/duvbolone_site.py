from pcconfig import config
import pynecone as pc
from duvbolone_site.pages import index, about

class State(pc.State):
    pass


app = pc.App(
    state=State
    )

# Add state and page to the app.
app.add_page(index.index, route="/", title="Matt3o0's Website", image="/M27.png", description="My website. Caution, it's very questionable 💀")
app.add_page(about.about, route="/about", title="Matt3o0's Website", image="/M27.png", description="My website. Caution, it's very questionable 💀")
app.compile()
