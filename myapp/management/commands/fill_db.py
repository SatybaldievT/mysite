from django.core.management.base import BaseCommand
from myapp.models import Tag, UserProfile, Question, Answer
from faker import Faker

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='....')
    def handle(self, *args, **kwargs):
        fake = Faker()
        # Обнуление данных в таблицах
        UserProfile.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()
        Tag.objects.all().delete()

        # Создание пользователей
        num_users = kwargs['total']
        for _ in range(num_users):
            user = UserProfile(name=fake.name())
            user.save()

        # Создание тэгов
        num_tags = num_users
        for _ in range(num_tags):
            tag = Tag(name=fake.word())
            tag.save()

        
    

        # Создание вопросов
        num_questions = num_users * 10
        for _ in range(num_questions):
            question = Question(title=fake.sentence(nb_words=5), text=fake.text(), rating=fake.random_int(min=0, max=100),
                                view=fake.random_int(min=0, max=100),user_profile =  UserProfile.objects.order_by('?').first())
            question.save()
            question.tags.set(Tag.objects.order_by('?')[:fake.random_int(min=1, max=3)])

        num_answers = num_users * 100
        for _ in range(num_answers):
            answer = Answer(text=fake.text(),correct = False,question = Question.objects.order_by('?').first(), user_profile =  UserProfile.objects.order_by('?').first())
            answer.save()
        # Создание ответов
        # Создание оценок пользователей
        num_ratings = num_users * 200
        for _ in range(num_ratings):
            rating = fake.random_int(min=-1, max=1)
            question = Question.objects.order_by('?').first()
            answer = Answer.objects.order_by('?').first()
            question.rating += rating
            answer.rating += rating
            question.save()
            answer.save()