import logging
import os
import zip_extractor
import GzipExtractor
import rar_extractor
import tar_extractor
import file_counter

from utils import *

THIS_DIR = os.path.realpath(os.path.dirname(__file__))


class Extractomatic(object):
    """
    The Extract-o-matic extracts files from a bunch of types of archives and puts
    those files in a temporary directory
    """

    def extract_file(self, archive, password=None):
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
        if password is not None:
            proc_input['password'] = password

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
        proc = None
        if file_type == 'Zip archive data':
            logging.info('Unarchiving as a [%s] file', file_type)
            proc = zip_extractor.ZipExtractor()
        elif file_type == 'gzip compressed data':
            logging.info('Unarchiving as a [%s] file', file_type)
            proc = GzipExtractor.GzipExtractor()
        elif file_type == 'POSIX tar archive':
            logging.info('Unarchiving as a [%s] file', file_type)
            proc = tar_extractor.TarExtractor()
        elif file_type == 'data' and extension == '.gpg':
            logging.info('Unarchiving as a GPG file')
            # proc = GPGExtractor.GPGExtractor()
        elif file_type == 'RAR archive data':
            logging.info('Unarchiving as a [%s] file', file_type)
            proc = rar_extractor.RARFile()
        elif file_type == '7-zip archive data':
            logging.info('Unarchiving as a [%s] file', file_type)
            # proc = seven_zip_extractor.SevenZipExtractor()
        else:
            logging.error('Error: unknown/unsupported file type of [%s]', file_type)
            return

        proc_output = proc.process(proc_input)

        logging.info('Extracted files are in [%s]', proc_output['extracted_files_directory'])
        file_proc_output = file_counter.FileCounter().process(proc_output)

        logging.info('Extracted %s files and %s directories', file_proc_output['extracted_file_count'],
                     file_proc_output['extracted_subdirectory_count'])
