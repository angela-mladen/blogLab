# Generated by Django 4.2.1 on 2023-05-31 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('files', models.FileField(upload_to='filesUploaded/')),
                ('dateCreated', models.DateField()),
                ('dateModified', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('dateCreated', models.DateField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.blogpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.bloguser')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.bloguser'),
        ),
        migrations.CreateModel(
            name='BlocksUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogUser_blocked', to='blogpost.bloguser')),
                ('blockerUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogUser_blocker', to='blogpost.bloguser')),
            ],
        ),
    ]
