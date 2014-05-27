from behave import *

step_matcher('re')


@when("I execute (?P<binary>.*) with the command (?P<options>.*)")
def when_command(context, binary, options):
    # TODO: implement
    pass
