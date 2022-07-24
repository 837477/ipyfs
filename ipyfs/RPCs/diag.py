from ipyfs.ipfs import IPFS


class Diag(IPFS):

    def __init__(self):
        super(Diag, self).__init__()
        self.cmds = self.Cmds()

    class Cmds(IPFS):

        def __init__(self):
            super(Diag.Cmds, self).__init__()

        def __call__(
            self,
            verbose: bool = None
        ) -> dict:
            """
            List commands run on this IPFS node.

            :param verbose: Print extra information. Required: no.
            :return response: Response from IPFS.
            """
            return self._send(locals())

        def clear(self) -> dict:
            """
            Clear inactive requests from the log.

            :return response: Response from IPFS.
            """
            return self._send(locals())

        def set_time(
            self,
            time: str,
            verbose: bool = None
        ) -> dict:
            """
            Set how long to keep inactive requests in the log.

            :param time: Time to keep inactive requests in log. Required: yes.
            :param verbose: Print extra information. Required: no.
            :return response: Response from IPFS.
            """
            replace = {"time": "arg"}
            return self._send(
                locals(),
                replace=replace
            )

    def profile(
        self,
        output: str = None,
        collectors: list = None,
        profile_time: str = None,
        mutex_profile_fraction: int = None,
        block_profile_rate: str = None
    ) -> dict:
        """
        Collect a performance profile for debugging.

        :param output: The path where the output .zip should be stored. Default: ./ipfs-profile-[timestamp].zip. Required: no.
        :param collectors: The list of collectors to use for collecting diagnostic data. Default: [goroutines-stack goroutines-pprof version heap bin cpu mutex block]. Default: [goroutines-stack goroutines-pprof version heap bin cpu mutex block]. Required: no.
        :param profile_time: The amount of time spent profiling. If this is set to 0, then sampling profiles are skipped. Default: 30s. Required: no.
        :param mutex_profile_fraction: The fraction 1/n of mutex contention events that are reported in the mutex profile. Default: 4. Required: no.
        :param block_profile_rate: The duration to wait between sampling goroutine-blocking events for the blocking profile. Default: 1ms. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "profile_time": "profile-time",
            "mutex_profile_fraction": "mutex-profile-fraction",
            "block_profile_rate": "block-profile-rate"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def sys(self) -> dict:
        """
        Print system diagnostic information.

        :return response: Response from IPFS.
        """
        return self._send(locals())
