
"""
Example of NFT Metadata Upload
"""
from ipyfs import Files
from time import sleep
from tqdm import tqdm

import json
import os
import re


class NFTMetadataUploader:
    def __init__(
            self,
            host: str,
            port: int,
            metadata_folder: str,
            images_folder: str,
            ipfs_folder: str,
            network_interval_seconds: float):

        self.files = Files(host, port)
        self.ipfs_folder = ipfs_folder
        self.metadata_folder = metadata_folder
        self.images_folder = images_folder
        self.ipfs_metadata_folder = os.path.join(ipfs_folder, 
                                                        metadata_folder)
        self.ipfs_images_folder = os.path.join(ipfs_folder, images_folder)
        self.network_interval_seconds = network_interval_seconds

    def check_folders(self):
        """
        Checks if folders exist and creates them if they don't
        """
        try:
            self.files.stat(f'/{self.ipfs_folder}')
        except Exception as e:
            if e.args[0]['Code'] == 0:
                print('IPFS({}) Folder does not exist. Creating...'.format(
                                                        self.ipfs_folder))
                self.files.mkdir(f'/{self.ipfs_folder}')

        try:
            self.files.stat(f'/{self.ipfs_images_folder}')
        except Exception as e:
            if e.args[0]['Code'] == 0:
                print('Image folder does not exist. Creating...')
                self.files.mkdir(f'/{self.ipfs_images_folder}')

        try:
            self.files.stat(f'/{self.ipfs_metadata_folder}')
        except Exception as e:
            if e.args[0]['Code'] == 0:
                print('Metadata folder does not exist. Creating...')
                self.files.mkdir(f'/{self.ipfs_metadata_folder}')

    def get_all_metadata(self) -> list:
        """
        Returns all metadata files in the metadata folder
        """
        return sorted([x for x in
                       os.listdir(self.metadata_folder) if ".json" in x])

    def get_images(self) -> dict:
        """
        Returns all images in the images folder
        """
        return {x.split('.')[0]: x
                for x in os.listdir(self.images_folder) if '.' in x}

    def upload(self, create=True):
        """
        Uploads all metadata and images to IPFS
        """
        all_metadata = self.get_all_metadata()
        images = self.get_images()
        for metadata_file in tqdm(all_metadata):
            with open(os.path.join(
                    self.metadata_folder, metadata_file), "r") as f_meta:
                # Upload image to IPFS
                count_str = re.findall(r'(\d+)', metadata_file)[0]
                image_name = images[count_str]
                image_path = os.path.join(self.images_folder, image_name)
                with open(image_path, "rb") as f_image:
                    ipfs_f_image_path = os.path.join(
                        self.ipfs_images_folder, image_name)
                    self.files.write(
                        path=f"/{ipfs_f_image_path}",
                        file=f_image,
                        create=create
                    )
                sleep(self.network_interval_seconds)
                info = self.files.stat(f'/{ipfs_f_image_path}')

                # Upload metadata to IPFS
                metadata = json.load(f_meta)
                metadata['name'] = metadata['name'].format(
                    count=int(count_str))
                metadata['image'] = metadata['image'].format(
                    image_hash=info['result']['Hash'])
                ipfs_f_meta_path = os.path.join(
                    self.ipfs_metadata_folder, metadata_file)
                self.files.write(
                    path=f"/{ipfs_f_meta_path}",
                    file=json.dumps(metadata),
                    create=True
                )
                sleep(self.network_interval_seconds)


if __name__ == "__main__":
    nftmu = NFTMetadataUploader(
        host="http://localhost",
        port=5001,
        metadata_folder="metadata",
        images_folder="images",
        ipfs_folder="test01",
        network_interval_seconds=0.03)

    nftmu.check_folders()
    nftmu.upload()
    print("Done")
