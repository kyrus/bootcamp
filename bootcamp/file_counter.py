import os

class FileCounter(object):

    def requires(self):
        return ['extracted_files_directory']

    def produces(self):
        return ['extracted_file_count', 'extracted_subdirectory_count']
        
    def process(self, input):
        # The most obscure way I could think to do this.
        (dir_count, file_count) = map(sum,zip(*map(lambda t: map(len,t[1:3]),os.walk(input['extracted_files_directory']))))
        
        return {
            'extracted_subdirectory_count': dir_count,
            'extracted_file_count': file_count,
            }
