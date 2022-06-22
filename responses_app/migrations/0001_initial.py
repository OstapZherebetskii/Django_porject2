# Generated by Django 4.0.4 on 2022-06-09 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='responses_app.areas')),
            ],
            options={
                'verbose_name_plural': 'places',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('texttt', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('file', models.ImageField(null=True, upload_to='files/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='responses_app.places')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
