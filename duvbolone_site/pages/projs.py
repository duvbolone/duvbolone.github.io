import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar

route = "/projs"
title = "Matt3o0's Website: projects"
image = "/M27.png"
description = "My projects"


def page():
    return pc.box(
        navBar("/"),
        pc.text("", id="topOfPage", padding="50px"),
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
            pc.html("""
<pre>




</pre>
"""),
            pc.divider(),
            pc.hstack(
                pc.heading("ClearFly", id="clearfly"),
                pc.image(src="/projs/clearfly/logo.png", width="48px")
            ),
            pc.text("""
ClearFly is a group that is making a high-quality Boeing 737-100 for the X-Plane flight simulator. 
They are maintaining a Virtual Airline too, called the ClearFly VA. 
Their current fleet consists of B737-800s, B737-200s and A300-600s, all equiped with beautiful liveries.

My role at ClearFly is programming systems, doing some Plane Maker stuff and developing the Discord bot of the ClearFly Discord server, ClearBot.
            """, width="65%", font_size="120%"),
            pc.tablet_and_desktop(
                pc.image(src="/projs/clearfly/clearbot_1.png",
                         box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                         _hover={
                             "filter": "brightness(105%)", "width": "40.1%"},
                         border_radius="4em",
                         width="40%",
                         position="relative",
                         left="50%",
                         bottom="-530px"
                         ),
                pc.image(src="/projs/clearfly/b731_1.png",
                         box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                         _hover={
                             "filter": "brightness(105%)", "width": "50.1%"},
                         border_radius="4em",
                         width="50%",
                         position="relative",
                         left="41%",
                         bottom="100px"
                         ),
                pc.image(src="/projs/clearfly/b731_2.png",
                         box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                         _hover={
                             "filter": "brightness(105%)", "width": "40.1%"},
                         border_radius="4em",
                         width="40%",
                         position="relative",
                         left="5%",
                         bottom="460px"
                         ),
                pc.image(src="/projs/clearfly/cfva_1.png",
                         box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                         _hover={
                             "filter": "brightness(105%)", "width": "40.1%"},
                         border_radius="4em",
                         width="40%",
                         position="relative",
                         left="10%",
                         bottom="530px"
                         ),
                pc.image(src="/projs/clearfly/b731_3.png",
                         box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                         _hover={
                             "filter": "brightness(105%)", "width": "50.1%"},
                         border_radius="4em",
                         width="50%",
                         position="relative",
                         left="27%",
                         bottom="1150px"
                         ),
                pc.center(
                    pc.hstack(
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.image(
                                    src="/icons/github-mark-white.png", height="1.5em"), _hover={"opacity": 0.85}),
                                label="ClearFly GitHub Profile",
                                has_arrow=True
                            ),
                            href="https://github.com/ClearFly-Official",
                            is_external=True
                        ),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.image(
                                    src="/icons/discord-mark-white.png", height="1.5em"), _hover={"opacity": 0.85}),
                                label="ClearFly Discord server",
                                has_arrow=True
                            ),
                            href="https://discord.gg/mBSVAV2np9",
                            is_external=True
                        ),
                        pc.link(
                            pc.tooltip(
                                pc.button("x-plane.org ", pc.icon(tag="ExternalLinkIcon",
                                                                  height="1.5em"), _hover={"opacity": 0.85}),
                                label="ClearFly on the .org forums",
                                has_arrow=True
                            ),
                            href="https://forums.x-plane.org/index.php?/forums/topic/265735-clearfly-boeing-737-100/&",
                            is_external=True
                        ),
                    ),
                    position="relative",
                    bottom="900px"
                )
            ),
            pc.mobile_only(
                pc.image(src="/projs/clearfly/b731_3.png",
                         box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                         border_radius="1em",
                         width="70%",
                         position="relative",
                         left="15%",
                         bottom="-5px"
                         ),
                pc.image(src="/projs/clearfly/cfva_1.png",
                         box_shadow="rgb(0, 0, 0, 0.2) -8px 8px 10px",
                         border_radius="1em",
                         width="70%",
                         position="relative",
                         left="15%",
                         bottom="-15px"
                         ),
                pc.center(
                    pc.hstack(
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.image(
                                    src="/icons/github-mark-white.png", height="1.5em"), _hover={"opacity": 0.85}),
                                label="ClearFly GitHub Profile",
                                has_arrow=True
                            ),
                            href="https://github.com/ClearFly-Official",
                            is_external=True
                        ),
                        pc.link(
                            pc.tooltip(
                                pc.button(pc.image(
                                    src="/icons/discord-mark-white.png", height="1.5em"), _hover={"opacity": 0.85}),
                                label="ClearFly Discord server",
                                has_arrow=True
                            ),
                            href="https://discord.gg/mBSVAV2np9",
                            is_external=True
                        ),
                        pc.link(
                            pc.tooltip(
                                pc.button("x-plane.org ", pc.icon(tag="ExternalLinkIcon",
                                                                  height="1.5em"), _hover={"opacity": 0.85}),
                                label="ClearFly on the .org forums",
                                has_arrow=True
                            ),
                            href="https://forums.x-plane.org/index.php?/forums/topic/265735-clearfly-boeing-737-100/&",
                            is_external=True
                        ),
                    ),
                    position="relative",
                    bottom="-25px"
                )
            ),
            pc.mobile_only(
                pc.html("""
    <pre>






    </pre>
    """),
            ),
            pc.divider(),
        ),
        footBar("/projs")
    )
