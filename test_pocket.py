import unittest
import pocket
from mock import patch


class PocketTest(unittest.TestCase):

    def setUp(self):
        self.consumer_key = 'consumer_key'
        self.access_token = 'access_token'
        self.username = 'username'

    def tearDown(self):
        pass

    def test_pocket_init(self):
        pocket_instance = pocket.Pocket(
            self.consumer_key,
            self.access_token,
            self.username,
        )

        self.assertEqual(self.consumer_key, pocket_instance.consumer_key)
        self.assertEqual(self.access_token, pocket_instance.access_token)
        self.assertEqual(self.username, pocket_instance.username)

        expected_payload = {
            'consumer_key': self.consumer_key,
            'access_token': self.access_token,
        }

        self.assertEqual(expected_payload, pocket_instance._payload)

    def test_post_request(self):
        mock_payload = {
            'consumer_key': self.consumer_key,
            'access_token': self.access_token,
        }
        mock_url = 'https://getpocket.com/v3/'
        mock_headers = {
            'content-type': 'application/json',
        }

        with patch('pocket.requests') as mock_requests:
            pocket.Pocket._post_request(mock_url, mock_payload, mock_headers, pocket.Pocket.timeout)
            mock_requests.post.assert_called_once_with(
                mock_url,
                data=mock_payload,
                headers=mock_headers,
                timeout=pocket.Pocket.timeout,
            )

if __name__ == '__main__':
    unittest.main()