<p align="center">
  <a href="https://github.com/837477/IPyFS"><img src="https://user-images.githubusercontent.com/37999795/180646280-7774e259-bc91-4ed3-8b68-84d705ff61c5.png"></a>
</p>
<p align="center">
    <em>IPFS allows you to easily control IPFS System in Python. (IPFS Python CLI)</em>
</p>
<p align="center">
<a href="https://github.com/837477/IPyFS/blob/main/LICENSE" target="_blank">
    <img src="https://img.shields.io/badge/License-MIT-19bfb6" alt="License">
</a>
<a href="https://pypi.org/project/ipyfs" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.7 | 3.8 | 3.9 | 3.10-19bfb6" alt="Package version">
</a>
<a href="https://pypi.org/project/ipyfs" target="_blank">
    <img src="https://img.shields.io/badge/Release-0.1.0-19bfb6" alt="Supported Python versions">
</a>
</p>

---

**IPFS RPC APIs Documnets**: <a href="https://docs.ipfs.io/reference/kubo/rpc/" target="_blank">https://docs.ipfs.io/reference/kubo/rpc </a>

**Source Code**: <a href="https://github.com/837477/IPyFS" target="_blank">https://github.com/837477/IPyFS </a>

---

IPyFS is a Python-based IPFS CLI.

The key features are:

* **Base**: IPyFS is built based on IPFS RPC APIs.
* **Easy**: It is designed to be easy to use and learn. You can simply refer to the IPFS RPC APIs document.

## Requirements

Python 3.7+

IPyFS stands on the shoulders of giants:

* <a href="https://docs.ipfs.io/install/" class="external-link" target="_blank">IPFS Daemon</a> for the IPFS server.
* <a href="https://github.com/psf/requests" class="external-link" target="_blank">Requests</a> For communication with IPFS Daemon.

<small>* It's so obvious! Since IPyFS is a Python-based IPFS CLI, IPFS Server must be running.</small>

## Installation

<div class="termy">

```console
$ pip install ipyfs
```

</div>

## Example

### Simple IPyFS usage

```Python
from ipyfs import Files, Swarm  # + Etc.

# Host and port can be modified for each IPyFS controller.
files = Files(
    host="http://localhost",  # Set IPFS Daemon Host
    port=5001  # Set IPFS Daemon Port
)
swarm = Swarm(
    host="http://sample.ipyfs.com",  # Set IPFS Daemon Host
    port=7477  # Set IPFS Daemon Port
)
```

The parameters of the IPyFS module are designed to be almost identical to the parameters of the IPFS RPC APIs.

### Example of NFT Metadata Upload

* You can check it in the `sample.py` file.

<div class="termy">

```Python
"""
Example of NFT Metadata Upload
"""
from ipyfs import Files
import json


# You can customize the host and port on any controller.
files = Files(
    host="http://localhost",  # Set IPFS Daemon Host
    port=5001  # Set IPFS Daemon Port
)

# Read the file and upload it to IPFS.
with open("ipyfs.png", "rb") as f:
    files.write(
        path=f"/{f.name}",
        file=f,
        create=True
    )

# Get the information of the uploaded file.
info = files.stat('/ipyfs.png')

# Generate NFT metadata.
metadata = {
    "name": "Sample NFT",
    "description": "Sample NFT Description",
    "image": f"ipfs://{info['result']['Hash']}"
}

# Upload the NFT metadata to IPFS.
files.write(
    path="/metadata.json",
    file=json.dumps(metadata),
    create=True
)
```

</div>

<details markdown="1">
<summary>Detail <code>Parameters</code>...</summary>

<br>

IPyFS is basically the same as the parameters of IPFS RPC APIs.

If you want to list the file in your `IPFS Daemon`:

* Here is the IPFS Files RPC API document: <a href="https://docs.ipfs.io/reference/kubo/rpc/#api-v0-files-ls" target="_blank">https://docs.ipfs.io/reference/kubo/rpc/#api-v0-files-ls </a>

The document needs parameters `arg` / `long` / `u`. <br>
Likewise, IPyFS can use the same parameters. (`path` / `long` / `u`) <br>
However, they are not exactly the same. In RPC, most parameter names are used as `arg`.

This is not a good way.<br>
Therefore, IPyFS has slightly changed parameter names to suit their functions.

Importantly, only the name has changed, the purpose of the parameter is the same.

```Python
from ipyfs import Files


files = Files(
    host="http://localhost",  # Set IPFS Daemon Host
    port=5001  # Set IPFS Daemon Port
)

result = files.ls(
    path="/",
    long=True
)
print(result)
```

If you want to know what each parameter is, please refer to the <a href="https://docs.ipfs.io/reference/kubo/rpc/" target="_blank">IPFS RPC API documentation.</a>

</details>


## Contributing
The following is a set of guidelines for contributing to sejong-univ-auth. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

1. Please create a branch in this format, **`<Issue Number>-<Some name>`**
2. Open a terminal and navigate to your project path. And enter this.
   **`git config --global commit.template .gitmessage.txt`**
3. You can use the template, with `git commit` through vi. **Not** `git commit -m`
4. If you want to merge your work, please pull request to the `dev` branch.
5. Enjoy contributing!

If you have any other opinions, please feel free to suggest 😀

## License

This project is licensed under the terms of the MIT license.