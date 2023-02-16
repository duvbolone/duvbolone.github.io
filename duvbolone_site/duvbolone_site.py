from pcconfig import config
import pynecone as pc
from duvbolone_site.pages import index, about

class State(pc.State):
    pass

pages = [index, about]

style = {
    "theme_color": "#FFFFFF",
    "font_family":"helvetica",
    "background_color": "rgb(30, 30, 30)",
    "color":"#FFFFFF",
    pc.Button: {
        "bg":"rgb(50, 50, 50)"
    }
}

app = pc.App(
    state=State,
    style = style
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
