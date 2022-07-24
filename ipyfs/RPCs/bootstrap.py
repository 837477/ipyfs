from ipyfs.ipfs import IPFS


class BootStrap(IPFS):

    def __init__(self):
        super(BootStrap, self).__init__()
        self.add = self.Add()
        self.rm = self.Rm()

    def __call__(self) -> dict:
        """
        Show or edit the list of bootstrap peers.

        :return response: Response from IPFS.
        """
        return self._send(locals())

    class Add(IPFS):

        def __init__(self):
            super(BootStrap.Add, self).__init__()

        def __call__(
            self,
            peer: str = None,
            default: bool = None
        ) -> dict:
            """
            Add peers to the bootstrap list.

            :param peer: A peer to add to the bootstrap list (in the format '<multiaddr>/<peerID>') Required: no.
            :param default: Add default bootstrap nodes. (Deprecated, use 'default' subcommand instead). Required: no.
            :return response: Response from IPFS.
            """
            replace = {"peer": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

        def default(self) -> dict:
            """
            Add default bootstrap nodes.

            :return response: Response from IPFS.
            """
            return self._send(locals())

    class Rm(IPFS):

        def __init__(self):
            super(BootStrap.Rm, self).__init__()

        def __call__(
            self,
            peer: str = None
        ) -> dict:
            """
            Remove a peer from the bootstrap list.

            :param peer: A peer to add to the bootstrap list (in the format '<multiaddr>/<peerID>') Required: no.
            :return response: Response from IPFS.
            """
            replace = {"peer": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

        def all(self) -> dict:
            """
            Remove all peers from the bootstrap list.

            :return response: Response from IPFS.
            """
            return self._send(locals())

    def list(self) -> dict:
        """
        Show peers in the bootstrap list.

        :return response: Response from IPFS.
        """
        return self._send(locals())
