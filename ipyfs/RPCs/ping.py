from ipyfs.ipfs import IPFS


class Ping(IPFS):

    def __call__(
        self,
        peer_id: str,
        count: int = None
    ) -> dict:
        """
        Send echo request packets to IPFS hosts.

        :param peer_id: ID of peer to be pinged. Required: yes.
        :param count: Number of ping messages to send. Default: 10. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"peer_id": "arg"}
        return self._send(
            locals(),
            replace=replace
        )
