from django.db import models
'''
@name: table_names
@fields: table_fields
@app_label: application's name
@module: 
@options: meta options
'''
def create_custom_model(name, fields=None, app_label='',  module='', options=None):
    class Meta:
        pass
    
    if app_lable:
        setattr(Meta,'app_lbel', app_lbel)
    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)
    attrs = {'__module__': module, 'Meta': Meta}
    if fields:
        attars.update(fields)
    
    return type(name, (models.Model,), attrs)

def install_model(custom_model):
    from django.db import connection
    from django.db.backends.base.schema import BaseDatabaseSchemaEditor
    editor = BaseDatabaseSchemaEditor(connect)
    try:
        editor.create_model(model=custom_model)
    except AttributeError as aerror:
        print(aerror)


'''
Example
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb_kvm.settings")
django.setup()
from django.db import models
from dytable import install, create_model1
def dy():
    fields={
        'type': models.CharField(max_length=100),
        'category': models.CharField(max_length=1024),
        'title': models.CharField(max_length=10240),
        'answer': models.CharField(max_length=200),
        '__str__': lambda self: '%s %s %s %s' % (self.type, self.category, self.title, self.answer),
    }
    options = {'ordering': ['type', 'category', 'title', 'answer'], 'verbose_name': 'valued customer', }
    #model对象
    custom_model = create_model1('testt', fields, options=options, app_label='dy', module='dy.models')
    install(custom_model) #数据库创建表
    return custom_model

print dy().objects.all()
'''