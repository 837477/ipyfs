from ipyfs.ipfs import IPFS


class Name(IPFS):

    def publish(
        self,
        path: str,
        resolve: bool = None,
        lifetime: str = None,
        allow_offline: bool = None,
        ttl: str = None,
        key: str = None,
        quieter: bool = None,
        ipns_base: str = None
    ) -> dict:
        """
        Publish IPNS names.

        :param path: ipfs path of the object to be published. Required: yes.
        :param resolve: Check if the given path can be resolved before publishing. Default: true. Required: no.
        :param lifetime: Time duration that the record will be valid for.
        This accepts durations such as "300s", "1.5h" or "2h45m". Valid time units are
        "ns", "us" (or "µs"), "ms", "s", "m", "h". Default: 24h. Required: no.
        :param allow_offline: When offline, save the IPNS record to the the local datastore without broadcasting to the network instead of simply failing. Required: no.
        :param ttl: Time duration this record should be cached for. Uses the same syntax as the lifetime option. (caution: experimental). Required: no.
        :param key: Name of the key to be used or a valid PeerID, as listed by 'ipfs key list -l'. Default: self. Required: no.
        :param quieter: Write only final hash. Required: no.
        :param ipns_base: Encoding used for keys: Can either be a multibase encoded CID or a base58btc encoded multihash. Takes {b58mh|base36|k|base32|b...}. Default: base36. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "allow_offline": "allow-offline",
            "ipns_base": "ipns-base"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def resolve(
        self,
        name: str = None,
        recursive: bool = None,
        nocache: bool = None,
        dht_record_count: int = None,
        dht_timeout: str = None,
        stream: bool = None
    ) -> dict:
        """
        Resolve IPNS names.

        :param name: The IPNS name to resolve. Defaults to your node's peerID. Required: no.
        :param recursive: Resolve until the result is not an IPNS name. Default: true. Required: no.
        :param nocache: Do not use cached entries. Required: no.
        :param dht_record_count: Number of records to request for DHT resolution. Required: no.
        :param dht_timeout: Max time to collect values during DHT resolution eg "30s". Pass 0 for no timeout. Required: no.
        :param stream: Stream entries as they are found. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "name": "arg",
            "dht_record_count": "dht-record-count",
            "dht_timeout": "dht-timeout"
        }
        return self._send(
            locals(),
            replace=replace
        )
