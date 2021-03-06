# Generated by Django 3.1.2 on 2020-11-11 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_auto_20201111_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryStates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.category')),
            ],
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.categorystates'),
        ),
    ]
