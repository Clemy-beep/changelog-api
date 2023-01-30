# Generated by Django 4.1.5 on 2023-01-30 18:33

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_remove_post_publish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('no-type', 'No category'), ('weekly', 'Weekly update'), ('announcement', 'Announcement'), ('community', 'Community Highlight')], default='no-type', max_length=12),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=200)),
                ('heading', models.CharField(max_length=200)),
                ('body', django_ckeditor_5.fields.CKEditor5Field()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='blog.post')),
            ],
        ),
    ]
