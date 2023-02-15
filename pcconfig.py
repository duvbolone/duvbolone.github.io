import pynecone as pc

config = pc.Config(
    app_name="duvbolone_site",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
