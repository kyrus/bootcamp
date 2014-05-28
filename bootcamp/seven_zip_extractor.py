__author__ = 'davidzilz'

import subprocess
import tempfile

class SevenZipExtractor(object):

    def requires(self):
        return ['archive-file']

    def produces(self):
        return ['extracted_files_directory']

    def process(self,input):
        path = input['filename']
        tmpDir = tempfile.mkdtemp(prefix='tmp',suffix='un7zip')
        subprocess.check_call(['cp',path,tmpDir])
        subprocess.check_call(['7za', 'x', path])
        return {'extracted_files_directory':tmpDir}