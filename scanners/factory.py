from scanners.subfinder import SubfinderScanner
from scanners.httpx import HttpxScanner
from scanners.katana import KatanaScanner
from scanners.gau import GauScanner


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
            
        ]
