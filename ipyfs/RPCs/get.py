from ipyfs.ipfs import IPFS


class Get(IPFS):

    def __call__(
        self,
        path: str,
        output: str = None,
        archive: bool = None,
        compress: bool = None,
        compression_level: int = None,
        progress: bool = None
    ) -> dict:
        """
        Download IPFS objects.

        :param path: The path to the IPFS object(s) to be outputted. Required: yes.
        :param output: The path where the output should be stored. Required: no.
        :param archive: Output a TAR archive. Required: no.
        :param compress: Compress the output with GZIP compression. Required: no.
        :param compression_level: The level of compression (1-9). Required: no.
        :param progress: Stream progress data. Default: true. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "compression_level": "compression-level"
        }
        return self._send(
            locals(),
            replace=replace
        )
