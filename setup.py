from setuptools import setup

dependencies = [
    "blspy==1.0.6",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.14",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the venidium processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
    "watchdog==2.1.3",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="venidium-blockchain",
    author="Venidium",
    author_email="contact@venidium.io",
    description="Venidium blockchain full node, farmer, timelord, and wallet.",
    url="https://venidium.io/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="venidium blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "venidium",
        "venidium.cmds",
        "venidium.clvm",
        "venidium.consensus",
        "venidium.daemon",
        "venidium.full_node",
        "venidium.timelord",
        "venidium.farmer",
        "venidium.harvester",
        "venidium.introducer",
        "venidium.plotting",
        "venidium.pools",
        "venidium.protocols",
        "venidium.rpc",
        "venidium.server",
        "venidium.simulator",
        "venidium.types.blockchain_format",
        "venidium.types",
        "venidium.util",
        "venidium.wallet",
        "venidium.wallet.puzzles",
        "venidium.wallet.rl_wallet",
        "venidium.wallet.cc_wallet",
        "venidium.wallet.did_wallet",
        "venidium.wallet.settings",
        "venidium.wallet.trading",
        "venidium.wallet.util",
        "venidium.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "venidium = venidium.cmds.venidium:main",
            "venidium_wallet = venidium.server.start_wallet:main",
            "venidium_full_node = venidium.server.start_full_node:main",
            "venidium_harvester = venidium.server.start_harvester:main",
            "venidium_farmer = venidium.server.start_farmer:main",
            "venidium_introducer = venidium.server.start_introducer:main",
            "venidium_timelord = venidium.server.start_timelord:main",
            "venidium_timelord_launcher = venidium.timelord.timelord_launcher:main",
            "venidium_full_node_simulator = venidium.simulator.start_simulator:main",
        ]
    },
    package_data={
        "venidium": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "venidium.util": ["initial-*.yaml", "english.txt"],
        "venidium.ssl": ["venidium_ca.crt", "venidium_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
