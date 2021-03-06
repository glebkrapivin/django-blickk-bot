# Generated by Django 3.1.2 on 2020-11-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0011_auto_20201111_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='categorystate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorystate',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='moviecategorystate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviecategorystate',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommendation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sessionquestion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sessionquestion',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='categorystate',
            name='text',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
