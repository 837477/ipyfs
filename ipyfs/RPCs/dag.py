from ipyfs.ipfs import IPFS


class Dag(IPFS):

    def export(
        self,
        cid: str,
        progress: bool = None
    ) -> dict:
        """
        Streams the selected DAG as a .car stream on stdout.

        :param cid: CID of a root to recursively export Required: yes.
        :param progress: Display progress on CLI. Defaults to true when STDERR is a TTY. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"cid": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def get(
        self,
        path: str,
        output_codec: str = None
    ) -> dict:
        """
        Get a DAG node from IPFS.

        :param path: The object to get Required: yes.
        :param output_codec: Format that the object will be encoded as. Default: dag-json. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "output_codec": "output-codec"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def import_(
        self,
        file,
        pin_roots: bool = None,
        silent: bool = None,
        stats: bool = None,
        allow_big_block: bool = None
    ) -> dict:
        """
        Import the contents of .car files

        :param file: The file to import Required: yes.
        :param pin_roots: Pin optional roots listed in the .car headers after importing. Default: true. Required: no.
        :param silent: No output. Required: no.
        :param stats: Output stats. Required: no.
        :param allow_big_block: Disable block size check and allow creation of blocks bigger than 1MiB. WARNING: such blocks won't be transferable over the standard bitswap. Default: false. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "pin_roots": "pin-roots",
            "allow_big_block": "allow-big-block"
        }
        return self._send(
            locals(),
            replace=replace,
            file=file
        )

    def put(
        self,
        file,
        store_codec: str = None,
        input_codec: str = None,
        pin: bool = None,
        hash: str = None,
        allow_big_block: bool = None
    ) -> dict:
        """
        Add a DAG node to IPFS.

        :param file: The file to add Required: yes.
        :param store_codec: Codec that the stored object will be encoded with. Default: dag-cbor. Required: no.
        :param input_codec: Codec that the input object is encoded in. Default: dag-json. Required: no.
        :param pin: Pin this object when adding. Required: no.
        :param hash: Hash function to use. Default: sha2-256. Required: no.
        :param allow_big_block: Disable block size check and allow creation of blocks bigger than 1MiB. WARNING: such blocks won't be transferable over the standard bitswap. Default: false. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "store_codec": "store-codec",
            "input_codec": "input-codec",
            "allow_big_block": "allow-big-block"
        }
        return self._send(
            locals(),
            replace=replace,
            file=file
        )

    def resolve(
        self,
        path: str
    ) -> dict:
        """
        Resolve IPLD block.

        :param path: The path to resolve Required: yes.
        :return response: Response from IPFS.
        """
        replace = {"path": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def stat(
        self,
        cid: str,
        progress: bool = None
    ) -> dict:
        """
        Gets stats for a DAG.

        :param cid: CID of a DAG root to get statistics for Required: yes.
        :param progress: Return progressive data while reading through the DAG. Default: true. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"cid": "arg"}
        return self._send(
            locals(),
            replace=replace
        )
