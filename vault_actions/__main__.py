#!/usr/bin/env python3

"""
This is the main module of the vault_actions package.
It serves as the entry point for running the application.
"""

import logging


import sys


import hvac

from vault_actions.actions.actions import Actions
from vault_actions.utils.args import argparser


def main():
    """main function"""

    args = argparser().parse_args()

    if not (args.dest or args.delete):
        argparser().error(
            "You must at least use --dest or --delete in combination with --source"
        )

    try:
        # Configure logging
        logging.basicConfig(level=logging.DEBUG if args.dryrun else logging.INFO)
        logger = logging.getLogger(__name__)

        if args.dryrun:
            logger.info("***Dry Run Started***")

        # Vault Client init
        vault_actions = Actions(args)

        if args.delete:
            vault_actions.recursive_delete(args.source, args.dest)
        else:
            vault_actions.recursive_fetch(args.source, args.dest)

        if args.dryrun:
            logger.info("***Dry Run Ended***")
    except KeyError:
        logger.error("Unable to find VAULT_ADDR or VAULT_TOKEN environment variable")
    except hvac.exceptions.InvalidPath:
        logger.error(f"Unable to find the path: secrets/{args.source}")
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
