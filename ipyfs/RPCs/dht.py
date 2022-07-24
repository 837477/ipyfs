from ipyfs.ipfs import IPFS


class DHT(IPFS):

    def findpeer(
        self,
        peer_id: str,
        verbose: bool = None
    ) -> dict:
        """
        Find the multiaddresses associated with a Peer ID.

        :param peer_id: The ID of the peer to search for. Required: yes.
        :param verbose: Print extra information. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"peer_id": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def findprovs(
        self,
        key: str,
        verbose: bool = None,
        num_providers: int = None
    ) -> dict:
        """
        Find peers that can provide a specific value, given a key.

        :param key: The key to find providers for. Required: yes.
        :param verbose: Print extra information. Required: no.
        :param num_providers: The number of providers to find. Default: 20. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "key": "arg",
            "num_providers": "num-providers"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def get(
        self,
        key: str,
        verbose: bool = None
    ) -> dict:
        """
        Given a key, query the routing system for its best value.

        :param key: The key to find a value for. Required: yes.
        :param verbose: Print extra information. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"key": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def provide(
        self,
        key: str,
        verbose: bool = None,
        recursive: bool = None
    ) -> dict:
        """
        Announce to the network that you are providing given values.

        :param key: The key[s] to send provide records for. Required: yes.
        :param verbose: Print extra information. Required: no.
        :param recursive: Recursively provide entire graph. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"key": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def put(
        self,
        key: str,
        file,
        verbose: bool = None
    ) -> dict:
        """
        Write a key/value pair to the routing system.

        :param key: The key to store the value at. Required: yes.
        :param file: The file to store. Required: yes.
        :param verbose: Print extra information. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"key": "arg"}
        return self._send(
            locals(),
            replace=replace,
            file=file
        )

    def query(
        self,
        peer_id: str,
        verbose: bool = None
    ) -> dict:
        """
        Find the closest Peer IDs to a given Peer ID by querying the DHT.

        :param peer_id: The peerID to run the query against. Required: yes.
        :param verbose: Print extra information. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"peer_id": "arg"}
        return self._send(
            locals(),
            replace=replace
        )
