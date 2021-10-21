# Venidium Blockchain

Hello and welcome to Venidium Blockchain.

We are happy to announce the launch of our mainnet today.

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

Shortly after this release, the windows installer should be available for download.  
Please check the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page.

ℹ️ _Before you start, you are advised to __not launch the installer directly__. We have prepared an executable that you need to run to make sure previous installations don't interfere. Please run `cleanup-testnet-environment` (exe) that you can find at the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page before installing venidium_

Please follow the steps in order to cleanly install venidium:

1. Download the latest `cleanup-testnet-environment` (exe) file from the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page.
1. Double click on `cleanup-testnet-environment` file (exe).
1. Select the `Cleanup the whole venidium directory (highly recommended)` option by pressing `1` and then enter.
1. Select the `Cleanup VENIDIUM_ROOT environment variable (highly recommended)` options by pressing `1` and then enter.
1. Download the latest `VenidiumSetup` (exe) file from the [releases](https://github.com/Venidium-Network/venidium-blockchain/releases) page.
1. Double-click on `VenidiumSetup` (exe) and wait for the installation to finish.
1. Venidiub Blockchain should now start. You can recover/generate your keys, add your plot directories.

For people that want to join the testnet directly on launch, you would need to perform a few extra steps.

1. Visit [https://download.venidium.io/notify/mainnet_alert.txt](https://download.venidium.io/notify/mainnet_alert.txt)
1. If the text you get includes `\"ready\": false` then the mainnet wasn't initiated yet. Keep refreshing until you notice any changes.
1. Once the text includes `\"ready\": true`, you are ready to configure your node. Keep your browser open, you will need the value of the `\"genesis_challenge\"` section later.
1. Open notepad by pressing start, typing `notepad` and clicking on the notepad icon
![Notepad](/images/win1.PNG)
1. In notepad click the file menu and select open
1. In the address bar, paste the following: `%homedrive%%homepath%.venidium\mainnet\config` and press enter
![Notepad - go to the correct directory](/images/win2.png)
1. On the bottom right corner, select `All files`
1. Select the `config` (yaml) file and press open
![Notepad - open the config file](/images/win3.png)
1. Locate the line that contains `GENESIS_CHALLENGE: null`
1. On your browser, copy the value of the `\"genesis_challenge\"` section. (Be careful not to copy any neigbouring characters such as `\"`!)
1. On notepad, replace the `null` value with the `genesis_challenge` value that you copied from your browser.
![Notepad - open the config file](/images/win4.png)
1. On notepad, click `File > Save` and exit
1. Launch Venidium Blockchain. You can restore/generate keys, include plot directories and start farming.

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

sh install.sh

. ./activate

venidium init
```

*There is no easy way to have the GUI working while having the wallet/node running in a WSL2 instance.*  
*We suggest the use of the GUI installer instead.*
