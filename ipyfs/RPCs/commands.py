from ipyfs.ipfs import IPFS


class Commands(IPFS):

    def __init__(self):
        super(Commands, self).__init__()
        self.completion = self.Completion()

    def __call__(
        self,
        flags: bool = None
    ) -> dict:
        """
        List all available commands.

        :param flags: Show command flags. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    class Completion(IPFS):

        def __init__(self):
            super(Commands.Completion, self).__init__()

        def bash(self) -> dict:
            """
            Generate bash shell completions.

            :return response: Response from IPFS.
            """
            return self._send(locals())
