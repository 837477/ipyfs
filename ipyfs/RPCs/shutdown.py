from ipyfs.ipfs import IPFS


class Shutdown(IPFS):

    def __call__(self) -> dict:
        """
        Shut down the ipfs daemon.

        :return response: Response from IPFS.
        """
        return self._send(locals())
