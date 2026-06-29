from scanners.subfinder import SubfinderScanner
from scanners.httpx import HttpxScanner

class ScannerFactory:
    """
    Returns the list of available scanners.
    """

    @staticmethod
    def get_scanners():

        return [
            SubfinderScanner,
	    HttpxScanner,
        ]
