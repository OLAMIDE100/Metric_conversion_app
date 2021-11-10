from django.test import SimpleTestCase,TestCase
from django.urls import reverse

# Create your tests here.



class ConvTest(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('')

    def test_conv_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_conv_template(self):
        self.assertTemplateUsed(self.response, 'base.html')

    def test_conv_contains_correct_html(self):
        self.assertContains(self.response, 'CONVERSION')

class ConvTempTest(TestCase):

    def setUp(self):
        self.url = reverse('temp')
        self.post_dict = {'Value':50, 'Units':'Fahrenheit ==> Celsius'}

        self.response = self.client.post(self.url, self.post_dict)

    def test_convtemp_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_convtemp_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_convtemp_response(self):

        self.assertEqual(self.response.status_code, 200)


    def test_ConvTemp_no_value_response(self):

        post_dict = {'Value':'', 'Units':'Fahrenheit ==> Celsius'}

        response = self.client.post(self.url, post_dict)

        self.assertEqual(response.status_code, 200)

class ConvTimeTest(TestCase):

    def setUp(self):
        self.url = reverse('time')
        self.post_dict = {'Value':50, 'Units':'seconds ==> minutes'}

        self.response = self.client.post(self.url, self.post_dict)

    def test_convtime_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_convtime_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_convtime_response(self):

        self.assertEqual(self.response.status_code, 200)


    def test_ConvTime_no_value_response(self):

        post_dict = {'Value':'', 'Units':'seconds ==> minutes'}

        response = self.client.post(self.url, post_dict)

        self.assertEqual(response.status_code, 200)




