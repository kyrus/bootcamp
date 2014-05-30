import os
import bootcamp

from behave import *

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


@when(u'I determine the extractor to use on the file')
def determine_extractor(context):
    context.extractor = bootcamp.Extractomatic().get_extractor(os.path.realpath(context.current_file))
    print 'Extractor being used: %s' % type(context.extractor)


@when(u'I run the extractor "(?P<extractor_type>.*)"')
def run_extractor(context, extractor_type):
    extractor = get_extractor_by_type(extractor_type)

    context.extraction_result = extractor.process({'filename': context.current_file})
    print context.extraction_result


@then(u'I should be using the "(?P<extractor_type>.*)" extractor')
def expect_extractor(context, extractor_type):
    extractor = get_extractor_by_type(extractor_type)

    print 'Expected extractor: %s' % type(extractor)
    assert type(context.extractor) is type(extractor)


@then(u'I should get a directory that contains the contents of the archive')
def expect_directory(context):
    assert 'extracted_files_directory' in context.extraction_result
    assert os.path.isdir(context.extraction_result['extracted_files_directory'])
    assert os.path.isfile(os.path.join(context.extraction_result['extracted_files_directory'], 'testfile.txt'))


def get_extractor_by_type(extractor_type):
    if extractor_type == 'Zip':
        extractor = bootcamp.zip_extractor.ZipExtractor()
    elif extractor_type == 'Gzip':
        extractor = bootcamp.GzipExtractor.GzipExtractor()
    elif extractor_type == '7zip':
        extractor = bootcamp.seven_zip_extractor.SevenZipExtractor()
    elif extractor_type == 'Tar':
        extractor = bootcamp.tar_extractor.TarExtractor()
    elif extractor_type == 'Rar':
        extractor = bootcamp.rar_extractor.RARFile()
    else:
        raise Exception('Unknown extractor type')

    return extractor
