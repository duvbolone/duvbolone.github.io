import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar
from duvbolone_site.comps.state import State

route = "/[any]"
title = "404 - Matt3o0's Website"
image = "/M27.png"
description = "This is a 404 page, nothing here 💀"


def page():
    url = State.get_url
    return pc.box(
        pc.vstack(
            pc.heading("Error 404", font_size="900%", padding="30px"),
            pc.hstack(
                pc.heading("Page", color="rgb(220, 220, 220)"),
                pc.heading(url, color="rgb(160, 160, 160)"),
                pc.heading("not found", color="rgb(220, 220, 220)")
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
