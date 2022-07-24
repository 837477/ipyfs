from ipyfs.ipfs import IPFS


class Log(IPFS):

    def level(
        self,
        subsystem: str,
        level: str
    ) -> dict:
        """
        Change the logging level.

        :param subsystem: The subsystem logging identifier. Use 'all' for all subsystems. Required: yes.
        :param level: The log level, with 'debug' the most verbose and 'fatal' the least verbose.
        One of debug, info, warn, error, dpanic, panic, fatal. Required: yes.
        :return response: Response from IPFS.
        """
        replace = {
            "subsystem": "arg",
            "level": "arg"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def ls(self) -> dict:
        """
        List the logging subsystems.

        :return response: Response from IPFS.
        """
        return self._send(locals())
