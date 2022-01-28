# cybergisx-cli

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Command Line Usage

Running `cybergisx` from the command line should display the following help message:

    Usage: cybergisx.py [OPTIONS] COMMAND [ARGS]...

    Options:
    -a, --avail                  See available CyberGISX kernels.
    -i, --install TEXT           Install an available kernel.
    -p, --personal               See your personal kernels.
    -rp, --remove-personal TEXT  Remove a personal kernel.
    -v, --version                Show the version and exit.
    -h, --help                   Show this message and exit.

#### `-a/--avail`

Prints the available kernels to the terminal.

    cybergisx -a
    cybergisx --avail

#### `-i/--install TEXT`

Installs an available kernel (see `-a/--avail`). PATH is kernel to install.

    cybergisx -i python3
    cybergisx --install python3

#### `-p/--personal`

Prints the personal kernels you have installed.

    cyberigsx -p
    cyberigsx --personal

#### `-rp/--remove-personal TEXT`

Removes a kernel from your list of personal kernels (see `-p/--personal`). Note that
this does not automatically remove the kernel from the dropdown, but it will no longer
appear after a container restart unless it is a kernel installed by default

    cybergisx -rp
    cybergisx --remove-personal

#### `-v/--version`

Prints the version of the cybergisx command line tool.

    cybergisx -v
    cybergisx --version

#### `-h/--help`

Prints the help text for the cybergisx command line tool.

    cybergisx -h
    cybergisx --help

