from dataclasses import dataclass
from typing import Optional

from venidium.types.blockchain_format.sized_bytes import bytes32
from venidium.util.ints import uint8, uint64
from venidium.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class SubEpochSummary(Streamable):
    prev_subepoch_summary_hash: bytes32
    reward_chain_hash: bytes32  # hash of reward chain at end of last segment
    num_blocks_overflow: uint8  # How many more blocks than 384*(N-1)
    new_difficulty: Optional[uint64]  # Only once per epoch (diff adjustment)
    new_sub_slot_iters: Optional[uint64]  # Only once per epoch (diff adjustment)
