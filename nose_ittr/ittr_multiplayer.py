__author__ = 'Sergey Ragatsky'
__version__ = '0.0.1'

import re
import logging
from types import FunctionType
from itertools import product

logger = logging.getLogger(__name__)


def ittr(*args, **kwargs):
    """
    Decorator that adds iteration attributes to test method
    """
    def update_attr(func):
        # combining kwargs and args dict with ittr dict
        ittrs = {str(item): item for item in args or []}
        ittr_dict = getattr(func, 'ittr', dict())
        ittr_dict.update(ittrs)
        ittr_dict.update(kwargs)
        setattr(func, 'ittr', ittr_dict)

        return func
    return update_attr


class IttrMultiplayer(type):
    """
    Multiples the tests in a given test class by
    the parameters given in ittr decorator.
    """
    def __new__(mcs, name, bases, dct):

        for attribute_name, attribute in dct.items():
            # if not a method continue
            if not type(attribute) == FunctionType:
                logging.debug('attribute {0} is not a method'.format(attribute_name))
                continue

            # is method decorated with platform attr
            if not hasattr(attribute, 'ittr') or not attribute.ittr:
                logging.debug('method {0} has not attr decorator'.format(attribute_name))
                continue

            # create product of all the iterators
            b = [map(lambda value: (key, value), values)
                 for key, values in attribute.ittr.iteritems() if values]
            products = map(dict, product(*b))

            for prod in products:
                logging.debug('method product: {0}'.format(prod))
                suffix = re.sub(r'\W+', '',
                                str(prod.values())
                                .translate(None, "[]'")
                                .replace(',', '_'))
                logging.debug('method suffix: {0}'.format(suffix))

                # in case itts passed are empty
                if not suffix:
                    logging.debug('Empty suffix, product: {0}'.format(prod))
                    continue
                new_func_name = attribute_name + '_' + suffix

                # combine both product and ittr dict to be added to new method
                func_params = dict(attribute.func_dict, **prod)
                mirror_func = mcs._attribute_injector(attribute, **func_params)
                setattr(mirror_func, 'ittr', prod)

                # assign new name and docstring and save back at our class
                mirror_func.func_name = new_func_name
                mirror_func.func_doc = attribute.func_doc
                dct[new_func_name] = mirror_func

            # set no test flag to original test method
            attribute.__test__ = False
        return type.__new__(mcs, name, bases, dct)

    @classmethod
    def _attribute_injector(cls, func, **keywords):
        def injector(*fargs, **fkeywords):
            # transfer ittr and attr to self when called
            self = fargs[0]
            for name, value in keywords.iteritems():
                setattr(self, name, value)
            return func(*fargs, **fkeywords)

        # transfers all attr and ittr to newfunc
        for name, value in keywords.iteritems():
            setattr(injector, name, value)
        setattr(injector, 'keywords', keywords)
        return injector
