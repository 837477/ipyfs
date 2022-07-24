from ipyfs.ipfs import IPFS


class Repo(IPFS):

    def gc(
        self,
        stream_errors: bool = None,
        quiet: bool = None,
        silent: bool = None
    ) -> dict:
        """
        Perform a garbage collection sweep on the repo.

        :param stream_errors: Stream errors. Required: no.
        :param quiet: Write minimal output. Required: no.
        :param silent: Write no output. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"stream_errors": "stream-errors"}
        return self._send(
            locals(),
            replace=replace
        )

    def stat(
        self,
        size_only: bool = None,
        human: bool = None
    ) -> dict:
        """
        Get stats for the currently used repo.

        :param size_only: Only report RepoSize and StorageMax. Required: no.
        :param human: Print sizes in human readable format (e.g., 1K 234M 2G). Required: no.
        :return response: Response from IPFS.
        """
        replace = {"size_only": "size-only"}
        return self._send(
            locals(),
            replace=replace
        )

    def verify(self) -> dict:
        """
        Verify all blocks in repo are not corrupted.

        :return response: Response from IPFS.
        """
        return self._send(locals())

    def version(
        self,
        quiet: bool = None
    ) -> dict:
        """
        Show the version of IPFS.

        :param quiet: Write minimal output. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())
