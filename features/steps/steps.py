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
