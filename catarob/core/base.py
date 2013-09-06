# -*- coding: iso8859-1 -*- 
'''
Created on 22 aoÃ»t 2013

@author: thomas
'''

from contextlib import contextmanager


def singleton(cls):
	instances = {}
	def get_instance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return get_instance


class _MethodDecoratorAdaptor(object):
	def __init__(self, decorator, function):
		self.decorator = decorator
		self.function = function
	def __call__(self, *args, **kwargs):
		return self.decorator(self.function)(*args, **kwargs)
	def __get__(self, instance, owner):
		return self.decorator(self.function.__get__(instance, owner))



def auto_adapt_to_methods(decorator):
	def adapt(func):
		return _MethodDecoratorAdaptor(decorator, func)
	return adapt


def typedef_control(*args, **kwargs):
	"""Check paramters' type of each input of function"""
	@auto_adapt_to_methods
	def decorator(func):
		"""Decorator return changed function"""
		def func_changed(*args_, **kwargs_):
			if(len(args) != len(args_)):
				print("Nombre d'argument de la fonction différent de celui du décorateur")
			for i, arg_ in enumerate(args_):
				if args[i] is not type(arg_):
					raise TypeError("Argument {0} n'est pas de type {1}".format(i, args[i]))
			for key in kwargs_:
				if key not in kwargs:
					raise TypeError("Argument {0} sans type".format(repr(key)))
				if kwargs[key] is not type(kwargs_[key]):
					raise TypeError("Argument {0} n'est pas de type {1}".format(repr(key), kwargs[key]))
			return func(*args_, **kwargs_)
		return func_changed
	return decorator

class AutoSlots(type):
	"""Define slot in each class (earn memory)"""
	def __new__(cls, name, bases, dct):
		slots = dct.get('__slots__', set())
		#Now get properties from properties and running_properties
		if 'properties' in dct:
			 slots.update((p for p in dct['properties']))
		if 'running_properties' in dct:
			slots.update((p for p in dct['running_properties']))
			dct['__slots__'] = tuple(slots)
		return type.__new__(cls, name, bases, dct)

""" Context Manager Method:
	with statement
"""

@contextmanager
def opened_w_error(filename, mode="r"):
	try:
		f = open(filename, mode)
	except IOError, err:
		yield None, err
	else:
		try:
			yield f, None
		finally:
			f.close()

"""
#Example
with opened_w_error("/etc/passwd", "a") as (f, err):
    if err:
	print "IOError:", err
    else:
	f.write("guido::0:0::/:/bin/sh\n")
"""


@contextmanager
def working_directory(path):
	current_dir = os.getcwd()
	os.chdir(path)
	try:
		yield
	finally:
		os.chdir(current_dir)

"""
#Example
with working_directory("data/stuff"):
    # do something within data/stuff
# here I am back again in the original working directory
"""



@contextmanager
def opened(filename, mode="r"):
	f = open(filename, mode)
	try:
		yield f
	finally:
		f.close

@contextmanager
def stdout_redirected(new_stdout):
	save_stdout = sys.stdout
	sys.stdout = new_stdout
	try:
		yield None
	finally:
		sys.stdout = save_stdout

"""
#Examples
with opened(filename, "w") as f:
	with stdout_redirected(f):
		print "Hello world"
"""
