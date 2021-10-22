# Venidium Blockchain

Hello and welcome to Venidium Blockchain.

We are happy to announce the launch of our mainnet today.

_For now, we only provide Graphical User Interface instructions for Windows and Command Line Interface instructions for Linux, Mac and WSL._

# Installation instructions for Ubuntu/Debian

Follow below install instructions for Ubuntu 20.04 LTS. If you are installing on Ubuntu 18.04 LTS you should use Python 3.7 instead: `sudo apt-get install python3.7-venv python3.7-distutils python3.7-dev git lsb-release -y`

```shell
sudo apt-get update
sudo apt-get upgrade -y

# Install Git
sudo apt install git -y

# Checkout the source and install
git clone https://github.com/Venidium-Network/venidium-blockchain.git -b latest --recurse-submodules
cd venidium-blockchain

# Clear any remnant env vars
unset VENIDIUM_ROOT

sh install.sh

. ./activate

venidium init

# install gui
sh install-gui.sh

# activate GUI
cd venidium-blockchain-gui
npm run electron &
```

# Installation instructions for macOS

For macOS, make sure [brew](https://brew.sh/) is available before starting the setup and that python 3.7 or newer is installed.

```shell
# Checkout the source and install
git clone https://github.com/Venidium-Network/venidium-blockchain.git -b latest --recurse-submodules
cd venidium-blockchain

# Clear any remnant env vars
unset VENIDIUM_ROOT

sh install.sh

. ./activate

venidium init

# install gui
sh install-gui.sh

# activate GUI
cd venidium-blockchain-gui
npm run electron &
```

# Windows

## GUI

ℹ️ _Before you start, you are advised to __not launch the installer directly__. We have prepared a tool that you need to run to make sure previous installations don't interfere. Please run `cleanup-testnet-environment` (exe) that you can find at the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page before installing venidium_

Please follow the steps in order to cleanly install venidium:

1. Download the latest `cleanup-testnet-environment` (exe) file from the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page.
1. Double click on `cleanup-testnet-environment` file (exe).
1. Select the `Cleanup the whole venidium directory (highly recommended)` option by pressing `1` and then enter.
1. Select the `Cleanup VENIDIUM_ROOT environment variable (highly recommended)` options by pressing `1` and then enter.
1. Download the latest `VenidiumSetup` (exe) file from the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page.
1. Double-click on `VenidiumSetup` (exe) and wait for the installation to finish.
1. Venidium Blockchain should now start. You can recover/generate your keys, add your plot directories.

## WSL2

*We suggest the use of the Windows GUI installer instead of running venidium over WSL2*

If you feel comfortable with using the command line, you can install Venidium (CLI) on a WSL2 instance.

Install Ubuntu 20.04 LTS from the Microsoft Store and run it and complete its initial install steps. You now have a linux bash shell environment that can run linux native software on Windows.

Then follow the steps below which are the same as the usual Ubuntu instructions above with a target of Python 3.8.

```shell
sudo apt-get update
sudo apt-get upgrade -y

# Install Git
sudo apt install git -y

# Checkout the source and install
git clone https://github.com/Venidium-Network/venidium-blockchain.git -b latest --recurse-submodules
cd venidium-blockchain

# Clear any remnant env vars
unset VENIDIUM_ROOT

sh install.sh

. ./activate

venidium init
```

*There is no easy way to have the GUI working while having the wallet/node running in a WSL2 instance.*  
*We suggest the use of the GUI installer instead.*
