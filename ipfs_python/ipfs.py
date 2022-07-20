import sys
import requests
from typing import TextIO
from collections import defaultdict


class IPFS:
    def __init__(
        self,
        host: str = "http://localhost",
        port: int = 5001,
        version: int = 0
    ):
        self.host = host
        self.port = port
        self.version = version
        self.uri = (
            f"{self.host}:{self.port}"
            f"/api/v{self.version}"
            f"/{self.__class__.__module__.split('.')[-1].lower()}"
        )
        class_name = self.__class__.__name__.lower()
        if class_name not in self.uri:
            self.uri += f"/{class_name}"

    @staticmethod
    def _response(response: requests.Response) -> dict:
        if response.status_code != 200:
            try:
                raise Exception(response.json())
            except:
                raise Exception(response.text)
        return {
            "status": response.status_code,
            "result": response.json()
        }

    def _send(
        self,
        params: dict,
        replace: dict = None,
        file: TextIO = None
    ) -> dict:
        """
        Request to IPFS.
        """
        # Generate URI
        method = sys._getframe(1).f_code.co_name
        uri = self.uri
        if method != '__call__':
            uri += f"/{method}"

        # Generate Params
        data = defaultdict(list)
        for key, value in params.items():
            if not value or key in ('self', 'replace', 'file'):
                continue
            if replace and key in replace:
                data[replace[key]].append(value)
            else:
                data[key].append(value)
        for key, value in data.items():
            if len(value) == 1:
                data[key] = value[0]

        # Send Request
        return self._response(
            requests.post(
                url=uri,
                params=data,
                files={'file': file}
            )
        )
