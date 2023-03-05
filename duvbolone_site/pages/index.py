import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar

route = "/"
title = "Home - Matt3o0's Website"
image = "/M27.png"
description = "The website that's supposed to tell you a little bit more about Matt3o0"
meta = [
    {"name":"theme-color", "content":"rgb(0, 0, 5)"}
]


def page():
    return pc.box(
        pc.box(
            navBar("/"),
            pc.center(
                pc.vstack(
                    pc.text("", id="topOfPage"),
                    pc.spacer(padding="2%"),
                    pc.heading(
                        "Welcome wanderer!",
                        background_image="linear-gradient(60deg, rgb(250, 0, 0)10%, rgb(0, 0, 250))",
                        background_clip="text",
                        # text_shadow="rgb(0,0,0,0.5) -4px 4px 5px",
                        font_size=["490%","500%","500%","500%"],
                        filter="blur(0px)",
                        width=["92%", "92%", "90%", "90%"]
                    ),
                    pc.heading(
                        "This is Matt3o0's website, let me show you what to do here.", width=["90%", "90%", "90%", "100%"]
                    ),
                ),
            ),
            pc.tablet_and_desktop(
                pc.responsive_grid(
                    pc.box(
                        pc.text("Get to know Matt3o0 a little better on the about me page.",
                                padding="20px", font_size="150%"),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.icon(tag="link"), "About Me", bg="rgb(5, 5, 55)",
                                        _hover={"opacity": 0.85}),
                                label="My about me page",
                                has_arrow=True,
                            ),
                            href="/about",
                            padding="20px",
                            position="relative",
                            bottom="20px"
                        ),
                        height="auto",
                        width="auto",
                        border_radius="2em",
                        bg="rgba(20, 20, 70)",
                        opacity=1,
                        box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                        backdrop_filter="blur(2px)",
                    ),
                    pc.box(
                        pc.text("Check out Matt3o0's projects",
                                padding="20px", font_size="150%"),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.icon(tag="link"), "Projects", bg="rgb(5, 5, 55)",
                                        _hover={"opacity": 0.85}),
                                label="My project(s)",
                                has_arrow=True,
                            ),
                            href="/projs",
                            padding="20px",
                            position="relative",
                            #bottom="20px"
                        ),
                        height="auto",
                        width="auto",
                        border_radius="2em",
                        bg="rgba(20, 20, 70)",
                        opacity=1,
                        box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                        backdrop_filter="blur(2px)",
                    ),
                    pc.box(
                        pc.text("Check out the source code of this website",
                                padding="20px", font_size="150%"),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.icon(tag="link"), "Website source code", bg="rgb(5, 5, 55)",
                                        _hover={"opacity": 0.85}),
                                label="Source code of this website",
                                has_arrow=True,
                            ),
                            href="https://github.com/duvbolone/duvbolone.github.io",
                            is_external=True,
                            padding="20px",
                            position="relative",
                            bottom="20px"
                        ),
                        height="auto",
                        width="auto",
                        border_radius="2em",
                        bg="rgba(20, 20, 70)",
                        opacity=1,
                        box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                        backdrop_filter="blur(2px)",
                    ),
                    columns=[3],
                    spacing="10",
                    padding_left="10%",
                    padding_right="10%",
                    padding_top="3%"
                )
            ),
            pc.mobile_only(
                pc.responsive_grid(
                    pc.box(
                        pc.text("Get to know Matt3o0 a little better on the about me page.",
                                padding="20px", font_size="150%", ),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.icon(tag="link"), "About Me", bg="rgb(5, 5, 55)",
                                        _hover={"opacity": 0.85}),
                                label="My about me page",
                                has_arrow=True,
                            ),
                            href="/about",
                            padding="20px",
                            position="relative",
                            bottom="15px"
                        ),
                        height="auto",
                        width="auto",
                        border_radius="2em",
                        bg="rgba(20, 20, 70)",
                        opacity=1,
                        box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                        backdrop_filter="blur(2px)",
                    ),
                    pc.box(
                        pc.text("Check out Matt3o0's projects",
                                padding="20px", font_size="150%"),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.icon(tag="link"), "Projects", bg="rgb(5, 5, 55)",
                                        _hover={"opacity": 0.85}),
                                label="My project(s)",
                                has_arrow=True,
                            ),
                            href="/projs",
                            padding="20px",
                            position="relative",
                            bottom="15px"
                        ),
                        height="auto",
                        width="auto",
                        border_radius="2em",
                        bg="rgba(20, 20, 70)",
                        opacity=1,
                        box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                        backdrop_filter="blur(2px)",
                    ),
                    pc.box(
                        pc.text("Check out the source code of this website",
                                padding="20px", font_size="150%"),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.icon(tag="link"), "Website source code", bg="rgb(5, 5, 55)",
                                        _hover={"opacity": 0.85}),
                                label="Source code of this website",
                                has_arrow=True,
                            ),
                            href="https://github.com/duvbolone/duvbolone.github.io",
                            is_external=True,
                            padding="20px",
                            position="relative",
                            bottom="15px"
                        ),
                        height="auto",
                        width="auto",
                        border_radius="2em",
                        bg="rgba(20, 20, 70)",
                        opacity=1,
                        box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                        backdrop_filter="blur(2px)",
                    ),
                    columns=[0],
                    spacing="10",
                    padding_left="10%",
                    padding_right="10%",
                    padding_top="3%"
                )
            ),
            background_image="linear-gradient(0deg, rgb(10, 10, 60)10%, rgb(0, 0, 5))",
            height="150vh",
        ),
        footBar('/')
    )
