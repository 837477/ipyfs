from ipyfs.ipfs import IPFS


class Refs(IPFS):

    def __call__(
        self,
        path: str,
        format: str = None,
        edges: bool = None,
        unique: bool = None,
        recursive: bool = None,
        max_depth: int = None
    ) -> dict:
        """
        List links (references) from an object.

        :param path: Path to the object(s) to list refs from. Required: yes.
        :param format: Emit edges with given format. Available tokens: <src> <dst> <linkname>. Default: <dst>. Default: <dst>. Required: no.
        :param edges: Emit edge format: &lt;from&gt; -&gt; &lt;to&gt;. Required: no.
        :param unique: Omit duplicate refs from output. Required: no.
        :param recursive: Recursively list links of child nodes. Required: no.
        :param max_depth: Only for recursive refs, limits fetch and listing to the given depth. Default: -1. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "path": "arg",
            "max_depth": "max-depth"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def local(self) -> dict:
        """
        List local references.

        :return response: Response from IPFS.
        """
        return self._send(locals())
