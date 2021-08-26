from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "venidium_harvester venidium_timelord_launcher venidium_timelord venidium_farmer venidium_full_node venidium_wallet".split(),
    "node": "venidium_full_node".split(),
    "harvester": "venidium_harvester".split(),
    "farmer": "venidium_harvester venidium_farmer venidium_full_node venidium_wallet".split(),
    "farmer-no-wallet": "venidium_harvester venidium_farmer venidium_full_node".split(),
    "farmer-only": "venidium_farmer".split(),
    "timelord": "venidium_timelord_launcher venidium_timelord venidium_full_node".split(),
    "timelord-only": "venidium_timelord".split(),
    "timelord-launcher-only": "venidium_timelord_launcher".split(),
    "wallet": "venidium_wallet venidium_full_node".split(),
    "wallet-only": "venidium_wallet".split(),
    "introducer": "venidium_introducer".split(),
    "simulator": "venidium_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
