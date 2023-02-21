from pcconfig import config
import pynecone as pc
from duvbolone_site.pages import index, about, projs, error404
from duvbolone_site.comps.state import State

pages = [index, about, projs]

style = {
    #"theme_color": "#FFFFFF", #<meta name="theme-color" content="rgb(30, 30, 30)"/>
    #"font_family":"monospace",
    "bg": "linear-gradient(0deg, rgb(0, 0, 0), rgb(30, 30, 30))",
    "background_color":"rgb(10, 10, 15)",
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
app.add_custom_404_page(
        error404.page(),
        image = "/M27.png",
        description = "Error 404 page, noting interesting here.",
        title="Error 404 - Matt3o0's website"
    )
app.compile()
