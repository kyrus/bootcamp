import logging


class Extractomatic(object):
    """
    The Extract-o-matic extracts files from a bunch of types of archives and puts
    those files in a temporary directory
    """

    def extract_files(self, archive):
        """
        Extracts files from the given archive
        """
        logging.info('Extracting [%s]', archive)
