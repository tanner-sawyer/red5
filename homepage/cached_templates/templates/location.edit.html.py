# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448323634.801078
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/location.edit.html'
_template_uri = 'location.edit.html'
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        location = context.get('location', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        location = context.get('location', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n\t <div class="col-md-4">\r\n\t </div>\r\n\t <div class="content col-md-4">\r\n\t    <form method="POST">\r\n\t        <table>\r\n\t          ')
        __M_writer(str( form ))
        __M_writer('\r\n\t        </table>\r\n\t        <br>\r\n\t        <button type="submit" class="btn btn-primary">Submit</button>\r\n\t        <a href="/homepage/location.delete/')
        __M_writer(str( location.id ))
        __M_writer('" class="btn btn-danger">Delete Item</a>\r\n\t    </form>\r\n\t  </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "location.edit.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/location.edit.html", "line_map": {"65": 59, "37": 1, "55": 3, "56": 10, "57": 10, "58": 14, "59": 14, "28": 0, "47": 3}}
__M_END_METADATA
"""
