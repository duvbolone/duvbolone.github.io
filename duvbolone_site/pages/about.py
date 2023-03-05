import pynecone as pc
from duvbolone_site.comps.navbar import navBar
from duvbolone_site.comps.footbar import footBar
from duvbolone_site.comps.state import State

route = "/about"
title = "About - Matt3o0's Website"
image = "/M27.png"
description = "The website that's supposed to tell you a little bit more about Matt3o0"
meta = [
    {"name":"theme-color", "content":"rgb(22, 22, 22)"}
]
def page():
    return pc.box(
        navBar("/"),
        pc.box(
            pc.vstack(
                pc.spacer(id="topOfPage", padding="2%"),
                pc.heading(
                    "About me",
                    font_size = "300%",
                    padding = "30px",
                    ),
                pc.span("Hello there! I'm Matt3o0 and here I will tell you a little bit about myself.", font_size = "130%", font_weight="bold", width=["95%", "95%", "90%", "auto"]),
                pc.vstack(
                    pc.text("""
I live in Belgium, speak English, Dutch, Italian(I'm half Italian) and a bit of French. 
When I game it's usually X-Plane, Minecraft, ETS2 or Universe Sandbox. 
I'm interested in a lot of subjects too, like:
                    """, width = ["80%","90%", "90%", "35%"]),
                    pc.vstack(
                        pc.unordered_list(items = ["🛩️ Aviation", "🔭 Astronomy", "📸 (Astro)photography", "🗣️ Languages", "💻 Everything computers"]),
                        pc.unordered_list(items = ["⌨️ Coding"]),
                        pc.unordered_list(items = ["🐍 Python", "☕️ Java", "🚀 C++"], padding_left = "25%"),
                        font_weight = "bold",
                        font_size="90%",
                        padding_right=["0%", "0%", "0%", "10%"]
                        #bg="white",
                        #width="100%"
                    ),
                    font_size = "110%",
                    width="100%",
                    #bg="red",
                ),
                pc.heading("Quick Information"),
                pc.hstack(
                    pc.text("Current time for me:"),
                    pc.html("""
    <iframe src="https://free.timeanddate.com/clock/i8q5meqb/n48/fcfff/tct/pct/ts1/ta1" frameborder="0" width="84" height="18" allowtransparency="true"></iframe>
                    """),
                ),
                pc.text("My birthday: 20th of May"),
                pc.heading("Website Information"),
                pc.markdown("""
- Built with: [**Pynecone**](https://pynecone.io)
- Hosted on: [**GitHub Pages**](https://pages.github.com)
- Domain by: [**is-a.dev**](https://is-a.dev)
- Source Code: [**Github**](https://github.com/duvbolone/duvbolone.github.io)
                """),
                pc.spacer(padding="4%")
            ),
        ),
        footBar("/about"),
    )