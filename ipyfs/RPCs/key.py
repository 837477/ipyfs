from ipyfs.ipfs import IPFS


class Key(IPFS):

    def export(
        self,
        name: str,
        output: str = None,
        format: str = None
    ) -> dict:
        """
        Export a keypair

        :param name: name of key to export Required: yes.
        :param output: The path where the output should be stored. Required: no.
        :param format: The format of the exported private key, libp2p-protobuf-cleartext or pem-pkcs8-cleartext. Default: libp2p-protobuf-cleartext. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"name": "arg"}
        return self._send(
            locals(),
            replace=replace
        )

    def gen(
        self,
        name: str,
        type: str = None,
        size: int = None,
        ipns_base: str = None
    ) -> dict:
        """
        Create a new keypair

        :param name: name of key to create Required: yes.
        :param type: type of the key to create: rsa, ed25519. Default: ed25519. Required: no.
        :param size: size of the key to generate. Required: no.
        :param ipns_base: Encoding used for keys: Can either be a multibase encoded CID or a base58btc encoded multihash. Takes {b58mh|base36|k|base32|b...}. Default: base36. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "name": "arg",
            "ipns_base": "ipns-base"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def import_(
        self,
        file,
        name: str,
        ipns_base: str = None,
        format: str = None,
        allow_any_key_type: bool = None
     ) -> dict:
        """
        Import a key and prints imported key id

        :param file: file to import. Required: yes.
        :param name: name to associate with key in keychain Required: yes.
        :param ipns_base: Encoding used for keys: Can either be a multibase encoded CID or a base58btc encoded multihash. Takes {b58mh|base36|k|base32|b...}. Default: base36. Required: no.
        :param format: The format of the private key to import, libp2p-protobuf-cleartext or pem-pkcs8-cleartext. Default: libp2p-protobuf-cleartext. Required: no.
        :param allow_any_key_type: Allow importing any key type. Default: false. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "name": "arg",
            "ipns_base": "ipns-base",
            "allow_any_key_type": "allow-any-key-type"
        }
        return self._send(
            locals(),
            replace=replace,
            file=file
        )

    def list(
        self,
        l: bool = None,
        ipns_base: str = None
    ) -> dict:
        """
        List all local keypairs.

        :param l: Show extra information about keys. Required: no.
        :param ipns_base: Encoding used for keys: Can either be a multibase encoded CID or a base58btc encoded multihash. Takes {b58mh|base36|k|base32|b...}. Default: base36. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    def rename(
        self,
        old_name: str,
        new_name: str,
        force: bool = None,
        ipns_base: str = None
    ) -> dict:
        """
        Rename a keypair

        :param old_name: name of key to rename Required: yes.
        :param new_name: new name of the key Required: yes.
        :param force: Allow to overwrite an existing key. Required: no.
        :param ipns_base: Encoding used for keys: Can either be a multibase encoded CID or a base58btc encoded multihash. Takes {b58mh|base36|k|base32|b...}. Default: base36. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "old_name": "arg",
            "new_name": "arg",
            "ipns_base": "ipns-base"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def rm(
        self,
        name: str,
        l: bool = None,
        ipns_base: str = None
    ) -> dict:
        """
        Remove a keypair.

        :param arg: names of keys to remove Required: yes.
        :param l: Show extra information about keys. Required: no.
        :param ipns_base: Encoding used for keys: Can either be a multibase encoded CID or a base58btc encoded multihash. Takes {b58mh|base36|k|base32|b...}. Default: base36. Required: no.
        :return response: Response from IPFS.
        """
        replace = {
            "name": "arg",
            "ipns_base": "ipns-base"
        }
        return self._send(
            locals(),
            replace=replace
        )

    def rotate(
        self,
        old_key: str = None,
        type: str = None,
        size: int = None
    ) -> dict:
        """
        Rotates the IPFS identity.

        :param old_key: Keystore name to use for backing up your existing identity. Required: no.
        :param type: type of the key to create: rsa, ed25519. Default: ed25519. Required: no.
        :param size: size of the key to generate. Required: no.
        :return response: Response from IPFS.
        """
        replace = {"old_key": "oldkey"}
        return self._send(
            locals(),
            replace=replace
        )
