# Generated by Django 5.0.4 on 2024-05-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songs',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='songs',
            name='listened',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='songs',
            index=models.Index(fields=['id'], name='music_songs_id_8977f4_idx'),
        ),
    ]