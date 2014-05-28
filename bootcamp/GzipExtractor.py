import gzip
import tempfile


class GzipExtractor:
    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_directory']

    def process(self, input):
        filename = input['filename']
        f = gzip.open(filename, 'rb')
        file_content = f.read()
        d = tempfile.mkdtemp()
        t = open(d + "/extracteddata", "w+")
        t.write(file_content)
        return {'extracted_files_directory': d}
