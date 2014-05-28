import os

from behave import *

import bootcamp
import bootcamp.zip_extractor


use_step_matcher('re')


@when(u'I run the Extract-O-Matic with the args "(?P<args>.*)"')
def step_impl(context, args):
    # TODO: implement
    assert False


@then(u'I should see a usage message')
def step_impl(context):
    # TODO: implement
    assert False


@given(u'I have a file of type "(?P<file_type>.*)"')
def have_file_type(context, file_type):
    context.current_file = "testfiles/test1.%s" % file_type
    assert os.path.isfile(context.current_file)


@when(u'I run the extractor "(?P<extractor_type>.*)"')
def run_extractor(context, extractor_type):
    if extractor_type == 'Zip':
        extractor = bootcamp.zip_extractor.ZipExtractor()
    elif extractor_type == 'Gzip':
        extractor = bootcamp.GzipExtractor.GzipExtractor()
    else:
        raise Exception('Unknown extractor type')

    context.extraction_result = extractor.process({'filename': context.current_file})


@then(u'I should get a directory that contains the contents of the archive')
def expect_directory(context):
    assert 'extracted_files_directory' in context.extraction_result
    assert os.path.isdir(context.extraction_result['extracted_files_directory'])
    assert os.path.isfile(os.path.join(context.extraction_result['extracted_files_directory'], 'testfile.txt'))


