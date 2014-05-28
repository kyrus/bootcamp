import logging
import os
import zip_extractor

from utils import *

THIS_DIR = os.path.realpath(os.path.dirname(__file__))


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

        fullpath = os.path.realpath(archive)

        if not os.path.exists(fullpath):
            logging.error('Could not find [%s]', archive)
            return

        proc_input = {}
        proc_input['filename'] = fullpath

        name, extension = os.path.splitext(fullpath)

        logging.info('Extracting [%s] with extension [%s]', archive, extension)

        output = ''
        with lcd(THIS_DIR):
            output = local('file %s' % fullpath)
            logging.debug('file command output: %s', output)

        # Output will look similar to this:
        # /Users/jfawcett/git/apk-sploder/apks/fmlife.activities.apk: Zip archive data, at least v2.0 to extract
        file_output = '\\n'.join(output).split(fullpath)[1][2:]

        # file_output should now look like this:
        # Zip archive data, at least v2.0 to extract
        logging.debug('file command split output: %s', file_output)

        file_type = file_output.split(',')[0]

        logging.debug('file type: %s', file_type)

        proc_output = {}
        if file_type == 'Zip archive data':
            logging.info('Unarchiving as a [%s] file', file_type)
            proc_output = zip_extractor.ZipExtractor().process(proc_input)
        elif file_type == 'gzip compressed data':
            logging.info('Unarchiving as a [%s] file', file_type)
            # proc_output = gzip_extractor.gzip_extractor().process(proc_input)
        elif file_type == 'POSIX tar archive':
            logging.info('Unarchiving as a [%s] file', file_type)
            # proc_output = zip_extractor.ZipExtractor().process(proc_input)
        elif file_type == 'gpg':
            logging.info('Unarchiving as a [%s] file', file_type)
            # proc_output = GPGExtractor.GPGExtractor().process(proc_input)
        elif file_type == 'RAR archive data':
            logging.info('Unarchiving as a [%s] file', file_type)
            # proc_output = zip_extractor.ZipExtractor().process(proc_input)
        elif file_type == '7-zip archive data':
            logging.info('Unarchiving as a [%s] file', file_type)
            # proc_output = zip_extractor.ZipExtractor().process(proc_input)
        else:
            logging.error('Error: unknown/unsupported file type of [%s]', file_type)
            return

        logging.info('Extracted files are in [%s]', proc_output['extracted_files_directory'])