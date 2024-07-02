import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(
    settings=Settings(
        chroma_client_auth_provider="chromadb.auth.token_authn.TokenAuthClientProvider",
        chroma_client_auth_credentials="8585d84727f08b0d",
    ),
    host="65.109.12.98",
    port="8007",
)
# this should work with or without authentication - it is a public endpoint
client.heartbeat()

# this should work with or without authentication - it is a public endpoint
client.get_version()

# this is a protected endpoint and requires authentication
client.list_collections()
