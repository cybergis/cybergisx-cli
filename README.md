# cybergisx-cli

The repo for the `cybergisx` and `cjw` command line interface.

The [original version was written in Bash](bash). We are currently rewriting to use [Python with the click API](python) to introduce more functionality and easier testing.

Current Python functionality (deployed in 0.9.0):

```
Usage: cybergisx [OPTIONS] COMMAND [ARGS]...

Options:
  -a, --avail                  See available CyberGISX kernels.
  -i, --install TEXT           Install an available kernel.
  -p, --personal               See your personal kernels.
  -rp, --remove-personal TEXT  Remove a personal kernel.
  -v, --version                Show the version and exit.
  -h, --help                   Show this message and exit.
```


## TODO:

* Automated testing: https://click.palletsprojects.com/en/8.0.x/testing/
