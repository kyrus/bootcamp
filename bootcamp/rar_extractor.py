import rarfile
import os

class RARFile(object):

    def requires(self):
        return ['filename']

    def produces(self):
        return ['extracted_files_directory']

    #return the directory where files are extracted to
    def process(self, input):
        rarfile.UNRAR_TOOL = "unrar"
        rarfile.PATH_SEP = '\\'

        extract_path = "~/tempExtraction"
        file = input['filename']

        os.mkdir(extract_path, None)

        rf = rarfile.RarFile(file)
        rf.extractall(self, extract_path, None, None)


        return {
            'extracted_files_directory' : extract_path
        }

