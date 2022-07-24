from ipyfs.ipfs import IPFS


class LS(IPFS):

    def __call__(
        self,
        path: str,
        headers: bool = None,
        resolve_type: bool = None,
        size: bool = None,
        stream: bool = None
    ) -> dict:
        """
        List directory contents for Unix filesystem objects.

        :param arg: The path to the IPFS object(s) to list links from. Required: yes.
        :param headers: Print table headers (Hash, Size, Name). Required: no.
        :param resolve_type: Resolve linked objects to find out their types. Default: true. Required: no.
        :param size: Resolve linked objects to find out their file size. Default: true. Required: no.
        :param stream: Enable experimental streaming of directory entries as they are traversed. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "resolve_type": "resolve-type"
        }
        return self._send(
            locals(),
            replace=replace
        )
