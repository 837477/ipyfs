from ipyfs.ipfs import IPFS


class Files(IPFS):

    def chcid(
        self,
        path: str = None,
        cid_version: int = None,
        hash: str = None
    ) -> dict:
        """
        Change the CID version or hash function of the root node of a given path.

        :param path: Path to change. Default: '/'. Required: no.
        :param cid_version: Cid version to use. (experimental). Required: no.
        :param hash: Hash function to use. Will set Cid version to 1 if used. (experimental). Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "cid_version": "cid-version"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def cp(
        self,
        source: str,
        dest: str,
        parents: bool = None
    ) -> dict:
        """
        Add references to IPFS files and directories in MFS (or copy within MFS).

        :param source: Source IPFS or MFS path to copy. Required: yes.
        :param dest: Destination within MFS. Required: yes.
        :param parents: Make parent directories as needed. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "source": "arg",
            "dest": "arg"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def flush(
        self,
        path: str = None
    ) -> dict:
        """
        Flush the given path (for directories).

        :param path: Path to flush. Default: '/'. Required: no.
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
        long: bool = None,
        u: bool = None,
    ) -> dict:
        """
        List the given path.

        :param path: Path to list. Default: '/'. Required: no.
        :param long: Long listing. Required: no.
        :param u: Do not sort; list entries in directory order. Required: no.
        :return response: Response from IPFS.
        """
        replace = {'path': 'arg'}
        return self._send(
            locals(),
            replace=replace
        )

    def mkdir(
        self,
        path: str,
        parents: bool = None,
        cid_version: int = None,
        hash: str = None
    ) -> dict:
        """
        Create a directory at the given path.

        :param path: Path to create. Default: '/'. Required: no.
        :param parents: Create parent directories as needed. Required: no.
        :param cid_version: Cid version to use. (experimental). Required: no.
        :param hash: Hash function to use. Will set Cid version to 1 if used. (experimental). Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "cid_version": "cid-version"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def mv(
        self,
        source: str,
        dest: str
    ) -> dict:
        """
        Move IPFS files and directories.

        :param source: Source IPFS or MFS path to move. Required: yes.
        :param dest: Destination within MFS. Required: yes.
        :return response: Response from IPFS.
        """
        replace = {
            "source": "arg",
            "dest": "arg"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def read(
        self,
        path: str,
        offset: int = None,
        count: int = None
    ) -> dict:
        """
        Read a file in a given MFS.

        :param path: Path to read. Required: yes.
        :param offset: Byte offset to begin reading from. Required: no.
        :param count: Maximum number of bytes to read. Required: no.
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
        recursive: bool = None,
        force: bool = None
    ) -> dict:
        """
        Remove a file or directory.

        :param path: File to remove. Required: yes.
        :param recursive: Recursively remove directories. Required: no.
        :param force: Forcibly remove target at path; implies -r for directories. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"path": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def stat(
        self,
        path: str,
        format: str = None,
        hash: bool = None,
        size: bool = None,
        with_local: bool = None
    ) -> dict:
        """
        Display file status.

        :param path: Path to node to stat. Required: yes.
        :param format: Print statistics in given format. Allowed tokens: <hash> <size> <cumulsize> <type> <childs>. Conflicts with other format options. Default: <hash>
        Size: <size>
        CumulativeSize: <cumulsize>
        ChildBlocks: <childs>
        Type: <type>. Default: <hash> Size: <size> CumulativeSize: <cumulsize> ChildBlocks: <childs> Type: <type>. Required: no.
        :param hash: Print only hash. Implies '--format=<hash>'. Conflicts with other format options. Required: no.
        :param size: Print only size. Implies '--format=<cumulsize>'. Conflicts with other format options. Required: no.
        :param with_local: Compute the amount of the dag that is local, and if possible the total size. Required: no.
        """
        replace = {
            "path": "arg",
            "with_local": "with-local"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def write(
        self,
        path: str,
        file,
        offset: int = None,
        create: bool = None,
        parents: bool = None,
        truncate: bool = None,
        count: int = None,
        raw_leaves: bool = None,
        cid_version: int = None,
        hash: str = None
    ) -> dict:
        """
        Write to a mutable file in a given filesystem.

        :param path: [string]: Path to write to. Required: yes.
        :param file: File to write. Required: yes.
        :param offset: Byte offset to begin writing at. Required: no.
        :param create: Create the file if it does not exist. Required: no.
        :param parents: Make parent directories as needed. Required: no.
        :param truncate: Truncate the file to size zero before writing. Required: no.
        :param count: Maximum number of bytes to read. Required: no.
        :param raw_leaves: Use raw blocks for newly created leaf nodes. (experimental). Required: no.
        :param cid_version: Cid version to use. (experimental). Required: no.
        :param hash: Hash function to use. Will set Cid version to 1 if used. (experimental). Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "raw_leaves": "raw-leaves",
            "cid_version": "cid-version"
        }
        return self._send(
            locals(),
            replace=replace,
            file=file
        )
