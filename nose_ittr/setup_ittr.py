__author__ = 'Sergey'


from nose.plugins import Plugin


class SetupIttr(Plugin):
    """
    This plugin enables you to pass ittr attributes to setup, for
    customizing setup for each test.
    """

    name = 'setup-ittr'

    def beforeTest(self, test):
        if hasattr(test.test.__dict__['test'], 'ittr'):
            for key, value in test.test.__dict__['test'].ittr.iteritems():
                setattr(test.context, key, value)

    def afterTest(self, test):
        if hasattr(test.test.__dict__['test'], 'ittr'):
            for key, value in test.test.__dict__['test'].ittr.iteritems():
                delattr(test.context, key)
