from typing import Dict

# The rest of the codebase uses rays everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "venidium": 10 ** 12,  # 1 venidium (XCH) is 1,000,000,000,000 ray (1 trillion)
    "ray": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin rays
}
