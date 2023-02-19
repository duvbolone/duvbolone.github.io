import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar

route = "/404"
title = "404 - Matt3o0's Website"
image = "/M27.png"
description = "This is a 404 page, nothing interesting here 💀"


def page():
    return pc.box(
        pc.vstack(
            pc.heading("Error 404", font_size="900%", padding="30px"),
            pc.hstack(
                pc.heading("Page not found", color="rgb(220, 220, 220)"),
            ),
            pc.spacer(padding="50px"),
            pc.hstack(
                pc.icon(tag="ArrowDownIcon", font_size="250%"),
                pc.heading("See below for all available pages"),
                pc.icon(tag="ArrowDownIcon", font_size="250%"),
            ),
        ),
        pc.spacer(padding="200px"),
        footBar('/')
    )
