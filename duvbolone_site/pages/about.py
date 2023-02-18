import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar
from duvbolone_site.comps.state import State

route = "/about"
title = "Matt3o0's Website: about"
image = "/M27.png"
description = "My about me page, it tells you a bit about me I suppose."

def page():
    return pc.box(
        navBar("/"),
        pc.tablet_and_desktop(
            pc.vstack(
                pc.heading(
                    "About me",
                    font_size = "300%",
                    padding = "30px",
                    ),
                pc.span("Hello there! I'm Matt3o0 and here I will tell you a little bit about myself.", font_size = "130%", font_weight="bold"),
                pc.vstack(
                    pc.text("""
    I live in Belgium, speak English, Dutch, Italian(I'm half Italian) and a bit of French. 
    When I game it's usually X-Plane, Minecraft, ETS2 or Universe Sandbox. 
    I'm interested in a lot of subjects too, like:
                    """, width = "80vh"),
                    pc.vstack(
                        pc.unordered_list(items = ["🛩️ Aviation", "🔭 Astronomy/Rocketry", "📸 (Astro)photography", "🗣️ Languages", "💻 Everything computers"]),
                        pc.unordered_list(items = ["⌨️ Coding"]),
                        pc.unordered_list(items = ["🐍 Python", "☕️ Java", "🚀 C++"], padding_left = "9vh"),
                        padding_right = "50vh",
                        font_weight = "bold"
                    ),
                    font_size = "110%",
                ),
                pc.heading("Quick Information"),
                pc.hstack(
                    pc.text("Current time for me:"),
                    pc.html("""
    <iframe src="https://free.timeanddate.com/clock/i8q5meqb/n48/fcfff/tct/pct/ts1/ta1" frameborder="0" width="84" height="18" allowtransparency="true"></iframe>
                    """),
                    padding_right = "52vh"
                ),
                pc.text("My birthday: 20th of May",padding_right = "59vh"),
                pc.heading("Website Information"),
                pc.markdown("""
- Built with: [**Pynecone**](https://pynecone.io)
- Hosted on: [**GitHub Pages**](https://pages.github.com)
- Domain by: [**is-a.dev**](https://is-a.dev)
                """)
            ),
        ),
        pc.mobile_only(
            pc.vstack(
                pc.heading(
                    "About me",
                    font_size = "300%",
                    padding = "30px",
                    ),
                pc.span("Hello there! I'm Matt3o0 and here I will tell you a little bit about myself.", font_size = "130%", font_weight="bold"),
                pc.vstack(
                    pc.text("""
    I live in Belgium, speak English, Dutch, Italian(I'm half Italian) and a bit of French. 
    When I game it's usually X-Plane, Minecraft, ETS2 or Universe Sandbox. 
    I'm interested in a lot of subjects too, like:
                    """),
                    pc.vstack(
                        pc.unordered_list(items = ["🛩️ Aviation", "🔭 Astronomy/Rocketry", "📸 (Astro)photography", "🗣️ Languages", "💻 Everything computers"]),
                        pc.unordered_list(items = ["⌨️ Coding"]),
                        pc.unordered_list(items = ["🐍 Python", "☕️ Java", "🚀 C++"], padding_left = "9vh"),
                        font_weight = "bold"
                    ),
                    font_size = "110%",
                ),
                pc.heading("Quick Information"),
                pc.hstack(
                    pc.text("Current time for me:"),
                    pc.html("""
    <iframe src="https://free.timeanddate.com/clock/i8q5meqb/n48/fcfff/tct/pct/ts1/ta1" frameborder="0" width="84" height="18" allowtransparency="true"></iframe>
                    """),
                    padding_right = "12vh"
                ),
                pc.text("My birthday: 20th of May",padding_right = "19vh"),
                width = "100%",
                padding = "10px"
            ),
        ),
        pc.center(
            pc.hstack(
                pc.link(
                    pc.tooltip(
                                pc.button(pc.image(src="/icons/github-mark-white.png", height = "1.5em"), _hover={"opacity": 0.85}),
                                label = "My GitHub profile",
                                has_arrow = True
                            ),
                            href = "https://github.com/duvbolone"
                ),
                pc.link(
                    pc.tooltip(
                        pc.button(pc.image(src="/icons/discord-mark-white.png", height = "1.5em"), _hover={"opacity": 0.85}),
                        label = "My Discord profile",
                        has_arrow = True
                    ),
                    href = "https://discord.com/users/668874138160594985"
                ),
                pc.link(
                    pc.tooltip(
                        pc.button(pc.image(src="/icons/twitter-mark-white.svg", height = "1.5em"), _hover={"opacity": 0.85}),
                        label = "My Twitter profile",
                        has_arrow = True
                    ),
                    href = "https://twitter.com/Matt3o044"
                ),
            ),
            padding = "15px"
        ),
        footBar("/"),
    )