import pynecone as pc
from duvbolone_site import duvbolone_site

def navBar(root):
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(
                    pc.image(src="/M27_cropped.png", width="5%", height="5%", box_shadow = "rgba(0, 0, 0, 0.3) 0px 3px 10px", border_radius="30px", _hover={"opacity": 0.85}),
                    pc.heading("Matt3o0", _hover={"opacity": 0.85}),
                ),
                href = "/"
            ),
            pc.spacer(),
            pc.hstack(
                pc.link(
                    pc.tooltip(
                        pc.button("About", _hover={"opacity": 0.85}),
                        label = "My about me page",
                        has_arrow = True
                    ),
                    href = "/about"
                ),
                pc.link(
                    pc.tooltip(
                        pc.button("GitHub", _hover={"opacity": 0.85}),
                        label = "My GitHub profile",
                        has_arrow = True
                    ),
                    href = "https://github.com/duvbolone"
                ),
                pc.link(
                    pc.tooltip(
                        pc.button("Discord", _hover={"opacity": 0.85}),
                        label = "My Discord profile",
                        has_arrow = True
                    ),
                    href = "https://discord.com/users/668874138160594985"
                ),
                pc.tooltip(
                    pc.button(pc.icon(tag="MoonIcon"), on_click=pc.toggle_color_mode, _hover={"opacity": 0.85}),
                    label = "Toggle color mode"
                )
            ),
            padding = "6px",
        ),
        top = "0px",
        position = "sticky",
        background_color = "rgba(0, 0, 0, 0.1)",
        backdrop_filter="blur(2px)",
        box_shadow = "rgba(0, 0, 0, 0.1) 0px 4px 8px"
    )