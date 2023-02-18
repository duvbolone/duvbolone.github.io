import pynecone as pc
from duvbolone_site import duvbolone_site


def navBar(root):
    return pc.box(
        pc.hstack(
            pc.link(
                pc.mobile_and_tablet(
                    pc.image(src="/M27_cropped.png", width="30%", height="30%",
                             box_shadow="rgba(0, 0, 0, 0.3) 0px 3px 10px", border_radius="30px"),
                    _hover={"opacity": .7}
                ),
                pc.desktop_only(
                    pc.hstack(
                        pc.image(src="/M27_cropped.png", width="9%", height="9%",
                                 box_shadow="rgba(0, 0, 0, 0.3) 0px 3px 10px", border_radius="30px"),
                        pc.heading("Matt3o0", font_size="230%"),
                        _hover={"opacity": .7}
                    )
                ),
                href=root
            ),
            pc.spacer(),
            pc.tablet_and_desktop(
                pc.hstack(
                    pc.link(
                        pc.tooltip(
                            pc.button("Projects", _hover={"opacity": 0.85}),
                            label="My projects",
                            has_arrow=True
                        ),
                        href="/projs"
                    ),
                    pc.link(
                        pc.tooltip(
                            pc.button("About", _hover={"opacity": 0.85}),
                            label="My about me page",
                            has_arrow=True
                        ),
                        href="/about"
                    ),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.image(
                                src="/icons/github-mark-white.png", height="1.5em"), _hover={"opacity": 0.85}),
                            label="My GitHub profile",
                            has_arrow=True
                        ),
                        href="https://github.com/duvbolone",
                        is_external=True
                    ),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.image(
                                src="/icons/discord-mark-white.png", height="1.5em"), _hover={"opacity": 0.85}),
                            label="My Discord profile",
                            has_arrow=True
                        ),
                        href="https://discord.com/users/668874138160594985",
                        is_external=True
                    )
                ),
            ),
            pc.mobile_only(
                pc.hstack(
                    pc.link("Projects", href="/projs"),
                    pc.text(" "),
                    pc.link("About", href="/about"),
                    pc.text(" "),
                    pc.link("Github", href="https://github.com/duvbolone",is_external=True),
                    pc.text(" "),
                    pc.link("Discord", href="https://discord.com/users/668874138160594985",is_external=True),
                    font_size="110%",
                    padding="2px"
                ),
            ),
            padding="6px",
        ),
        top="0px",
        position="sticky",
        background_color="rgba(0, 0, 0, 0.2)",
        backdrop_filter="blur(4px)",
        box_shadow="rgba(0, 0, 0, 0.1) 0px 10px 13px",
        z_index=99
    )
