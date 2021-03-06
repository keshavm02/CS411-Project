# Generated by Django 3.1.4 on 2020-12-07 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='ranking_field_1',
            new_name='overall',
        ),
        migrations.AddField(
            model_name='review',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='AuthorReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.review')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
            bases=('main.review',),
        ),
        migrations.CreateModel(
            name='ArticleReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.review')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
            ],
            bases=('main.review',),
        ),
    ]
