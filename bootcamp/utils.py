import os
import shutil
import errno
import logging
import subprocess
from contextlib import contextmanager

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def rmdir_mkdir(dirname):
    '''Removes a directory then recreates it'''
    if os.path.exists(dirname):
        shutil.rmtree(dirname, True)
    mkdir_p(dirname)


def remove_empty_dirs(path):
    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                remove_empty_dirs(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0:
        os.rmdir(path)


def copytree(src, dst, symlinks=False, ignore=None, overwrite=False):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if not ignore or not item in ignore:
            if os.path.isdir(s):
                copytree(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or (overwrite and os.stat(src).st_mtime - os.stat(dst).st_mtime > 1):
                    print "copying in file: %s" % s
                    shutil.copy2(s, d)
                else:
                    print "not doing file overwrite: %s" % s
        else:
            logging.debug("Ignoring copying item: %s" % s)

# the current directory for all local() commands
lcd_directory = None


@contextmanager
def lcd(dir):
    """
    Context manager that causes all local() commands to run in the given directory.

    Intended to be a close-enough dropin replacement for Fabric's lcd() command.
    """
    global lcd_directory
    lcd_directory = os.path.abspath(dir)
    yield
    lcd_directory = os.getcwd()


def local(command):
    """
    Runs a shell command locally.

    Intended to be a close-enough dropin replacement for Fabric's local() command.
    """
    # save the current dir
    original_directory = os.getcwd()

    # switch to wherever the lcd context manager tells us to be
    logging.debug("Changing directory to [%s]" % lcd_directory)
    os.chdir(lcd_directory)
    try:
        # run the command
        logger = logging.getLogger("exec")
        logger.debug("Running: [%s]" % command)
        output = []
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        for line in iter(p.stdout.readline, ""):
            output.append(line.rstrip())
            logger.debug(line.rstrip())

        p.communicate()
        if p.returncode != 0:
            logging.error(output)
            raise Exception("Return code was non-zero for command [%s]" % command)
        return output
    finally:
        # go back to the old directory
        logging.debug("Changing directory back to [%s]" % original_directory)
        os.chdir(original_directory)


def list_all_files(directory):
    return [os.path.join(root, filename) for root, dirnames, filenames in os.walk(directory) for filename in filenames]


def replace_in_file(filename, values):
    original_lines = open(filename, 'rt').readlines()
    with open(filename, "wt") as f:
        for line in original_lines:
            newline = line
            for key, value in values.iteritems():
                newline = newline.replace(key, value)
            f.write(newline)


def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise