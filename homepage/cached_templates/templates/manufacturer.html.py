# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448306438.26435
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/manufacturer.html'
_template_uri = 'manufacturer.html'
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
        manufacturer = context.get('manufacturer', UNDEFINED)
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
        def content():
            return render_content(context)
        manufacturer = context.get('manufacturer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="row">\r\n\t  <div class="col-md-4">\r\n\t  \t<a href="/manufacturer.create/" class="pull-right btn btn-primary">Add New</a>\r\n\t  \t<a href="/catalog/" class="pull-right btn btn-success">Catalog</a>\r\n\t  </div>\r\n\t  <div class="col-md-4">\r\n\t\t<table class="table table-hover">\r\n\t\t  <tr>\r\n\t\t\t<th></th>\r\n\t\t \t<th>Maintainence Note</th>\r\n\t\t  </tr>\r\n')
        for a in manufacturer:
            __M_writer('\t        <tbody>\r\n\t          <tr>\r\n\t           <td class="asset_code"><a href="/manufacturer.edit/')
            __M_writer(str(a.id))
            __M_writer('">')
            __M_writer(str( a.id ))
            __M_writer('</a></td>\r\n\t           <td>')
            __M_writer(str( a.name ))
            __M_writer('</td>\r\n\t          </tr>\r\n')
        __M_writer('\t    </table>\r\n\t  </div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "manufacturer.html", "source_encoding": "utf-8", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/manufacturer.html", "line_map": {"68": 62, "36": 1, "60": 19, "46": 3, "53": 3, "54": 15, "55": 16, "56": 18, "57": 18, "58": 18, "59": 18, "28": 0, "61": 19, "62": 22}}
__M_END_METADATA
"""
