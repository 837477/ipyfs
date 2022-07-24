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
with open("sample.png", "rb") as f:
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