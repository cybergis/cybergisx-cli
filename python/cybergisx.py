import click
import os
import shutil

TOOLNAME = "cybergisx"
PLATFORM = "CyberGISX"
__version__ = "0.9.0-dev"

CIGI_EB_KERNEL_DIR = os.getenv("CIGI_EB_KERNEL_DIR")
IN_CONTAINER_KERNEL_PATH = os.getenv("IN_CONTAINER_KERNEL_PATH")
IN_CONTAINER_PERSONAL_KERNELS = os.getenv("IN_CONTAINER_PERSONAL_KERNELS")


def copy_dir(source, target):
    shutil.copytree(source, target)


def delete_path(path):
    if click.confirm("This action will delete {}, would you like to continue?".format(path)):
        shutil.rmtree(path)


def get_available_kernels():
    return [f for f in os.listdir(CIGI_EB_KERNEL_DIR)]


def get_personal_kernels():
    return [f for f in os.listdir(IN_CONTAINER_PERSONAL_KERNELS)]


def print_avail_kernels():
    kernels = get_available_kernels()
    print("Available kernels:")
    for kernel in kernels:
        print("  * {}".format(kernel))


def print_personal_kernels():
    personal_kernels = get_personal_kernels()
    if len(personal_kernels) > 0:
        print("Your personal kernels are:")
        for kernel in personal_kernels:
            print("  * {}".format(kernel))
    else:
        print("No personal kernels found at {}".format(IN_CONTAINER_PERSONAL_KERNELS))


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.option("-a", "--avail", is_flag=True, help="to see available {} kernels.".format(PLATFORM))
@click.option("-i", "--install", type=click.Path(), help="to install an available kernel.")
@click.option("-p", "--personal", is_flag=True, help="to see your personal kernels.")
@click.option("-rp", "--remove-personal", type=click.Path(), help="to remove a personal kernel.")
@click.version_option(__version__)
def cli(avail, install, personal, remove_personal):
    if avail:
        print_avail_kernels()
    elif install:
        kernels = get_available_kernels()
        if install in kernels:
            print("Installing {}...".format(install))
            to_install_dir = os.path.join(CIGI_EB_KERNEL_DIR, install)
            copy_dir(to_install_dir, os.path.join(IN_CONTAINER_PERSONAL_KERNELS, install))
            copy_dir(to_install_dir, os.path.join(IN_CONTAINER_KERNEL_PATH, install))
        else:
            print("{} not in available kernels.".format(install))
            print_avail_kernels()
    elif personal:
        print_personal_kernels()
    elif remove_personal:
        personal_kernels = get_personal_kernels()
        if remove_personal in personal_kernels:
            to_delete = os.path.join(IN_CONTAINER_PERSONAL_KERNELS, remove_personal)
            delete_path(to_delete)
        else:
            print("{} not found in personal kernels".format(remove_personal))
            print_personal_kernels()


if __name__ == "__main__":
    cli()
