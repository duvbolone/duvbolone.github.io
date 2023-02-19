import pynecone as pc

class State(pc.State):
    
    @pc.var
    def get_url(self):
        return self.get_query_params().get("any", "none")