# Generated by Django 2.2.6 on 2019-10-30 16:19

import article.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('article_type', models.CharField(choices=[('LEARN_ARTI', 'Learn Article'), ('PRACTICE_ARTI', 'Practice Article'), ('OTHER_ARTI', 'Other')], max_length=20)),
                ('category', models.CharField(choices=[('DS', 'Data Structres'), ('ALGOS', 'Algorithms'), ('ALGOS_ADV', 'Advanced Algorithms'), ('DS_ADV', 'Advanced Data Structures'), ('OTHER', 'Other'), ('NONE', 'NONE')], max_length=20)),
                ('title', models.CharField(max_length=120)),
                ('image_upload', models.ImageField(null=True, upload_to=article.models.articleImageUpload)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LearnCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('DS', 'Data Structres'), ('ALGOS', 'Algorithms'), ('ALGOS_ADV', 'Advanced Algorithms'), ('DS_ADV', 'Advanced Data Structures'), ('OTHER', 'Other'), ('NONE', 'NONE')], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('DS', 'Data Structres'), ('ALGOS', 'Algorithms'), ('ALGOS_ADV', 'Advanced Algorithms'), ('DS_ADV', 'Advanced Data Structures'), ('OTHER', 'Other'), ('NONE', 'NONE')], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120)),
                ('sec_text', models.TextField(blank=True)),
                ('has_subsections', models.BooleanField(default=False)),
                ('gist_url', models.CharField(blank=True, max_length=250)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Weaknesses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=120)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Weaknesses', to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120)),
                ('subsec_text', models.TextField(blank=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subSec', to='article.Article')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subSec', to='article.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Strengths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=120)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Strengths', to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ResourcesCitations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=120)),
                ('url', models.CharField(max_length=20)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources_citations', to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeCategoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=150)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.PracticeCategories')),
            ],
        ),
        migrations.CreateModel(
            name='LearnCategoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=150)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.LearnCategories')),
            ],
        ),
        migrations.CreateModel(
            name='Complexity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insert_best', models.CharField(blank=True, default='N/A', max_length=20)),
                ('insert_avg', models.CharField(blank=True, default='N/A', max_length=20)),
                ('insert_worst', models.CharField(blank=True, default='N/A', max_length=20)),
                ('delete_best', models.CharField(blank=True, default='N/A', max_length=20)),
                ('delete_avg', models.CharField(blank=True, default='N/A', max_length=20)),
                ('delete_worst', models.CharField(blank=True, default='N/A', max_length=20)),
                ('search_best', models.CharField(blank=True, default='N/A', max_length=20)),
                ('search_avg', models.CharField(blank=True, default='N/A', max_length=20)),
                ('search_worst', models.CharField(blank=True, default='N/A', max_length=20)),
                ('space_best', models.CharField(blank=True, default='N/A', max_length=20)),
                ('space_avg', models.CharField(blank=True, default='N/A', max_length=20)),
                ('space_worst', models.CharField(blank=True, default='N/A', max_length=20)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complexity', to='article.Article')),
            ],
        ),
    ]
