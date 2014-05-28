import zipfile
import tempfile

class ZipExtractor(object):

    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_directory']

    def process(self, input):
    	if not zipfile.is_zipfile(input['filename']):
        	raise TypeError('File is not a zip file')
        zipFile = zipfile.ZipFile(input['filename'])
        tmpDir = tempfile.mkdtemp(prefix='tmp',suffix='unzip')
        if 'password' in input:
        	zipFile.extractall(tmpDir,pwd=input['password'])
        else:
        	zipFile.extractall(tmpDir)
        return {'extracted_files_directory':tmpDir}