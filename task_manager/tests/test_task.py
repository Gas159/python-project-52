from django.test import TestCase
from django.urls import reverse
from users.models import Users
from statuses.models import Status
# from labels.models import Labels


# Create your tests here.
class CRUD_Tasks_Test(TestCase):

    def setUp(self):
        Users.objects.create(
            first_name='Alexey',
            last_name='Navalny',
            username='FBK',
            email='root@fbk.ru',
            password='iloveputin'
        )
        self.user = Users.objects.get(id=1)

        Status.objects.create(name='status1')
        self.status = Status.objects.get(id=1)

        # Labels.objects.create(name='label1')
        # self.label = Labels.objects.get(id=1)

        # Tasks.objects.create(name='status1')

    # Адреса которые нужно проверить
    url_tasks = [
        reverse('tasks'),
        reverse('create_task'),
        reverse('task', kwargs={'pk': 1}),
        reverse('update_task', kwargs={'pk': 1}),
        reverse('delete_task', kwargs={'pk': 1}),
    ]

    # Проверка доступа незалогененым пользователям
    def test_access(self, urls=url_tasks):
        for u in urls:
            resp = self.client.get(u)
            self.assertEqual(resp.status_code, 302)

        # self.client.force_login(self.user)
        # for u2 in urls:
        #     resp = self.client.get(u2)
        #     self.assertEqual(resp.status_code, 200)