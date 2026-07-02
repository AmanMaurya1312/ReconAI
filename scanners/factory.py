from scanners.subfinder import SubfinderScanner
from scanners.httpx import HttpxScanner
from scanners.katana import KatanaScanner
from scanners.gau import GauScanner
from scanners.nuclei import NucleiScanner


class ScannerFactory:
    """
    Returns the list of available scanners.
    """

    @staticmethod
    def get_scanners():

        return [
            SubfinderScanner,
	        HttpxScanner,
            KatanaScanner,
            GauScanner,
            NucleiScanner,
            
        ]
