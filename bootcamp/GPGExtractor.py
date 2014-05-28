import tempfile
from subprocess import call
import os

__author__ = 'devin'
GPGBINARY = os.environ.get('GPGBINARY', 'gpg')
if not os.path.exists(GPGBINARY):
    GPGBINARY = "/usr/local/bin/gpg"


class GPGExtractor(object):

    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_dir']

    def process(self, input):
        filename = input['filename']
        out_filename = os.path.splitext(filename)[0]

        extracted_files_dir = tempfile.mkdtemp()

        call([GPGBINARY, '-d', filename, '-o', os.path.join(extracted_files_dir,out_filename)])

        return {'extracted_files_dir': extracted_files_dir}