__author__ = 'Sergey Ragatsky'

import string

from nose.tools import nottest, ok_, assert_equal, assert_false, assert_in
from nose.plugins.attrib import attr

from nose_ittr import IttrMultiplier, ittr


class TestMetaClassIttrMultiplayer(object):



    def setup(self):
        self.test_class_one = test_class_one()
        self.test_class_two = test_class_two()


    def teardown(self):
        pass

    @attr(id=1)
    def test_correct_mirroring(self):
        """
        Test metaclass set ittr attributes in mirrors functions
        """
        ok_(hasattr(self.test_class_one.test_method_8_val_a_val_b_val_c,
                    'attr_one'))
        ok_(hasattr(self.test_class_one.test_method_8_val_a_val_b_val_c,
                    'attr_two'))
        ok_(hasattr(self.test_class_one.test_method_8_val_a_val_b_val_c,
                    'attr_three'))

    @attr(id=2)
    def test_ittr_attribute_insertion(self):
        """
        Tests metaclass adds ittr attribute to test
        """
        assert_in('attr_one',
                  self.test_class_one.test_method_8_val_a_val_b_val_c.ittr)
        assert_in('attr_two',
                  self.test_class_one.test_method_8_val_a_val_b_val_c.ittr)
        assert_in('attr_three',
                  self.test_class_one.test_method_8_val_a_val_b_val_c.ittr)

    @attr(id=3)
    def test_self_modification_by_test_method(self):
        """
        Verifies that when mirror method ran, it modifies self
        """
        self.test_class_one.test_method_9_val_b_val_c()
        ok_(hasattr(self.test_class_one, 'attr_one'))
        ok_(hasattr(self.test_class_one, 'attr_two'))

    @attr(id=4)
    def test_mirror_methods_suffix_name_creation(self):
        """
        Check that the suffix created correctly
        """
        ok_(hasattr(self.test_class_one, 'test_method_1'))
        ok_(hasattr(self.test_class_one, 'test_method_2'))
        ok_(hasattr(self.test_class_one, 'test_method_3'))
        ok_(hasattr(self.test_class_one, 'test_method_4'))
        ok_(hasattr(self.test_class_one, 'test_method_5'))
        ok_(hasattr(self.test_class_one, 'test_method_6_val_a'))
        ok_(hasattr(self.test_class_one, 'test_method_7_val_a_val_c'))
        ok_(hasattr(self.test_class_one, 'test_method_7_val_b_val_c'))
        ok_(hasattr(self.test_class_one, 'test_method_7_val_b_val_c'))
        ok_(hasattr(self.test_class_one, 'test_method_8_val_a_val_b_val_c'))
        ok_(hasattr(self.test_class_one, 'test_method_8_val_a_val_b_val_d'))
        ok_(hasattr(self.test_class_one, 'test_method_9_val_a_val_c'))
        ok_(hasattr(self.test_class_one, 'test_method_9_val_b_val_c'))
        ok_(hasattr(self.test_class_one, 'test_method_9_val_b_val_c'))
        ok_(hasattr(self.test_class_one, 'test_method_10_val_a_val_d_val_b'))
        ok_(hasattr(self.test_class_one, 'test_method_11_val_a__'))

    @attr(id=5)
    def test_ittr_product_method_number(self):
        """
        Verify correct number of methods duplicated based on ittr
        """
        res = filter(lambda x: 'test' in x or None, dir(self.test_class_one))
        assert_equal(len(res), 21)

    @attr(id=6)
    def test_original_method_has_notest_hook(self):
        """
        Original method, that been mirrored receive no test hook
        """
        assert_false(self.test_class_one.test_method_1.__test__)
        assert_false(self.test_class_one.test_method_2.__test__)
        assert_false(self.test_class_one.test_method_3.__test__)
        assert_false(self.test_class_one.test_method_6.__test__)
        assert_false(self.test_class_one.test_method_7.__test__)
        assert_false(self.test_class_one.test_method_8.__test__)
        assert_false(self.test_class_one.test_method_9.__test__)
        assert_false(self.test_class_one.test_method_10.__test__)
        assert_false(self.test_class_one.test_method_11.__test__)

    @attr(id=7)
    def test_class_decorator(self):
        ok_(hasattr(self.test_class_two, 'test_method_1_FB'))
        ok_(hasattr(self.test_class_two, 'test_method_1_GDN'))
        ok_(hasattr(self.test_class_two, 'test_method_2_val_a_linux'))
        ok_(hasattr(self.test_class_two, 'test_method_2_val_a_mac'))
        ok_(hasattr(self.test_class_two, 'test_method_2_val_b_linux'))
        ok_(hasattr(self.test_class_two, 'test_method_2_val_b_mac'))




@nottest
class test_class_two(object):

    __metaclass__ = IttrMultiplier
    __ittr__ = {'os': ['linux', 'mac']}

    def test_method_1(self):
        """Test method docstring"""
        pass

    @ittr(ittr_val=['val_a', 'val_b'])
    def test_method_2(self):
        """Test method docstring"""
        pass

@nottest
class test_class_one(object):

    __metaclass__ = IttrMultiplier

    @ittr(attr_one=[])
    def test_method_1(self):
        """Test method docstring"""
        pass

    @ittr(attr_one=[], attr_two=[])
    def test_method_2(self):
        """Test method docstring"""
        pass

    @ittr(attr_one={})
    def test_method_3(self):
        """Test method docstring"""
        pass

    @ittr()
    def test_method_4(self):
        """Test method docstring"""
        pass

    def test_method_5(self):
        """Test method docstring"""
        pass

    @ittr(attr_one=['val_a'])
    def test_method_6(self):
        pass

    @ittr(attr_one=['val_a', 'val_b'], attr_two=['val_c'])
    @attr(id=1234, section='test')
    def test_method_7(self):
        pass

    @ittr(attr_one=['val_a'], attr_two=['val_b'])
    @ittr(attr_three=['val_c', 'val_d'])
    def test_method_8(self):
        """Test method docstring"""
        pass

    @ittr(attr_one=['val_a', 'val_b'], attr_two=['val_c'])
    @ittr(attr_one=['val_e', 'val_d'])
    def test_method_9(self):
        """Test method docstring"""
        pass

    @ittr(attr_one=['val_a'], attr_two=['val_b'])
    @ittr(attr_one=['val_c'], attr_four=['val_d'])
    def test_method_10(self):
        """Test method docstring"""
        pass

    @ittr(attr_one=['val_a'+string.punctuation])
    def test_method_11(self):
        """Test method docstring"""
        pass