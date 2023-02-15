from pcconfig import config
import pynecone as pc
from duvbolone_site.pages import index

class State(pc.State):
    """The app state."""
    pass

app = pc.App(
    state=State
    )

# Add state and page to the app.
app.add_page(index.index, route="/", title="Matt3o0's Website", image="/M27.png")
app.compile()
