# Generated by Django 3.0.4 on 2020-05-29 21:40

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('articles', '0005_auto_20200529_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
