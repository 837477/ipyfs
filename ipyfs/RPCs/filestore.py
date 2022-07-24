from ipyfs.ipfs import IPFS


class FileStore(IPFS):

    def dups(self):
        """
        List blocks that are both in the filestore and standard block storage.
        """
        return self._send(locals())

    def ls(
        self,
        cid: str = None,
        file_order: bool = None
    ) -> dict:
        """
        List objects in filestore.

        :param cid: Cid of objects to list. Required: no.
        :param file_order: sort the results based on the path of the backing file. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "cid": "arg",
            "file_order": "file-order"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def verify(
        self,
        cid: str = None,
        file_order: bool = None
    ) -> dict:
        """
        Verify objects in filestore.

        :param cid: Cid of objects to verify. Required: no.
        :param file_order: verify the objects based on the order of the backing file. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "cid": "arg",
            "file_order": "file-order"
        }
        return self._send(
            locals(),
            replace=replace
        )
