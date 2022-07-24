from ipyfs.ipfs import IPFS


class Update(IPFS):

    def __call__(
        self,
        arg: str = None
    ) -> dict:
        """
        Update ipfs.

        :param arg: Arguments for subcommand. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())
