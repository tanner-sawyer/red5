# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448322822.227378
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/catalog.edit.html'
_template_uri = 'catalog.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        asset = context.get('asset', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        asset = context.get('asset', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n <div class="col-md-4">\r\n </div>\r\n <div class="col-md-4 content">\r\n    <form method="POST">\r\n        <table>\r\n          ')
        __M_writer(str( form ))
        __M_writer('\r\n        </table>\r\n        <br>\r\n        <button type="submit" class="btn btn-primary">Submit</button>\r\n        <a href="/homepage/catalog.delete/')
        __M_writer(str( asset.id ))
        __M_writer('" class="btn btn-danger">Delete Item</a>\r\n    </form>\r\n  </div>\r\n  <div class="col-md-4">\r\n  </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"48": 3, "66": 60, "37": 1, "56": 3, "57": 10, "42": 21, "59": 14, "28": 0, "58": 10, "60": 14}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/catalog.edit.html", "source_encoding": "utf-8", "uri": "catalog.edit.html"}
__M_END_METADATA
"""
