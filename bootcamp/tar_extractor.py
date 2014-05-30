__author__ = 'taylormattison'

import tempfile
import subprocess


class TarExtractor(object):

    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_directory']

    def process(self, input):
        inFileLocation = input['filename']
        temporaryDirectory = tempfile.mkdtemp()

        subprocess.call(['tar', '-xf', inFileLocation, '-C', temporaryDirectory])
        return {
            'extracted_files_directory': temporaryDirectory
        }