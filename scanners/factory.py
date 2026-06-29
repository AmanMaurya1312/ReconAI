from scanners.subfinder import SubfinderScanner


class ScannerFactory:
    """
    Returns the list of available scanners.
    """

    @staticmethod
    def get_scanners():

        return [
            SubfinderScanner,
        ]
