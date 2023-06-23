#!/usr/bin/env python3

"""Helper module containing all the basic vault actions"""

import os

import hvac

client = hvac.Client(
    url=os.environ["VAULT_ADDR"],
    token=os.environ["VAULT_TOKEN"],
)


def list_keys(root_path: str) -> list:
    """List the secrets keys. They can either be a secret path or secret"""
    list_response = client.secrets.kv.v2.list_secrets(path=root_path)

    return list_response["data"]["keys"]


def fetch_secret_data(path: str) -> dict:
    """Fetch the key/value data of a secret"""
    secret_response = client.secrets.kv.v2.read_secret_version(
        path=path,
    )

    return secret_response["data"]["data"]


def write_secret_to_dest(secret_data: dict, dest_dir: str):
    """Copies the secret to a new desired destination path"""
    client.secrets.kv.v2.create_or_update_secret(
        path=dest_dir,
        secret=secret_data,
    )


def destroy_secret(path: str):
    """Deletes a secret"""
    client.secrets.kv.v2.delete_metadata_and_all_versions(
        path=path,
    )
