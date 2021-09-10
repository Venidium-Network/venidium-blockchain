# Venidium Blockchain

Hello and welcome to Venidium Blockchain.

We are happy to announce the launch of our testnet today.

If you would like to join this test phase and contribute to our network please follow the instruction below.

_For now, we only provide instructions for the command line interface client._  
_Binary clients for **command line interface** but also for **graphical user interface** are currently under development but would be ready before the mainnet launch._  
_This includes binaries for, but not limited to: Ubuntu/Debian, Macos (x64 and ARM64), Windows (x64)_

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

# set $VENIDIUM_ROOT var
export VENIDIUM_ROOT="~/.venidium/kition"

sh install.sh

. ./activate

venidium init

venidium configure -t true

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

# set $VENIDIUM_ROOT var
export VENIDIUM_ROOT="~/.venidium/kition"

sh install.sh

. ./activate

venidium init

venidium configure -t true

# install gui
sh install-gui.sh

# activate GUI
cd venidium-blockchain-gui
npm run electron &

```

# Windows

## GUI

Shortly after this release, the windows installer should be available for download.  
Please check the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page.

Please follow the steps in order to join kition testnet:

1. Download the latest windows installer from the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page.
1. Download [set-environment-for-kition.bat](https://github.com/Venidium-Network/venidium-blockchain/raw/latest/helper-scripts/set-environment-for-kition.bat)
1. Run the installer by double-clicking on the file
1. Run set-environment-for-kition.bat by double clicking on the file
1. You can now use the Venidium shortcut to launch the GUI

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

# set $VENIDIUM_ROOT var
export VENIDIUM_ROOT="~/.venidium/kition"

sh install.sh

. ./activate

venidium init

venidium configure -t true

```

*There is no easy way to have the GUI working while having the wallet/node running in a WSL2 instance.*  
*We suggest the use of the GUI installer instead.*
