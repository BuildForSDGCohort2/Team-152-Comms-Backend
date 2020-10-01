
from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.template.loader import render_to_string


class WelcomeMessageTests(TestCase):

    async def test_no_to_value(self):
        """If no 'to' value is provided, an appropriate
        message is returned.
        """
        request_body = {
            'to': '',
            'data': {}
        }

        response = await self.client.post(reverse('dispatcher:welcome_message'), request_body)
        self.assertEqual(response.status_code, 400)

class EmailTest(TestCase):
    def test_send_welcome_email(self):

        request_body = {
            'to': 'empty@email.address',
            'data': {
                'name': 'Person\'s name'
            }
        }

        mail.send_mail(
            'SkillCafe Communication',
            render_to_string('welcome_message.txt', context=request_body),
            'SkillCafe Communication',
            [request_body.get('to')],
            fail_silently=False
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'SkillCafe Communication')
    
class RequestDataTestCase(TestCase):
    """TestCase confirms that the application receives ot
    rejects data based on their types and requirement.
    """

    def test_to_variable_present(self):

        pass

    async def test_to_variable_absent(self):
        """If no 'to' value is provided, an appropriate
        message is returned.
        """
        request_body = {
            'to': '',
            'data': {}
        }

        response = await self.client.post(reverse('dispatcher:welcome_message'), request_body)
        print(response.data, response.status_code)
        self.assertEqual(response.status_code, 400)

    async def test_to_variable_wrong_data_type(self):
        
        request_body = {
            'to': 'string@email',
            'data': {}
        }

        response = await self.client.post(reverse('dispatcher:welcome_message'), request_body)
        self.assertEqual(response.status_code, 400)


