from ipyfs.ipfs import IPFS


class Config(IPFS):

    def __init__(self):
        super(Config, self).__init__()
        self.profile = self.Profile()

    def __call__(
        self,
        key: str,
        value: str = None,
        bool: bool = None,
        json: bool = None
    ) -> dict:
        """
        Get and set IPFS config values.

        :param key: The key of the config entry (e.g. "Addresses.API"). Required: yes.
        :param valueng: The value to set the config entry to. Required: no.
        :param bool: Set a boolean value. Required: no.
        :param json: Parse stringified JSON. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "key": "arg",
            "value": "arg"
        }
        return self._send(
            locals(),
            replace=replace
        )

    class Profile(IPFS):

        def __init__(self):
            super(Config.Profile, self).__init__()

        def apply(
            self,
            profile: str,
            dry_run: bool = None
        ) -> dict:
            """
            Apply profile to config.

            :param profile: The profile to apply. Required: yes.
            :param dry_run: Show diff of config changes. Default: false. Required: no.
            :return response: Response from IPFS.
            """
            replace = {"profile": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

    def edit(self) -> dict:
        """
        Open the config file for editing in $EDITOR.

        :return response: Response from IPFS.
        """
        return self._send(locals())

    def replace(
        self,
        file
    ) -> dict:
        """
        Replace the config with <file>.

        :param file: File to replace the config with. Required: yes.
        :return response: Response from IPFS.
        """
        return self._send(
            locals(),
            file=file
        )

    def show(self) -> dict:
        """
        Output config file contents.

        :return response: Response from IPFS.
        """
        return self._send(locals())
