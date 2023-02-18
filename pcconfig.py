import pynecone as pc

config = pc.Config(
    app_name="duvbolone_site",
    #api_url="http://78.20.254.211:8000",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
