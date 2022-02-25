
## `cjw` Command Line Usage

The `cjw` command line interface is available on [CyberGIS-Jupyter for Water (CJW)](https://go.illinois.edu/cybergis-jupyter-water/). Running `cjw` from the command line should display the following help message:

    Usage: cjw [OPTIONS] COMMAND [ARGS]...

    Options:
    -a, --avail                  See available CJW kernels.
    -i, --install TEXT           Install an available kernel.
    -p, --personal               See your personal kernels.
    -rp, --remove-personal TEXT  Remove a personal kernel.
    -v, --version                Show the version and exit.
    -h, --help                   Show this message and exit.

#### `-a/--avail`

Prints the available kernels to the terminal.

    cjw -a
    cjw --avail

#### `-i/--install TEXT`

Installs an available kernel (see `-a/--avail`). TEXT is kernel to install.

    cjw -i python3
    cjw --install python3

#### `-p/--personal`

Prints the personal kernels you have installed.

    cyberigsx -p
    cyberigsx --personal

#### `-rp/--remove-personal TEXT`

Removes a kernel from your list of personal kernels (see `-p/--personal`). Note that
this does not automatically remove the kernel from the dropdown, but it will no longer
appear after a container restart unless it is a kernel installed by default

    cjw -rp
    cjw --remove-personal

#### `-v/--version`

Prints the version of the cjw command line tool.

    cjw -v
    cjw --version

#### `-h/--help`

Prints the help text for the cjw command line tool.

    cjw -h
    cjw --help

