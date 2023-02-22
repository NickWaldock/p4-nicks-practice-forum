import factory
from django.contrib.auth.models import User
from .models import Post
from factory.faker import faker

FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="admin")[0]

    @factory.lazy_attribute
    def content(self):
        x = ""
        for _ in range(0,5):
            x += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
        return x
    status = "published"
