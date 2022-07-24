from ipyfs.ipfs import IPFS


class Resolve(IPFS):

    def __call__(
        self,
        name: str,
        recursive: bool = None,
        dht_record_count: int = None,
        dht_timeout: str = None
    ) -> dict:
        """
        Resolve the value of names to IPFS.

        :param name: The name to resolve. Required: yes.
        :param recursive: Resolve until the result is an IPFS name. Default: true. Required: no.
        :param dht_record_count: Number of records to request for DHT resolution. Required: no.
        :param dht_timeout: Max time to collect values during DHT resolution eg "30s". Pass 0 for no timeout. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"name": "arg"}
        return self._send(
            locals(),
            replace=replace
        )
