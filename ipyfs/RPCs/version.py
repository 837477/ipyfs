from ipyfs.ipfs import IPFS


class Version(IPFS):

    def __call__(
        self,
        number: bool = None,
        commit: bool = None,
        repo: bool = None,
        all: bool = None
    ) -> dict:
        """
        Show IPFS version information.

        :param number: Only show the version number. Required: no.
        :param commit: Show the commit hash. Required: no.
        :param repo: Show repo version. Required: no.
        :param all: Show all version information. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    def deps(self):
        """
        Shows information about dependencies used for build.

        :return response: Response from IPFS.
        """
        return self._send(locals())
