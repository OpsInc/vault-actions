[![CI Pipeline](https://github.com/jad617/vault-actions/actions/workflows/ci.yaml/badge.svg)](https://github.com/jad617/vault-actions/actions/workflows/ci.yaml)

# vault-actions - command line for running actions on Vault

```shell
❯ vault-actions.py --help
usage: vault-actions.py [-h] --source SOURCE [--dest DEST] [--delete | --no-delete] [--dryrun | --no-dryrun]

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       Vault full source path
  --dest DEST           Vault full destination path, copy everything under path specified by --source
  --delete, --no-delete
                        Delete everything under path specified by --source (default: False)
  --dryrun, --no-dryrun
                        Allows you to preview without applying the changes (default: False)

```

## Requirements

### Python dependencies

```shell
pip install hvac

or 

pip install -r requirements.txt
```

## Usage

## Copy

To copy all secrets under a path you need to call the "--source" and "--dest" options

```shell
# Secret structure:
a/
└── b/
   ├── c/
   │  ├── d/
   │  │  ├── secret_d_1
   │  │  └── secret_d_2
   │  └── secret_c_1
   ├── secret_b_1
   └── secret_b_2

-------------------------------------------------

❯ ./vault-actions/vault-actions.py --source a/b/ --dest x/z/ --dryrun

***Dry Run Started***

Secret from:        a/b/c/d/secret_d_1
has been copied to: x/b/c/d/secret_d_1

Secret from:        a/b/c/d/secret_d_2
has been copied to: x/b/c/d/secret_d_2

Secret from:        a/b/c/secret_c_1
has been copied to: x/b/c/secret_c_1

Secret from:        a/b/secret_b_1
has been copied to: x/b/secret_b_1

Secret from:        a/b/secret_b_2
has been copied to: x/b/secret_b_2

***Dry Run Ended***
```

## Delete

To delete all secrets under a path you need to call the "--source" and "--delete" options

```shell
# Secret structure:
a/
└── b/
   ├── c/
   │  ├── d/
   │  │  ├── secret_d_1
   │  │  └── secret_d_2
   │  └── secret_c_1
   ├── secret_b_1
   └── secret_b_2

-------------------------------------------------

❯ ./vault-actions/vault-actions.py --source a/ --delete  --dryrun
***Dry Run Started***

Secret path to DELETE:        a/b/c/d/secretd1

Secret path to DELETE:        a/b/c/d/secretd2

Secret path to DELETE:        a/b/c/secredc1

Secret path to DELETE:        a/b/secret_b_1

Secret path to DELETE:        a/b/secretb1

Secret path to DELETE:        a/b/secretb2

***Dry Run Ended***

```
