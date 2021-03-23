from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Outfits

class ClosetTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        lazyuser1 = get_user_model().objects.create_user(username='lazyuser1', password='pass')
        lazyuser1.save()

        test_post = Outfits.objects.create(
            outfit_wearer = lazyuser1,
            outfit_name = 'Sleepy Sunday',
            top = 'Hoodie',
            bottom = 'Joggers',
            shoes = 'Slippers',
        )
        test_post.save()

    def test_closet_content(self):
        post = Outfits.objects.get(id=1)
        actual_outfit_wearer = str(post.outfit_wearer)
        actual_outfit_name = str(post.outfit_name)
        actual_top = str(post.top)
        actual_bottom = str(post.bottom)
        actual_shoes = str(post.shoes)

        self.assertEqual(actual_outfit_wearer, 'lazyuser1')
        self.assertEqual(actual_outfit_name, 'Sleepy Sunday')
        self.assertEqual(actual_top, 'Hoodie')
        self.assertEqual(actual_bottom, 'Joggers')
        self.assertEqual(actual_shoes, 'Slippers')
