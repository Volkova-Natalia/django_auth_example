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

    def execute(self, client=None):
        client, response = self.get(client=client)
        self._test_get(response, success_fail='success', assert_message='integration')

        client, response = self.post(client=client)
        self._test_post(response, success_fail='success', assert_message='integration')

        return client

    # ======================================================================

    def test(self):
        assert_message = 'integration logout'
        pass
        # TODO

    # ======================================================================
