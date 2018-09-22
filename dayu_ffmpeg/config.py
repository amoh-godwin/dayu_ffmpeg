#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

import os

# 记录三个平台下，ffmpeg 的执行文件路径
FFMPEG_EXEC = {'win32' : os.sep.join((os.path.dirname(__file__), 'static', 'bin', 'win32', 'ffmpeg.exe')),
               'darwin': os.sep.join((os.path.dirname(__file__), 'static', 'bin', 'darwin', 'ffmpeg')),
               'linux2': 'ffmpeg'}

FFMPEG_DEFAULT_FONT = {
    'win32' : os.sep.join((os.path.dirname(__file__), 'static', 'font', 'SourceHanSansK-Regular.ttf')),
    'darwin': os.sep.join((os.path.dirname(__file__), 'static', 'font', 'SourceHanSansK-Regular.ttf')),
    'linux2': os.sep.join((os.path.dirname(__file__), 'static', 'font', 'SourceHanSansK-Regular.ttf'))}