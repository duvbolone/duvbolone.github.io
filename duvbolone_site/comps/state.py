import pynecone as pc

class State(pc.State):
    def alert(self):
        return pc.window_alert("Hello there!")