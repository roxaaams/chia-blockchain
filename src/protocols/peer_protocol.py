from src.util.ints import uint64
from typing import List
from src.util.cbor_message import cbor_message
from src.types.sized_bytes import bytes32
from src.types.transaction import Transaction
from src.types.proof_of_time import ProofOfTime
from src.types.trunk_block import TrunkBlock
from src.types.full_block import FullBlock
from src.types.peer_info import PeerInfo
from dataclasses import dataclass

"""
Protocol between full nodes.
"""


@dataclass(frozen=True)
@cbor_message
class TransactionId:
    """
    Receive a transaction id from a peer.
    """
    transaction_id: bytes32


@dataclass(frozen=True)
@cbor_message
class RequestTransaction:
    """
    Request a transaction from a peer.
    """
    transaction_id: bytes32


@dataclass(frozen=True)
@cbor_message
class NewTransaction:
    """
    Receive a transaction from a peer.
    """
    transaction: Transaction


@dataclass(frozen=True)
@cbor_message
class NewProofOfTime:
    """
    Receive a new proof of time from a peer.
    """
    proof: ProofOfTime


@dataclass(frozen=True)
@cbor_message
class UnfinishedBlock:
    """
    Receive an unfinished block from a peer.
    """
    # Block that does not have ProofOfTime and Challenge
    block: FullBlock


@dataclass(frozen=True)
@cbor_message
class RequestBlock:
    """
    Requests a block from a peer.
    """
    header_hash: bytes32


@dataclass(frozen=True)
@cbor_message
class Block:
    """
    Receive a block from a peer.
    """
    block: FullBlock


@dataclass(frozen=True)
@cbor_message
class RequestPeers:
    """
    Return full list of peers
    """
    pass


@dataclass(frozen=True)
@cbor_message
class Peers:
    """
    Update list of peers
    """
    peer_list: List[PeerInfo]


@dataclass(frozen=True)
@cbor_message
class RequestTrunkBlocks:
    """
    Request trunks of blocks that are ancestors of the specified tip.
    """
    tip_header_hash: bytes32
    heights: List[uint64]


@dataclass(frozen=True)
@cbor_message
class TrunkBlocks:
    """
    Sends trunk blocks that are ancestors of the specified tip, at the specified heights.
    """
    tip_header_hash: bytes32
    trunk_blocks: List[TrunkBlock]


@dataclass(frozen=True)
@cbor_message
class RequestSyncBlocks:
    """
    Request download of blocks, in the blockchain that has 'tip_header_hash' as the tip
    """
    tip_header_hash: bytes32
    heights: List[uint64]


@dataclass(frozen=True)
@cbor_message
class SyncBlocks:
    """
    Send blocks to peer.
    """
    tip_header_hash: bytes32
    blocks: List[FullBlock]