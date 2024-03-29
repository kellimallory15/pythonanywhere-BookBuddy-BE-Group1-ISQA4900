# Generated by Django 4.2.10 on 2024-03-28 15:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('death_date', models.DateField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('auth_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_num', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=500)),
                ('publisher', models.CharField(max_length=50)),
                ('published_date', models.DateField(default=django.utils.timezone.now)),
                ('page_total', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='book_authors', to='buddy.author')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('reader_num', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='readers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1000)),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('edited_date', models.DateField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='book_review', to='buddy.book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='reader_review', to='buddy.reader')),
            ],
        ),
        migrations.CreateModel(
            name='BookBuddy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_status', models.BooleanField(default=False, null=True)),
                ('read_status', models.BooleanField(default=False, null=True)),
                ('read_later_status', models.BooleanField(default=False, null=True)),
                ('currently_reading', models.BooleanField(default=False, null=True)),
                ('current_page', models.IntegerField(default=0, null=True)),
                ('last_read', models.DateField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='buddy_book', to='buddy.book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='buddy_reader', to='buddy.reader')),
            ],
        ),
    ]