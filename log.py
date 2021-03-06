from datetime import datetime
from threading import RLock
import sys
import traceback

quiet = False
verbose = False
server = ''
lock = RLock()

TIME_FORMAT = '%d/%m/%Y %H:%M:%S'

def say(format_, args=(), say_quiet=False):
	if quiet and not say_quiet: return
	with lock:
		p = format_ % args
		if verbose:
			print('%s %s,' % (server, datetime.now().strftime(TIME_FORMAT)), p)
		else:
			sys.stdout.write('\r%s\r%s %s' % (' '*80, server, p))
		sys.stdout.flush()

def say_line(format_, args=()):
	if not verbose:
		format_ = '%s, %s\n' % (datetime.now().strftime(TIME_FORMAT), format_)
	say(format_, args)

def say_exception(message=''):
	type_, value, tb = sys.exc_info()
	say_line(message + ' %s', str(value))
	if verbose:
		traceback.print_exception(type_, value, tb)

def say_quiet(format_, args=()):
	say(format_, args, True)
