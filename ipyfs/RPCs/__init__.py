"""
IPFS RPC APIs
"""


# IPFS RPC APIs Method
from .add import Add
from .bitswap import BitSwap
from .block import Block
from .bootstrap import BootStrap
from .cat import Cat
from .cid import Cid
from .commands import Commands
from .config import Config
from .dag import Dag
from .dht import DHT
from .diag import Diag
from .files import Files
from .filestore import FileStore
from .get import Get
from .id import Id
from .key import Key
from .log import Log
from .ls import LS
from .multibase import MultiBase
from .name import Name
from .pin import Pin
from .ping import Ping
from .refs import Refs
from .repo import Repo
from .resolve import Resolve
from .shutdown import Shutdown
from .stats import Stats
from .swarm import Swarm
from .update import Update
from .version import Version


__VERSION__ = "0.13.0"