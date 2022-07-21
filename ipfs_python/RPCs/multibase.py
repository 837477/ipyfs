from typing import TextIO
from ipfs_python.ipfs import IPFS


class MultiBase(IPFS):

    def decode(
        self,
        file: TextIO
    ) -> dict:
        """
        Decode multibase string

        :param file: File to decode. Required: yes.
        :return response: Response from IPFS.
        """
        return self._send(
            locals(),
            file=file
        )

    def encode(
        self,
        file: TextIO,
        base: str
    ) -> dict:
        """
        Encode data into a multibase string

        :param file: File to encode. Required: yes.
        :param base: multibase encoding. Default: base64url. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"base": "b"}
        return self._send(
            locals(),
            replace=replace,
            file=file
        )

    def list(
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

    def transcode(
        self,
        file: TextIO,
        base: str = None
    ) -> dict:
        """
        Transcode multibase string between bases

        :param file: File to transcode. Required: yes.
        :param base: multibase encoding. Default: base64url. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"base": "b"}
        return self._send(
            locals(),
            replace=replace,
            file=file
        )
