from ipyfs.ipfs import IPFS


class Stats(IPFS):

    def bitswap(
        self,
        verbose: bool = None,
        human: bool = None
    ) -> dict:
        """
        Show some diagnostic information on the bitswap agent.

        :param verbose: Print extra information. Required: no.
        :param human: Print sizes in human readable format (e.g., 1K 234M 2G). Required: no.
        """
        return self._send(locals())

    def bw(
        self,
        peer: str = None,
        proto: str = None,
        poll: bool = None,
        interval: str = None
    ) -> dict:
        """
        Print IPFS bandwidth information.

        :param peer: Specify a peer to print bandwidth for. Required: no.
        :param proto: Specify a protocol to print bandwidth for. Required: no.
        :param poll: Print bandwidth at an interval. Required: no.
        :param interval: Time interval to wait between updating output, if 'poll' is true.
        This accepts durations such as "300s", "1.5h" or "2h45m". Valid time units are:
        "ns", "us" (or "µs"), "ms", "s", "m", "h". Default: 1s. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    def dht(
        self,
        dht: str = None
    ) -> dict:
        """
        Returns statistics about the node's DHT(s).

        :param dht: The DHT whose table should be listed (wanserver, lanserver, wan, lan).
        wan and lan refer to client routing tables.
        When using the experimental DHT client only WAN is supported.
        Defaults to wan and lan. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"dht": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def provide(self) -> dict:
        """
        Returns statistics about the node's (re)provider system.

        :return response: Response from IPFS.
        """
        return self._send(locals())

    def repo(
        self,
        size_only: bool = None,
        human: bool = None
    ) -> dict:
        """
        Get stats for the currently used repo.

        :param size_only: Only report RepoSize and StorageMax. Required: no.
        :param human: Print sizes in human readable format (e.g., 1K 234M 2G). Required: no.
        :return response: Response from IPFS.
        """
        replace = {"size_only": "size-only"}
        return self._send(
            locals(),
            replace=replace
        )
