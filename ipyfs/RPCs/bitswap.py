from ipyfs.ipfs import IPFS


class BitSwap(IPFS):

    def ledger(
        self,
        peer_id: str = None
    ) -> dict:
        """
        Show the current ledger for a peer.

        :param peer_id: Show the current ledger for a peer.
        :return response: Response from IPFS.
        """
        replace = {"peer_id": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def reprovide(self) -> dict:
        """
        Trigger reprovider.
        """
        return self._send(locals())

    def stat(
        self,
        verbose: bool = None,
        human: bool = None
    ) -> dict:
        """
        Show some diagnostic information on the bitswap agent.

        :param verbose: Print extra information. Required: no.
        :param human: Print sizes in human readable format (e.g., 1K 234M 2G). Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    def wantlist(
        self,
        peer: str = None
    ) -> dict:
        """
        Show blocks currently on the wantlist.

        :param peer: Specify which peer to show wantlist for. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())
