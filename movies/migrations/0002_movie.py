# Generated by Django 5.0.6 on 2024-06-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='movie_posters/')),
                ('slug', models.SlugField()),
                ('genre', models.ManyToManyField(related_name='movies', to='movies.genre')),
            ],
        ),
    ]
