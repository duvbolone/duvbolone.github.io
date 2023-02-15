import pynecone as pc
from duvbolone_site.comps.navbar import navBar

def index():
    return pc.box(
        navBar("/"),
        pc.vstack(
            pc.hstack(
                pc.heading("⚠️", color="rgb(200, 170, 0)", _hover={"color": "rgb(210, 185, 0)"}),
                pc.heading("Work In Progress", color = "gray"),
                pc.circular_progress(
                    is_indeterminate = True,
                    color = "white",
                    track_color = "gray"
                    ),
                padding = "40px",
                _hover={"opacity": 0.85}
            ),
            pc.markdown("*You can check the source code on my **[GitHub profile](https://github.com/duvbolone/duvbolone.github.io)** if interested*", padding = "40px"),
        )
    )