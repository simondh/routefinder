from django.test import TestCase

from route_api.route_finder import find_best_path


class TestRouteFinder(TestCase):
    def test_route_finder_simple(self):
        result = find_best_path(1,2)
        self.assertEqual(result, [1,2])

    def test_route_finder_2(self):
        result = find_best_path(1,4)
        self.assertEqual(result, [1,6,4])
