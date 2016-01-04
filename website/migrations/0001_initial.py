# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=0)),
                ('ends', models.DateTimeField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('checkout_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('service_comment_id', models.IntegerField()),
                ('username', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('project', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/projects', blank=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=400)),
                ('language', models.CharField(blank=True, max_length=255, choices=[(b'C#', b'C#'), (b'C', b'C'), (b'C++', b'C++'), (b'CSS', b'CSS'), (b'Erlang', b'Erlang'), (b'Haskell', b'Haskell'), (b'HTML', b'HTML'), (b'Java', b'Java'), (b'JavaScript', b'JavaScript'), (b'NodeJS', b'NodeJS'), (b'Perl', b'Perl'), (b'PHP', b'PHP'), (b'Python', b'Python'), (b'Ruby', b'Ruby'), (b'Scala', b'Scala'), (b'Shell', b'Shell'), (b'VB', b'VB')])),
                ('status', models.CharField(default=b'open', max_length=255, choices=[(b'open', b'open'), (b'in review', b'in review'), (b'paid', b'paid')])),
                ('paid', models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)),
                ('closed_by', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('notified_user', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
                ('template', models.CharField(max_length=255)),
                ('regex', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, choices=[(b'json', b'json'), (b'xml', b'xml'), (b'http', b'http')])),
                ('api_url', models.CharField(max_length=255, blank=True)),
                ('link_template', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(help_text=b'Pull Request Link ')),
                ('status', models.CharField(default=b'in review', max_length=250, choices=[(b'in review', b'In review'), (b'Merged or accepted', b'Merged or accepted'), (b'Requested for revision', b'Requested for revision')])),
                ('issue', models.ForeignKey(to='website.Issue')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Taker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(to='website.Issue')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balance', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('payment_service', models.CharField(blank=True, max_length=255, null=True, choices=[(b'wepay', 'WePay')])),
                ('payment_service_email', models.EmailField(default=b'', max_length=255, null=True, blank=True)),
                ('user', models.OneToOneField(related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='service',
            field=models.ForeignKey(related_name='+', to='website.Service'),
        ),
        migrations.AddField(
            model_name='issue',
            name='winner',
            field=models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(to='website.Issue'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='issue',
            field=models.ForeignKey(to='website.Issue'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='issue',
            unique_together=set([('service', 'number', 'project')]),
        ),
    ]
