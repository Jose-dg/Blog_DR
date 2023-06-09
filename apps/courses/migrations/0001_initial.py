# Generated by Django 4.0.6 on 2023-04-06 22:15

import apps.courses.models
import apps.courses.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('is_accepted_answer', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(upload_to=apps.courses.models.course_directory_path)),
                ('sales_video', models.FileField(upload_to=apps.courses.models.course_directory_path)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('student_rating', models.IntegerField(default=0)),
                ('language', models.CharField(choices=[('espanol', 'Espanol'), ('english', 'English')], max_length=50)),
                ('course_length', models.CharField(default=0, max_length=20)),
                ('payment', models.CharField(choices=[('paid', 'Paid'), ('free', 'Free')], default='paid', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('compare_price', models.DecimalField(blank=True, decimal_places=18, max_digits=18, null=True)),
                ('sold', models.IntegerField(blank=True, default=0)),
                ('best_seller', models.BooleanField(default=False)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.useraccount')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category')),
                ('comments', models.ManyToManyField(blank=True, to='courses.comment')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('has_accepted_answer', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Requisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to=apps.courses.models.course_directory_path)),
                ('url', models.URLField(blank=True, null=True)),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WhatLearnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('vote', models.CharField(choices=[('U', 'Up Vote'), ('D', 'Down Vote')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_votes', to='courses.answer')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sector_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('thumbnail', models.ImageField(upload_to=apps.courses.models.sector_directory_path)),
                ('related_courses', models.ManyToManyField(blank=True, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='PaidCoursesLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.useraccount')),
                ('courses', models.ManyToManyField(blank=True, to='courses.course')),
            ],
            options={
                'verbose_name_plural': 'Purchased Courses Library',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to=apps.courses.models.course_directory_path, validators=[apps.courses.validators.validate_is_video])),
                ('content', models.TextField()),
                ('length', models.DecimalField(decimal_places=2, max_digits=100)),
                ('episode_number', models.IntegerField(blank=True, null=True)),
                ('user', models.CharField(max_length=255)),
                ('questions', models.ManyToManyField(blank=True, to='courses.question')),
                ('resources', models.ManyToManyField(blank=True, to='courses.resource')),
            ],
            options={
                'ordering': ('episode_number',),
            },
        ),
        migrations.CreateModel(
            name='CoursesLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.useraccount')),
                ('courses', models.ManyToManyField(blank=True, to='courses.course')),
            ],
            options={
                'verbose_name_plural': 'Bookmarked Courses Library',
            },
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section_number', models.IntegerField(blank=True, null=True)),
                ('section_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user', models.CharField(max_length=255)),
                ('episodes', models.ManyToManyField(blank=True, to='courses.episode')),
            ],
            options={
                'ordering': ('section_number',),
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_section',
            field=models.ManyToManyField(blank=True, to='courses.coursesection'),
        ),
        migrations.AddField(
            model_name='course',
            name='questions',
            field=models.ManyToManyField(blank=True, to='courses.question'),
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.ManyToManyField(blank=True, to='courses.rate'),
        ),
        migrations.AddField(
            model_name='course',
            name='requisite',
            field=models.ManyToManyField(blank=True, to='courses.requisite'),
        ),
        migrations.AddField(
            model_name='course',
            name='resources',
            field=models.ManyToManyField(blank=True, to='courses.resource'),
        ),
        migrations.AddField(
            model_name='course',
            name='what_learnt',
            field=models.ManyToManyField(blank=True, to='courses.whatlearnt'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.question'),
        ),
    ]
