from ipyfs.ipfs import IPFS


class Block(IPFS):

    def get(
        self,
        cid: str
    ) -> dict:
        """
        Get a raw IPFS block.

        :param cid: The CID of an existing block to get. Required: yes.
        :return response: Response from IPFS.
        """
        replace = {"cid": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def put(
        self,
        cid_codec: str = None,
        mhtype: str = None,
        mhlen: int = None,
        pin: bool = None,
        allow_big_block: bool = None,
        format: str = None
    ) -> dict:
        """
        Store input as an IPFS block.

        :param cid_codec: Multicodec to use in returned CID. Default: raw. Required: no.
        :param mhtype: Multihash hash function. Default: sha2-256. Required: no.
        :param mhlen: Multihash hash length. Default: -1. Required: no.
        :param pin: Pin added blocks recursively. Default: false. Required: no.
        :param allow_big_block: Disable block size check and allow creation of blocks bigger than 1MiB. WARNING: such blocks won't be transferable over the standard bitswap. Default: false. Required: no.
        :param format: Use legacy format for returned CID (DEPRECATED). Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "cid_codec": "cid-codec",
            "allow_big_block": "allow-big-block"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def rm(
        self,
        cid: str,
        force: bool = None,
        quiet: bool = None
    ) -> dict:
        """
        Remove IPFS block(s) from the local datastore.

        :param cid: CIDs of block(s) to remove. Required: yes.
        :param force: Ignore nonexistent blocks. Required: no.
        :param quiet: Write minimal output. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"cid": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def stat(
        self,
        cid: str
    ) -> dict:
        """
        Print information of a raw IPFS block.

        :param cid: The CID of an existing block to stat. Required: yes.
        :return response: Response from IPFS.
        """
        replace = {"cid": "arg"}
        return self._send(
            locals(),
            replace=replace
        )
