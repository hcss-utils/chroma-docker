# chroma-docker

This repository provides an example setup for running the Chroma service using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository:
    ```sh
    git clone https://github.com/hcss-utils/chroma-docker.git
    cd chroma-docker
    ```

2. Create a `.env` file with the following content:
    ```env
    CHROMA_SERVER_AUTHN_CREDENTIALS="8585d84727f08b0d"
    CHROMA_SERVER_AUTHN_PROVIDER="chromadb.auth.token_authn.TokenAuthenticationServerProvider"
    ```

3. Ensure the necessary port (8007) is open in your firewall settings.

## Running the Service

Run the following command to start the service:
```sh
docker-compose up -d
```

The Chroma service will be available on port 8007 of your host machine.

## Files

- `docker-compose.yml`: Docker Compose configuration for the Chroma service.
- `.env`: Environment variables for authentication (not included in the repository, you need to create this file).
- `test_connection.py`: Script to test the connection and verify the service endpoints.
