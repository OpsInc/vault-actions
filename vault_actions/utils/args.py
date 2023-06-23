#!/usr/bin/env python3

"""Module for configuring argparse"""

import argparse


def argparser():
    """Defines the args that will be used"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source", type=str, required=True, help="Vault full source path"
    )

    parser.add_argument(
        "--dest",
        type=str,
        required=False,
        help=(
            "Vault full destination path, copy everything under path specified by"
            " --source, if the path does not end with a '/' it will only copy the"
            " secret"
        ),
    )

    parser.add_argument(
        "--delete",
        default=False,
        action=argparse.BooleanOptionalAction,
        help=(
            "Delete everything under path specified by --source, if the path does not"
            " end with a '/' it will only delete the secret"
        ),
    )

    parser.add_argument(
        "--dryrun",
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Allows you to preview without applying the changes",
    )

    return parser
