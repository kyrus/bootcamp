import zipfile
import tempfile

class ZipExtractor(object):

    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_directory']

    def process(self, input):
        zipFile = zipfile.ZipFile(input['filename'])
        tmpDir = tempfile.mkdtemp(prefix='tmp',suffix='unzip')
        zipFile.extractall(tmpDir)
        return {'extracted_files_directory':tmpDir}