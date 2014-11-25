nose-ittr
=========
nose extension for supporting parametrized testing.
---------------------------------------------------
Allow developer to run the same test over and over again using different values.

Main Features:
 * Very easy to integrate with existing tests.
 * Saves a lot of boilerplate code, and code replication.
 * Work with all nose plugins (including multiprocessing).

Installation:
-------------

.. code-block:: shell

    pip install nose_ittr

Basic usage:
------------

.. code-block:: python

    from nose.tools import assert_equal
    from nose_ittr import IttrMultiplayer, ittr

    class TestFoo(object):
        
        __metaclass__ = IttrMultiplayer
        
        def setup(self):
            pass
        
        def teardown(self):
            pass
            
        @ittr(number=[1, 2, 3, 4])
        def test_even(self):
            assert_equal(self.number % 2, 0)
            
        
        @ittr(numerator=[15, 6], denominator=[2, 3])
        def test_no_remainder(self):
                assert_equal(self.numerator % self.denominator, 0)
                
result:
                   
.. code-block:: shell

        TestFoo.test_even_1 ... FAIL
        TestFoo.test_even_2 ... .ok
        TestFoo.test_even_3 ... FAIL
        TestFoo.test_even_4 ... .ok
        TestFoo.test_no_remainder_2_6 ... .ok
        TestFoo.test_no_remainder_2_15 ... FAIL
        TestFoo.test_no_remainder_3_6 ... .ok
        TestFoo.test_no_remainder_3_15 ... .ok


**notes:**
 * Doesn't affect setup.
 * Doesn't affect test docstring if used with -v parameter.

To change the docstring printout based on the varibales passed to test, use the plugin 
`nose-docstring-modifier <https://pypi.python.org/pypi/nose-docstring-modifier/>`_.

:Authors:
    Sergey Ragatsky 
:Contributors: 
    Tal Ben Basat
  
    Nicole Franco  

    Roy Klinger 
 
    Maroun Maroun  
:Version: 1.0 of 25/11/2014 
