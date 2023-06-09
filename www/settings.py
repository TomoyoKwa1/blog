# -*- coding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nrnen$7n$+(sm7qtu808qryubv$0)x$)y3)w9-84s)_#cjr2(l'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['18.191.169.252']


# 正式部署时使用
# DEBUG = False
# ALLOWED_HOSTS = ['localhost','.bgods.cn','bgods.cn']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog.apps.BlogConfig',  # 注册app应用
    'comment.apps.CommentConfig',  # 注册app应用
    'ckeditor',  # 注册富文本编辑器
    'ckeditor_uploader',  # 上传文件
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'www.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'www.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")  # 静态文件收集路径

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "common_static"),
]

MEDIA_URL = '/media/'
# 放在django项目根目录，同时也需要创建media文件夹
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

# CKEDITOR编辑器配置
CKEDITOR_CONFIGS = {
    # 配置名是default时，django-ckeditor默认使用这个配置
    'default': {
        # 使用简体中文
        'language': 'en',
        # 编辑器的宽高请根据你的页面自行设置
        'width': 'auto',
        'height': '400px',
        'image_previewText': ' ',
        'tabSpaces': 4,
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],

            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Link', 'Unlink', 'Anchor'],
            ['Blockquote', 'CodeSnippet'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
        ),
        # 添加按钮在这里
        'toolbar_Custom': [],
        # 插件
        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils', 'prism', 'clipboard', ]),
    },

    # 评论富文本编辑器
    'comment': {
        # 使用简体中文
        'language': 'zh-cn',
        # 编辑器的宽高请根据你的页面自行设置
        'width': 'auto',
        'height': '300px',
        'image_previewText': ' ',
        'tabSpaces': 4,
        'toolbar': (
            ['Smiley', 'CodeSnippet'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize', 'TextColor', 'BGColor'],
            ['About']
        ),
        # 添加按钮在这里
        'toolbar_Custom': [],
        # 插件
        'extraPlugins': ','.join(['codesnippet', 'widget', 'lineutils', 'prism', 'clipboard']),
    }
}


#  邮箱配置
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'koustttu@gmail.com'  # 邮箱帐号：用于发送邮件的账号
EMAIL_HOST_PASSWORD = 'Shi-603Kawa11'        # 邮箱密码：用于发送邮件的账号密码
DEFAULT_FROM_EMAIL = 'コウ <koustttu@gmail.com>'   # 发件人，邮件头部显示
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_RECEIVE_LIST = [
    'koustttu@gmail.com',
]  # 接收邮件帐号列表(可写多个)： 有评论时候，通知哪些邮箱，可以是发件邮箱或者其他

