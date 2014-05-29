import logging
import sys

import bootcamp


def main(args=sys.argv[1:]):
    from optparse import OptionParser

    parser = OptionParser("usage: bootcamp [options] <input file>...")

    parser.add_option("-v", "--verbose", dest="verbose",
                      help="Be chatty",
                      action="store_true", default=False)

    (opts, args) = parser.parse_args(args)
    logging.root.setLevel(logging.DEBUG if opts.verbose else logging.INFO)

    if len(args) == 0:
        parser.print_help()
        return 2

    # extract the files
    for archive_file in args:
        bootcamp.Extractomatic().extract_file(archive_file)


if __name__ == '__main__':
    exit(main())
