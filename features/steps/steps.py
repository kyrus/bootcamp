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

@given(u'the file is a "zip"')
def step_impl(context):
    assert False

@when(u'given to an "zip_extractor"')
def step_impl(context):
    assert False

@then(u'the file should be "directory with unzipped archive file"')
def step_impl(context):
    assert False

@given(u'the file is a "gpg"')
def step_impl(context):
    assert False

@then(u'the file should be "exception"')
def step_impl(context):
    assert False

@given(u'the file is a "gzip"')
def step_impl(context):
    assert False

@when(u'given to an "gzip_extractor"')
def step_impl(context):
    assert False