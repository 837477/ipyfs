from ipyfs.ipfs import IPFS


class Cat(IPFS):

    def __call__(
        self,
        path: str,
        offset: int = None,
        length: int = None,
        progress: bool = None,
    ) -> dict:
        """
        Show IPFS object data.

        :param path: The path to the IPFS object(s) to be outputted. Required: yes.
        :param offset: Byte offset to begin reading from. Required: no.
        :param length: Maximum number of bytes to read. Required: no.
        :param progress: Stream progress data. Default: true. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"path": "arg"}
        return self._send(
            locals(),
            replace=replace
        )
