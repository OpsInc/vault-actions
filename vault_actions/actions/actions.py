#!/usr/bin/env python3

"""Module containing the core functions to recursively execute an action"""

from dataclasses import dataclass
from typing import Any

from vault_actions.utils.vault import (
    destroy_secret,
    fetch_secret_data,
    list_keys,
    write_secret_to_dest,
)


@dataclass
class Actions:
    args: Any

    def recursive_fetch(self, project: str, vault_dest_path: str):
        """
        Recursively fetches and copies secrets from the source path to the destination path.
        """
        if not project.endswith("/"):
            if not self.args.dryrun:
                secret_data = fetch_secret_data(project)
                write_secret_to_dest(secret_data, vault_dest_path)
            print(f"\nSecret from: {project}\nCopied to  : {vault_dest_path}")
        else:
            secrets = list_keys(project)

            for secret in secrets:
                if secret.endswith("/"):  # If folder, then continue recursion
                    self.recursive_fetch(project + secret, vault_dest_path)
                else:  # if secret, fetch secret data
                    secret_current_path = project + secret
                    secret_suffix = secret_current_path.replace(self.args.source, "")
                    secret_dest_path = vault_dest_path.rstrip("/") + "/" + secret_suffix
                    if not self.args.dryrun:
                        secret_data = fetch_secret_data(secret_current_path)
                        write_secret_to_dest(secret_data, secret_dest_path)

                    print(
                        f"\nSecret from: {secret_current_path}\nCopied to  :"
                        f" {secret_dest_path}"
                    )

    def recursive_delete(self, project: str, vault_dest_path: str):
        """
        Recursively deletes all secrets under the source path.
        """
        secrets = list_keys(project)

        for secret in secrets:
            if secret.endswith("/"):  # If folder, then continue recursion
                self.recursive_delete(project + secret, vault_dest_path)
            else:  # if secret, delete it
                secret_current_path = project + secret
                if not self.args.dryrun:
                    destroy_secret(secret_current_path)

                print(f"\nSecret path to DELETE: {secret_current_path}")
