import pynecone as pc
from duvbolone_site import duvbolone_site

def navBar(root):
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(
                    pc.mobile_only(
                        pc.image(src="/M27_cropped.png", width="15%", height="15%", box_shadow = "rgba(0, 0, 0, 0.3) 0px 3px 10px", border_radius="30px"),
                    ),
                    pc.tablet_and_desktop(
                        pc.image(src="/M27_cropped.png", width="8%", height="8%", box_shadow = "rgba(0, 0, 0, 0.3) 0px 3px 10px", border_radius="30px"),
                        pc.heading("Matt3o0", font_size = "150%"),
                    ),
                    _hover={"opacity": 0.85}
                ),
                href = "/"
            ),
            pc.spacer(),
            pc.tablet_and_desktop(
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
                            pc.button(pc.image(src="/icons/github-mark-white.png", height = "20px", width = "20px"), _hover={"opacity": 0.85}),
                            label = "My GitHub profile",
                            has_arrow = True
                        ),
                        href = "https://github.com/duvbolone"
                    ),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.image(src="/icons/discord-mark-white.png", height = "auto", width = "20px"), _hover={"opacity": 0.85}),
                            label = "My Discord profile",
                            has_arrow = True
                        ),
                        href = "https://discord.com/users/668874138160594985"
                    )
                ),
            ),
            pc.mobile_only(
                pc.breadcrumb(
                    pc.breadcrumb_item(
                        pc.breadcrumb_link(
                            "About",
                            href = "/about"
                        ),
                    ),
                    pc.breadcrumb_item(
                        pc.breadcrumb_link(
                            "GitHub",
                            href = "https://github.com/duvbolone"
                        ),
                    ),
                    pc.breadcrumb_item(
                        pc.breadcrumb_link(
                            "Discord",
                            href = "https://discord.com/users/668874138160594985"
                        ),
                    ),
                    separator = "|",
                    #separator_margin = "0px"
                ),
                width = "100%"
            ),
            padding = "6px",
        ),
        top = "0px",
        position = "sticky",
        background_color = "rgba(0, 0, 0, 0.1)",
        backdrop_filter="blur(2px)",
        box_shadow = "rgba(0, 0, 0, 0.1) 0px 4px 8px",
        z_index = 99
    )