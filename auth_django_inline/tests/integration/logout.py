from ..views.base.logout import BaseLogoutTestCase


# Create your tests here.
class IntegrationLogoutTestCase(BaseLogoutTestCase):

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def execute(self):
        response = self.get()
        self._test_get(response, success_fail='success', assert_message='integration')

        response = self.post()
        self._test_post(response, success_fail='success', assert_message='integration')

    # ======================================================================

    def test(self):
        assert_message = 'integration logout'
        pass
        # TODO

    # ======================================================================
