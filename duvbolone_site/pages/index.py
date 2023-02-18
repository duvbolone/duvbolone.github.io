import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar

route = "/"
title = "Matt3o0's Website"
image = "/M27.png"
description = "My website, supposed to tell you something about me and more."


def page():
    return pc.box(
        navBar("/"),
        pc.tablet_and_desktop(
            pc.vstack(
                pc.heading(
                    "Welcome wanderer!",
                    background_image="linear-gradient(60deg, rgb(250, 0, 0)10%, rgb(0, 0, 250))",
                    background_clip="text",
                    # text_shadow="rgb(0,0,0,0.5) -4px 4px 5px",
                    font_size="500%",
                    filter="blur(0px)",
                    id="topOfPage"
                ),
                pc.heading(
                    "This is Matt3o0's website, let me show you what to do here.")
            ),
            pc.hstack(
                pc.box(
                    pc.text("Get to know Matt3o0 a little better on his about me page.",
                            padding="20px", font_size="150%"),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.icon(tag="LinkIcon"), "About Me", bg="rgb(5, 5, 55)",
                                      _hover={"opacity": 0.85}),
                            label="My about me page",
                            has_arrow=True,
                        ),
                        href="/about",
                        position="relative",
                        padding_left="15px",
                        padding_bottom="15px"
                    ),
                    height="230px",
                    width="300px",
                    border_radius="2em",
                    bg="rgba(20, 20, 70)",
                    opacity=1,
                    box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                    backdrop_filter="blur(2px)",
                    position="relative",
                    left="300px",
                    top="100px"
                ),
                pc.box(
                    pc.text("Check out Matt3o0's projects",
                            padding="20px", font_size="150%"),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.icon(tag="LinkIcon"), "Projects", bg="rgb(5, 5, 55)",
                                      _hover={"opacity": 0.85}),
                            label="My project(s)",
                            has_arrow=True,
                        ),
                        href="/projs",
                        position="relative",
                        padding_left="15px",
                        padding_bottom="15px"
                    ),
                    height="230px",
                    width="300px",
                    border_radius="2em",
                    bg="rgba(20, 20, 70)",
                    opacity=1,
                    box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                    backdrop_filter="blur(2px)",
                    position="relative",
                    left="350px",
                    top="100px"
                ),
                pc.box(
                    pc.text("Check out the source code of this website!",
                            padding="20px", font_size="130%"),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.icon(tag="LinkIcon"), "Website source code", bg="rgb(5, 5, 55)",
                                      _hover={"opacity": 0.85}),
                            label="Source code of this website",
                            has_arrow=True,
                        ),
                        href="https://github.com/duvbolone/duvbolone.github.io",
                        position="relative",
                        padding_left="15px",
                        padding_bottom="15px",
                        is_external=True
                    ),
                    height="230px",
                    width="300px",
                    border_radius="2em",
                    bg="rgba(20, 20, 70)",
                    opacity=1,
                    box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                    backdrop_filter="blur(2px)",
                    position="relative",
                    left="400px",
                    top="100px"
                )
            ),
            background_image="linear-gradient(0deg, rgb(10, 10, 60)10%, rgb(0, 0, 5))",
            height="150vh"
        ),
        pc.mobile_only(
            pc.vstack(
                pc.alert(
                        pc.alert_icon(),
                        pc.alert_title("Warning: This website is NOT optimised for mobile devices.", color="black"),
                        status="warning",
                        variant="subtle",
                        width="100%",
                        height="50px"
                ),
                pc.heading(
                    "Welcome wanderer!",
                    background_image="linear-gradient(60deg, rgb(250, 0, 0)10%, rgb(0, 0, 250))",
                    background_clip="text",
                    # text_shadow="rgb(0,0,0,0.5) -4px 4px 5px",
                    font_size="490%",
                    filter="blur(0px)",
                    width="90%"
                ),
                pc.heading(
                    "This is Matt3o0's website, let me show you what to do here.", width="90%")
            ),
            pc.hstack(
                pc.box(
                    pc.text("Get to know Matt3o0 a little better on his about me page.",
                            padding="20px", font_size="130%"),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.icon(tag="LinkIcon"), "About Me", bg="rgb(5, 5, 55)",
                                      _hover={"opacity": 0.85}),
                            label="My about me page",
                            has_arrow=True,
                        ),
                        href="/about",
                        position="relative",
                        padding_left="15px",
                        padding_bottom="15px"
                    ),
                    height="350px",
                    width="2000px",
                    border_radius="2em",
                    bg="rgba(20, 20, 70)",
                    opacity=1,
                    box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                    backdrop_filter="blur(2px)",
                    position="relative",
                    left="30px",
                    top="50px"
                ),
                pc.box(
                    pc.text("Check out Matt3o0's projects",
                            padding="20px", font_size="130%"),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.icon(tag="LinkIcon"), "Projects", bg="rgb(5, 5, 55)",
                                      _hover={"opacity": 0.85}),
                            label="My project(s)",
                            has_arrow=True,
                        ),
                        href="/projs",
                        position="relative",
                        padding_left="15px",
                        padding_bottom="15px"
                    ),
                    height="350px",
                    width="2000px",
                    border_radius="2em",
                    bg="rgba(20, 20, 70)",
                    opacity=1,
                    box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                    backdrop_filter="blur(2px)",
                    position="relative",
                    left="60px",
                    top="50px"
                ),
                pc.box(
                    pc.text("Check out the source code of this website!",
                            padding="20px", font_size="130%"),
                    pc.link(
                        pc.tooltip(
                            pc.button(pc.icon(tag="LinkIcon"), "Website source code", bg="rgb(5, 5, 55)",
                                      _hover={"opacity": 0.85}),
                            label="Source code of this website",
                            has_arrow=True,
                        ),
                        href="https://github.com/duvbolone/duvbolone.github.io",
                        is_external=True,
                        position="relative",
                        padding_left="15px",
                        padding_bottom="15px"
                    ),
                    height="350px",
                    width="2000px",
                    border_radius="2em",
                    bg="rgba(20, 20, 70)",
                    opacity=1,
                    box_shadow="rgb(0, 0, 0, .2) -15px 20px 15px",
                    backdrop_filter="blur(2px)",
                    position="relative",
                    left="-200px",
                    top="450px"
                )
            ),
            background_image="linear-gradient(0deg, rgb(10, 10, 60)10%, rgb(0, 0, 5))",
            height="150vh"
        ),
        footBar('/')
    )
