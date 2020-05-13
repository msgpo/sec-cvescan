import bz2
from cvescan.errors import BZ2Error, DownloadError
import pycurl

def download(download_url, filename):
    try:
        with open(filename, "wb") as target_file:
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, download_url)
            curl.setopt(pycurl.WRITEDATA, target_file)
            curl.perform()
            curl.close()
    except Exception as ex:
        raise DownloadError("Downloading %s failed: %s" % (download_url, ex))

def bz2decompress(bz2_archive, target):
    try:
        with open(bz2_archive, "rb") as archive:
            with open(target, "wb") as target:
                target.write(bz2.decompress(archive.read()))
    except Exception as ex:
        raise BZ2Error("Decompressing %s to %s failed: %s", (bz2_archive, target, ex))