__author__ = 'ferronhanse'

import unittest

from bs4 import BeautifulSoup

import social_sharing


class SocialSharingTestCase(unittest.TestCase):
    def setUp(self):
        social_sharing.app.config['TESTING'] = True
        self.app = social_sharing.app.test_client()

    def tearDown(self):
        """nothing here"""

    def test_load_metadata_via_content(self):
        """loading meta_data via the /content/<content> route"""
        content = 'This is just a simple unit test'
        rv = self.app.get('/content/{0}'.format(content))
        soup = BeautifulSoup(rv.data)
        assert soup.find_all(attrs={'property': 'og:description'})[0]['content'] == content

    def test_load_meta_via_content_title(self):
        """loading meta_data via the /content/<content>/title/<title> route"""
        content = 'This is just a simple unit test'
        title = 'DEVELOPER TEST'
        rv = self.app.get('/content/{0}/title/{1}'.format(content, title))
        soup = BeautifulSoup(rv.data)
        assert soup.meta['content'] == title

    def test_load_meta_via_content_image(self):
        """loading meta_data via the /content/<content>/image/<image> route"""
        content = 'This is just a simple unit test'
        title = 'CarePass'
        image = 'https://developer.carepass.com/files/carepass-icon.png'
        rv = self.app.get('/content/{0}/image/{1}'.format(content, image))
        soup = BeautifulSoup(rv.data)
        assert soup.meta['content'] == title
        assert soup.find_all(attrs={'property': 'og:image'})[0]['content'] == image

    def test_load_meta_via_content_image_title(self):
        """loading meta_data via the /content/<content>/image/<image>/title/<title> route"""
        content = 'This is just a simple unit test'
        title = 'DEVELOPER_TEST'
        image = 'https://developer.carepass.com/files/carepass-icon.png'
        rv = self.app.get('/content/{0}/image/{1}/title/{2}'.format(content, image, title))
        soup = BeautifulSoup(rv.data)
        assert soup.meta['content'] == title
        assert soup.find_all(attrs={'property': 'og:image'})[0]['content'] == image
        assert soup.find_all(attrs={'property': 'og:description'})[0]['content'] == content


if __name__ == '__main__':
    unittest.main()