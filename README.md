# cybergisx-cli

The repo for the `cybergisx` and `cjw` command line interface.

The [original version was written in Bash](bash). We are currently rewriting to use [Python with the click API](python) to introduce more functionality and easier testing.


Bash functionality (deployed):

```
  This is cybergisx (version 2021-09), designed to help manage compute
  environments here on CyberGISX. Your options are:
    --help [-h]:             to display this help message.
    --version [-v]:          to see version information.
    --avail [-a]:            to see available CyberGISX kernels.
    --install [-i] <kernel>: to install an available kernel.
    --personal [-p]:         to see personal kernels.
    --remove-personal [-rp]: to remove a personal kernel.
```

Current Python functionality:

```
Usage: cybergisx.py [OPTIONS] COMMAND [ARGS]...

Options:
  -a, --avail                  to see available CyberGISX kernels.
  -i, --install PATH           to install an available kernel.
  -p, --personal               to see your personal kernels.
  -rp, --remove-personal PATH  to remove a personal kernel.
  --version                    Show the version and exit.
  --help                       Show this message and exit.
```


## TODO:

* ~~Replicate functionality in click.~~ The functions with suffix `_dir` do this
* ~~Handle personal kernels without duplicating config. Transition to JSON/YAML?~~ Transitioned to JSON (functions with `_json` suffix)
* ~~Write function to transition configs to JSON/YAML~~ See `transition_pk_dir2json`
* ~~Write function to install personal kernels to in_container_kernel_path~~ Added as hidden `-s`/`--startup` option
* ~~Add `-h` option for help~~ Added to `@click.version_option` as param_decls. [See docs](https://click.palletsprojects.com/en/8.0.x/api/#click.version_option)
* ~~Move dir->json transition to startup~~ Done
* Automated testing: https://click.palletsprojects.com/en/8.0.x/testing/


## TODO for Startup Scripts

* Add $CIGI_PERSONAL_CONFIG to `set_environment.sh`
* Call with `-s` in `pre-start-notebook.sh`