import pynecone as pc
from duvbolone_site.comps.navbar import navBar

def about():
    return pc.box(
        navBar("/"),
        pc.vstack(
            pc.heading(
                "About me",
                font_weight=700,
                font_size="500%", 
                background_image="linear-gradient(45deg, rgb(200, 0, 0) 20%, rgb(0, 0, 200) 50%)",
                background_clip = "text", 
                padding = "5px"
            ),
            pc.box(
                pc.span("""Hello, I'm Matt3o0.
                         I like everything to do with technology, especially aviation. In terms of programming I mostly use Python(this website is made with Pynecone), Lua and sometimes some other programming languages for fun(Java and C++).
                         """, font_size = "120%"),
                pc.markdown("<br><br>*More to come soon, hopefully...*"),
                width = "20%",
            )
        )
    )