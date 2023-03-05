import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar

route = "/projs"
title = "Projects - Matt3o0's Website"
image = "/M27.png"
description = "The website that's supposed to tell you a little bit more about Matt3o0"
meta = [{"name": "theme-color", "content": "rgb(22, 22, 22)"}]


def page():
    return pc.box(
        navBar("/"),
        pc.spacer(id="topOfPage", padding="2%"),
        pc.vstack(
            pc.heading(
                "Projects",
                font_size="300%",
                padding="30px",
            ),
            pc.link(
                pc.markdown("- **ClearFly**"),
                href="/projs#clearfly",
            ),
            pc.link(
                pc.markdown("- **WingFlex Studios**"),
                href="/projs#wingflex",
            ),
            pc.spacer(padding="1%"),
            pc.divider(),
            pc.vstack(
                pc.hstack(
                    pc.heading("ClearFly", id="clearfly"),
                    pc.image(src="/projs/clearfly/logo.png", width="48px"),
                ),
                pc.text(
                    """
    ClearFly is a group that is making a high-quality Boeing 737-100 for the X-Plane flight simulator. 
    They are maintaining a Virtual Airline too, called the ClearFly VA. 
    Their current fleet consists of B737-800s, B737-200s and A300-600s, all equiped with beautiful liveries.

    My role at ClearFly is programming systems, doing some Plane Maker stuff and developing the Discord bot of the ClearFly Discord server, ClearBot.
                """,
                    width=["90%", "65%", "65%", "65%"],
                    font_size="120%",
                ),
                pc.tablet_and_desktop(
                    pc.responsive_grid(
                        pc.image(
                            src="/projs/clearfly/clearbot_1.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            width="auto",
                            position="relative",
                            top="26%",
                            left="14%",
                        ),
                        pc.image(
                            src="/projs/clearfly/b731_1.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            width="auto",
                            position="relative",
                            top="1%",
                        ),
                        pc.image(
                            src="/projs/clearfly/b731_2.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            width="auto",
                            position="relative",
                            top="20%",
                            right="30%",
                        ),
                        pc.image(
                            src="/projs/clearfly/cfva_1.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            width="auto",
                            position="relative",
                            bottom="50%",
                            left="30%",
                        ),
                        pc.image(
                            src="/projs/clearfly/b731_3.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            width="100%",
                            position="relative",
                            bottom="10%",
                        ),
                        columns=[3],
                        spacing="4",
                        padding_left="10%",
                        padding_right="10%",
                        padding_top="3%",
                    ),
                    pc.center(
                        pc.hstack(
                            pc.link(
                                pc.tooltip(
                                    pc.button(
                                        pc.image(
                                            src="/icons/github-mark-white.png",
                                            height="1.5em",
                                        ),
                                        _hover={"opacity": 0.85},
                                    ),
                                    label="ClearFly GitHub Profile",
                                    has_arrow=True,
                                ),
                                href="https://github.com/ClearFly-Official",
                                is_external=True,
                            ),
                            pc.link(
                                pc.tooltip(
                                    pc.button(
                                        pc.image(
                                            src="/icons/discord-mark-white.png",
                                            height="1.5em",
                                        ),
                                        _hover={"opacity": 0.85},
                                    ),
                                    label="ClearFly Discord server",
                                    has_arrow=True,
                                ),
                                href="https://discord.gg/mBSVAV2np9",
                                is_external=True,
                            ),
                            pc.link(
                                pc.tooltip(
                                    pc.button(
                                        "x-plane.org ",
                                        pc.icon(tag="external_link", height="1.5em"),
                                        _hover={"opacity": 0.85},
                                    ),
                                    label="ClearFly on the .org forums",
                                    has_arrow=True,
                                ),
                                href="https://forums.x-plane.org/index.php?/forums/topic/265735-clearfly-boeing-737-100/&",
                                is_external=True,
                            ),
                        ),
                    ),
                    height="800px",
                ),
                pc.mobile_only(
                    pc.responsive_grid(
                        pc.image(
                            src="/projs/clearfly/b731_1.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            position="relative",
                            top="1%",
                        ),
                        pc.image(
                            src="/projs/clearfly/cfva_1.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            width="auto",
                            position="relative",
                            bottom="50%",
                            left="10%",
                        ),
                        pc.image(
                            src="/projs/clearfly/b731_3.png",
                            box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                            _hover={"filter": "brightness(105%)", "z_index": "97"},
                            border_radius="4em",
                            width="100%",
                            position="relative",
                            bottom="80%",
                            right="9%",
                        ),
                        columns=[0],
                        spacing="4",
                        padding_left="10%",
                        padding_right="10%",
                        padding_top="3%",
                        width="100%",
                    ),
                    pc.center(
                        pc.hstack(
                            pc.link(
                                pc.tooltip(
                                    pc.button(
                                        pc.image(
                                            src="/icons/github-mark-white.png",
                                            height="1.5em",
                                        ),
                                        _hover={"opacity": 0.85},
                                    ),
                                    label="ClearFly GitHub Profile",
                                    has_arrow=True,
                                ),
                                href="https://github.com/ClearFly-Official",
                                is_external=True,
                            ),
                            pc.link(
                                pc.tooltip(
                                    pc.button(
                                        pc.image(
                                            src="/icons/discord-mark-white.png",
                                            height="1.5em",
                                        ),
                                        _hover={"opacity": 0.85},
                                    ),
                                    label="ClearFly Discord server",
                                    has_arrow=True,
                                ),
                                href="https://discord.gg/mBSVAV2np9",
                                is_external=True,
                            ),
                            pc.link(
                                pc.tooltip(
                                    pc.button(
                                        "x-plane.org ",
                                        pc.icon(tag="external_link", height="1.5em"),
                                        _hover={"opacity": 0.85},
                                    ),
                                    label="ClearFly on the .org forums",
                                    has_arrow=True,
                                ),
                                href="https://forums.x-plane.org/index.php?/forums/topic/265735-clearfly-boeing-737-100/&",
                                is_external=True,
                            ),
                        ),
                        position="relative",
                        bottom="70px",
                    ),
                ),
            ),
        ),
        pc.vstack(
            pc.hstack(
                pc.heading("WingFlex Studios", id="wingflex"),
                pc.image(src="/projs/wingflex/logo.png", width="52px", border_radius="15px"),
            ),
            pc.text(
                """
WingFlex Studios is making the Boeing 787-9 and -8 for the X-Plane flight simulator and the Microsoft Flight Simulator. My role there is coding (SASL) and Plane Maker.
                """,
                width=["90%", "65%", "65%", "65%"],
                font_size="120%",
            ),
            pc.tablet_and_desktop(
                pc.responsive_grid(
                    pc.image(
                        src="/projs/wingflex/b787_1.png",
                        box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                        _hover={"filter": "brightness(105%)", "z_index": "97"},
                        border_radius="4em",
                        width="auto",
                        position="relative",
                        top="0%",
                        left="42%",
                    ),
                    pc.image(
                        src="/projs/wingflex/b787_3.png",
                        box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                        _hover={"filter": "brightness(105%)", "z_index": "97"},
                        border_radius="4em",
                        width="auto",
                        position="relative",
                        top="15%",
                        left="50%",
                    ),
                    pc.image(
                        src="/projs/wingflex/b787_2.png",
                        box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                        _hover={"filter": "brightness(105%)", "z_index": "97"},
                        border_radius="4em",
                        width="auto",
                        position="relative",
                        top="26%",
                        left="-100%",
                    ),
                    columns=[3],
                    spacing="4",
                    padding_left="10%",
                    padding_right="10%",
                    padding_top="0%",
                ),
                pc.center(
                    pc.hstack(
                        pc.link(
                            pc.tooltip(
                                pc.button(
                                    pc.image(
                                        src="/icons/github-mark-white.png",
                                        height="1.5em",
                                    ),
                                    _hover={"opacity": 0.85},
                                ),
                                label="WingFlex Studios GitHub Repo",
                                has_arrow=True,
                            ),
                            href="https://github.com/Brusselsaviation/Wingflex-B787-9-B787-8/",
                            is_external=True,
                        ),
                        pc.link(
                            pc.tooltip(
                                pc.button(
                                    pc.image(
                                        src="/icons/discord-mark-white.png",
                                        height="1.5em",
                                    ),
                                    _hover={"opacity": 0.85},
                                ),
                                label="WingFlex Studios Discord server",
                                has_arrow=True,
                            ),
                            href="https://discord.gg/wdnkbACAb2",
                            is_external=True,
                        ),
                    ),
                    padding_top="5%"
                ),
                height="900px",
            ),
            pc.mobile_only(
                pc.responsive_grid(
                    pc.image(
                        src="/projs/wingflex/b787_1.png",
                        box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                        _hover={"filter": "brightness(105%)", "z_index": "97"},
                        border_radius="4em",
                        width="auto",
                        position="relative",
                        top="0%",
                        left="0%",
                    ),
                    pc.image(
                        src="/projs/wingflex/b787_3.png",
                        box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                        _hover={"filter": "brightness(105%)", "z_index": "97"},
                        border_radius="4em",
                        width="auto",
                        position="relative",
                        top="-17%",
                        left="10%",
                    ),
                    pc.image(
                        src="/projs/wingflex/b787_2.png",
                        box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                        _hover={"filter": "brightness(105%)", "z_index": "97"},
                        border_radius="4em",
                        width="auto",
                        position="relative",
                        top="-30%",
                        left="-9%",
                    ),
                    columns=[0],
                    spacing="4",
                    padding_left="10%",
                    padding_right="10%",
                    padding_top="0%",
                ),
pc.center(
                    pc.hstack(
                        pc.link(
                            pc.tooltip(
                                pc.button(
                                    pc.image(
                                        src="/icons/github-mark-white.png",
                                        height="1.5em",
                                    ),
                                    _hover={"opacity": 0.85},
                                ),
                                label="WingFlex Studios GitHub Repo",
                                has_arrow=True,
                            ),
                            href="https://github.com/Brusselsaviation/Wingflex-B787-9-B787-8/",
                            is_external=True,
                        ),
                        pc.link(
                            pc.tooltip(
                                pc.button(
                                    pc.image(
                                        src="/icons/discord-mark-white.png",
                                        height="1.5em",
                                    ),
                                    _hover={"opacity": 0.85},
                                ),
                                label="WingFlex Studios Discord server",
                                has_arrow=True,
                            ),
                            href="https://discord.gg/wdnkbACAb2",
                            is_external=True,
                        ),
                    ),
                ),
            ),
        ),
        pc.spacer(padding="4%"),
        footBar("/projs"),
    )
