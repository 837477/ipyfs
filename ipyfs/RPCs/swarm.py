from ipyfs.ipfs import IPFS


class Swarm(IPFS):

    def __init__(self):
        super(Swarm, self).__init__()
        self.addrs = self.Addrs()
        self.filters = self.Filters()
        self.peering = self.Peering()

    def connect(
        self,
        address: str
    ) -> dict:
        """
        Open connection to a given address.

        :param address: Address of peer to connect to. Required: yes.
        :return response: Response from IPFS.
        """
        replace = {"address": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def disconnect(
        self,
        address: str
    ) -> dict:
        """
        Close connection to a given address.

        :param address: Address of peer to disconnect from. Required: yes.
        :return response: Response from IPFS.
        """
        replace = {"address": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def peers(
        self,
        verbose: bool = None,
        streams: bool = None,
        latency: bool = None,
        direction: bool = None
    ) -> dict:
        """
        List peers with open connections.

        :param verbose: display all extra information. Required: no.
        :param streams: Also list information about open streams for each peer. Required: no.
        :param latency: Also list information about latency to each peer. Required: no.
        :param direction: Also list information about the direction of connection. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    class Addrs(IPFS):

        def __init__(self):
            super(Swarm.Addrs, self).__init__()

        def __call__(self) -> dict:
            """
            List known addresses. Useful for debugging.

            :return response: Response from IPFS.
            """
            return self._send(locals())

        def listen(self) -> dict:
            """
            List interface listening addresses.

            :return response: Response from IPFS.
            """
            return self._send(locals())

        def local(
            self,
            id: bool = None
        ) -> dict:
            """
            List local addresses.

            :param id: Show peer ID in addresses. Required: no.
            """
            return self._send(locals())

    class Filters(IPFS):

        def __init__(self):
            super(Swarm.Filters, self).__init__()

        def add(
            self,
            address: str
        ) -> dict:
            """
            Remove an address filter.

            :param address: Multiaddr filter to remove. Required: yes.
            :return response: Response from IPFS.
            """
            replace = {"address": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

        def rm(
            self,
            address: str
        ) -> dict:
            """
            Remove an address filter.

            :param address: Multiaddr filter to remove. Required: yes.
            :return response: Response from IPFS.
            """
            replace = {"address": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

    class Peering(IPFS):

        def __init__(self):
            super(Swarm.Peering, self).__init__()

        def add(
            self,
            address: str
        ) -> dict:
            """
            Add peers into the peering subsystem.

            :param address: address of peer to add into the peering subsystem Required: yes.
            :return response: Response from IPFS.
            """
            replace = {"address": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

        def ls(self) -> dict:
            """
            List peers registered in the peering subsystem.

            :return response: Response from IPFS.
            """
            return self._send(locals())

        def rm(
            self,
            address: str
        ) -> dict:
            """
            Remove peers from the peering subsystem.

            :param address: ID of peer to remove from the peering subsystem Required: yes.
            :return response: Response from IPFS.
            """
            replace = {"address": "arg"}
            return self._send(
                locals(),
                replace=replace
            )
