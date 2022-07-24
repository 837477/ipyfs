from ipyfs.ipfs import IPFS


class Id(IPFS):

    def __call__(
        self,
        peer_id: str = None,
        format: str = None,
        peerid_base: str = None
    ) -> dict:
        """
        Show IPFS node id info.

        :param peer_id: Peer.ID of node to look up. Required: no.
        :param format: Optional output format. Required: no.
        :param peerid_base: Encoding used for peer IDs: Can either be a multibase encoded CID or a base58btc encoded multihash. Takes {b58mh|base36|k|base32|b...}. Default: b58mh. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "peer_id": "arg",
            "peerid_base": "peerid-base"
        }
        return self._send(
            locals(),
            replace=replace
        )
