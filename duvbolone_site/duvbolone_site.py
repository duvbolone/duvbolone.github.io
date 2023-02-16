from pcconfig import config
import pynecone as pc
from duvbolone_site.pages import index, about

class State(pc.State):
    pass

pages = [index, about]

app = pc.App(
    state=State,
    theme_color = "#FFFFFF"
    )

for page in pages:
    app.add_page(
        page.page(),
        route = page.route,
        title = page.title,
        image = page.image,
        description = page.description,
        )

# Add state and page to the app.
app.compile()
