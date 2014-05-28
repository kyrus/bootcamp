import zipfile
import tempfile

class ZipExtractor(object):

    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_directory']

    def process(self, input):
        zipFile = zipfile.ZipFile(input['filename'])
        if not zipFile.is_zipfile():
        	raise TypeError('File is not a zip file')
        tmpDir = tempfile.mkdtemp(prefix='tmp',suffix='unzip')
        if input['password'] is not None:
        	zipFile.extractall(tmpDir,pwd=input['password'])
        else:
        	zipFile.extractall(tmpDir)
        return {'extracted_files_directory':tmpDir}