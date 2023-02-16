import pynecone as pc
from duvbolone_site.comps.navbar import navBar

route = "/"
title = "Matt3o0's Website"
image = "/M27.png"
description = "My website, supposed to tell you something about me and more."

def page():

    return pc.box(
        navBar("/"),
        pc.vstack(
            pc.hstack(
                pc.heading("⚠️", color="rgb(200, 180, 0)", _hover={"color": "rgb(210, 185, 0)"}),
                pc.heading("Work In Progress", color = "gray"),
                pc.circular_progress(
                    is_indeterminate = True,
                    color = "rgb(150, 150, 150)",
                    track_color = "transparent"
                    ),
                padding = "40px",
                _hover={"opacity": 0.85}
            ),
            pc.markdown("*You can check the source code on my **[GitHub profile](https://github.com/duvbolone/duvbolone.github.io)** if interested*", padding = "40px"),
            pc.skeleton_text(
                    no_of_lines = 8,
                    width = "40%",
                    height = "20px",
                    speed = 1.5
                    ),
        )
    )