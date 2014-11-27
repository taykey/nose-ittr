__author__ = 'Sergey'


from nose.plugins import Plugin


class SetupIttr(Plugin):
    """
    This plugin enables you to pass ittr attributes to setup, for
    customizing setup for each test.
    """

    name = 'setup-ittr'

    def beforeTest(self, test):
        try:
            if hasattr(test.test.__dict__['test'], 'ittr'):
                for key, value in test.test.__dict__['test'].ittr.iteritems():
                    setattr(test.context, key, value)
        except KeyError:
            return

    def afterTest(self, test):
        try:
            if hasattr(test.test.__dict__['test'], 'ittr'):
                for key, value in test.test.__dict__['test'].ittr.iteritems():
                    delattr(test.context, key)
        except KeyError:
            return