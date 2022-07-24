from ipyfs.ipfs import IPFS


class Cid(IPFS):

    def base32(
        self,
        arg: str,
    ) -> dict:
        """
        Convert CIDs to Base32 CID version 1.

        :param cid: CIDs to convert. Required: yes.
        :return response: Response from IPFS.
        """
        replace = {"cid": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def bases(
        self,
        prefix: bool = None,
        numeric: bool = None
    ) -> dict:
        """
        List available multibase encodings.

        :param prefix: also include the single letter prefixes in addition to the code. Required: no.
        :param numeric: also include numeric codes. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    def codecs(
        self,
        numeric: bool = None,
        supported: bool = None
    ) -> dict:
        """
        List available CID multicodecs.

        :param numeric: also include numeric codes. Required: no.
        :param supported: list only codecs supported by go-ipfs commands. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    def format(
        self,
        cid: str,
        f: str = None,
        v: str = None,
        mc: str = None,
        b: str = None
    ) -> dict:
        """
        Format and convert a CID in various useful ways.

        :param cid: CIDs to format. Required: yes.
        :param f: Printf style format string. Default: %s. Default: %s. Required: no.
        :param v: CID version to convert to. Required: no.
        :param mc: CID multicodec to convert to. Required: no.
        :param b: Multibase to display CID in. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"cid": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def hashes(
        self,
        numeric: bool = None,
        supported: bool = None
    ) -> dict:
        """
        List available multihashes.

        :param numeric: also include numeric codes. Required: no.
        :param supported: list only codecs supported by go-ipfs commands. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

