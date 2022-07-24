from ipyfs.ipfs import IPFS


class Pin(IPFS):

    def __init__(self):
        super(Pin, self).__init__()
        self.remote = self.Remote()

    def add(
        self,
        path: str,
        recursive: bool = None,
        progress: bool = None
    ) -> dict:
        """
        Pin objects to local storage.

        :param path: Path to object(s) to be pinned. Required: yes.
        :param recursive: Recursively pin the object linked to by the specified object(s). Default: true. Required: no.
        :param progress: Show progress. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"path": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def ls(
        self,
        path: str = None,
        type: str = None,
        quiet: bool = None,
        stream: bool = None
    ) -> dict:
        """
        List objects pinned to local storage.

        :param path: Path to object(s) to be listed. Required: no.
        :param type: The type of pinned keys to list. Can be "direct", "indirect", "recursive", or "all". Default: all. Required: no.
        :param quiet: Write just hashes of objects. Required: no.
        :param stream: Enable streaming of pins as they are discovered. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"path": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def rm(
        self,
        path: str,
        recursive: bool = None
    ) -> dict:
        """
        Remove object from pin-list.

        :param path: Path to object(s) to be unpinned. Required: yes.
        :param recursive: Recursively unpin the object linked to by the specified object(s). Default: true. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"path": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def update(
        self,
        old_path: str,
        new_path: str,
        unpin: bool = None
    ) -> dict:
        """
        Update a recursive pin.

        :param old_path: Path to old object. Required: yes.
        :param new_path: Path to a new object to be pinned. Required: yes.
        :param unpin: Remove the old pin. Default: true. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "old_path": "arg",
            "new_path": "arg"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def verify(
        self,
        verbose: bool = None,
        quiet: bool = None
    ) -> dict:
        """
        Verify that recursive pins are complete.

        :param verbose: Also write the hashes of non-broken pins. Required: no.
        :param quiet: Write just hashes of broken pins. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    class Remote(IPFS):

        def __init__(self):
            super(Pin.Remote).__init__()
            self.service = self.Service()

        def add(
            self,
            path: str,
            service: str = None,
            name: str = None,
            background: bool = None
        ) -> dict:
            """
            Pin object to remote pinning service.

            :param path: Path to object(s) to be pinned. Required: yes.
            :param service: Name of the remote pinning service to use (mandatory). Required: no.
            :param name: An optional name for the pin. Required: no.
            :param background: Add to the queue on the remote service and return immediately (does not wait for pinned status). Default: false. Required: no.
            :return response: Response from IPFS.
            """
            replace = {"path": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

        def ls(
            self,
            service: str = None,
            name: str = None,
            cid: list = None,
            status: list = None
        ) -> dict:
            """
            List objects pinned to remote pinning service.

            :param service: Name of the remote pinning service to use (mandatory). Required: no.
            :param name: Return pins with names that contain the value provided (case-sensitive, exact match). Required: no.
            :param cid: Return pins for the specified CIDs (comma-separated). Required: no.
            :param status: Return pins with the specified statuses (queued,pinning,pinned,failed). Default: [pinned]. Required: no.
            :return response: Response from IPFS.
            """
            return self._send(locals())

        def rm(
            self,
            service: str = None,
            name: str = None,
            cid: list = None,
            status: list = None,
            force: bool = None
        ) -> dict:
            """
            Remove pins from remote pinning service.

            :param service: Name of the remote pinning service to use (mandatory). Required: no.
            :param name: Remove pins with names that contain provided value (case-sensitive, exact match). Required: no.
            :param cid: Remove pins for the specified CIDs. Required: no.
            :param status: Remove pins with the specified statuses (queued,pinning,pinned,failed). Default: [pinned]. Required: no.
            :param force: Allow removal of multiple pins matching the query without additional confirmation. Default: false. Required: no.
            :return response: Response from IPFS.
            """
            return self._send(locals())

        class Service(IPFS):

            def __init__(self):
                super(Pin.Remote.Service).__init__()

            def add(
                self,
                service: str,
                endpoint: str,
                key: str
            ) -> dict:
                """
                Add remote pinning service.

                :param service: Service name. Required: yes.
                :param endpoint: Service endpoint. Required: yes.
                :param key: Service key. Required: yes.
                :return response: Response from IPFS.
                """
                replace = {
                    "service": "arg",
                    "endpoint": "arg",
                    "key": "arg"
                }
                return self._send(
                    locals(),
                    replace=replace
                )

            def ls(
                self,
                stat: bool = None
            ) -> dict:
                """
                List remote pinning services.

                :param stat: Try to fetch and display current pin count on remote service (queued/pinning/pinned/failed). Default: false. Required: no.
                :return response: Response from IPFS.
                """
                return self._send(locals())

            def rm(
                self,
                service: str
            ) -> dict:
                """
                Remove remote pinning service.

                :param service: Name of remote pinning service to remove. Required: yes.
                :return response: Response from IPFS.
                """
                replace = {"service": "arg"}
                return self._send(
                    locals(),
                    replace=replace
                )
