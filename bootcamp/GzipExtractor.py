import gzip
import tempfile
import subprocess

class GzipExtractor(object):
    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_directory']

    def process(self, input):
        filename = input['filename']

        file_info = subprocess.check_output(['file', filename])
        original_name = file_info.split('"')[1]

        f = gzip.open(filename, 'rb')
        file_content = f.read()
        d = tempfile.mkdtemp()
        t = open(d + "/" + original_name, "w+")
        t.write(file_content)
        t.close()
        return {'extracted_files_directory': d}
