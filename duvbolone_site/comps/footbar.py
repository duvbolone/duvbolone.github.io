import pynecone as pc
from duvbolone_site.comps.state import State


def footBar(root):
    return pc.hstack(
        pc.image(src="/M27_cropped.png", width="7%", height="7%",
                box_shadow="rgba(0, 0, 0, 0.6) -5px 5px 10px", border_radius="50px", position="relative", bottom="20px", left="20px"),
        pc.vstack(
            pc.heading("Pages", font_size="100%"),
            pc.link(
                pc.text("Home", color="gray"),
                href="/"
            ),
            pc.link(
                pc.text("About", color="gray"),
                href="/about"
            ),
            pc.link(
                pc.text("Projects", color="gray"),
                href="/projs"
            ),
            z_index=1,
            bg="transparent",
            padding_left=["50px","75px", "100px", "200px"],
            padding_top="25px",
            height="200px"
        ),
        pc.spacer(),
        pc.link(
                pc.button("Back to top", pc.icon(tag="ArrowUpIcon")),
                href=f"{root}#topOfPage",
                padding_right = "10px",
                padding_top = "130px"
                ),
        bg="rgb(10, 10, 15)"
    )
