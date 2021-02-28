# Generated by Django 3.1.7 on 2021-02-28 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='password',
        ),
        migrations.AddField(
            model_name='writing',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='writer.author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
