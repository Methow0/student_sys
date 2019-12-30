from django.test import TestCase,Client

from .models import Student
class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            eamil='nobody@the5fire.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        self.assertEqual(student.sex_show,'男','性别字段内容和展示的不一样!')

    def test_filter(self):
        Student.objects.create(
          name='huyang',
          sex='1',
          email='nobody@dd.com',
          profession='程序员',
          qq='3333',
          phone='32222',
        )
        name='the5fire'
        students =Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,
                         '应该只存在一个名称{}的记录'.format(name))
