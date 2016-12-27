# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-23 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


def default_blog(apps, schema_editor):
    Blog = apps.get_model("blog", "Blog")
    Post = apps.get_model("blog", "Post")
    db_alias = schema_editor.connection.alias
    if settings.PINAX_BLOG_SCOPING_MODEL is None:
        blog = Blog.objects.using(db_alias).create()
        Post.objects.using(db_alias).all().update(blog=blog)  # the only way we migrate existing posts is if there isn't a scoping


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161223_1013'),
    ]

    operations = [
        migrations.RunPython(default_blog)
    ]