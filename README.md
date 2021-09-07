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