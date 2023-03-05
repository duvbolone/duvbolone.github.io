import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar

route = "/404"
title = "404 - Matt3o0's Website"
image = "/M27.png"
description = "This is a 404 page, nothing interesting here 💀"
meta = [
    {"name":"theme-color", "content":"rgb(22, 22, 22)"}
]

def page():
    return pc.box(
        pc.vstack(
            pc.heading("Oops, seems like you took a wrong turn.", font_size="500%", padding="60px", id="topOfPage"),
            pc.link(
                pc.button(pc.icon(tag="arrow_back"), "Return to Home", font_size="190%", _hover={"opacity": 0.85}),
                href="/"
                ),
            pc.spacer(padding="50px"),
            pc.hstack(
                pc.heading("Error 404: Page not found", color="rgb(220, 220, 220)"),
            ),
        ),
        pc.spacer(padding="200px"),
        footBar('/e')
    )
