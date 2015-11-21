# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448146640.223855
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/index.html'
_template_uri = 'index.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n \r\n\t<!-- Main jumbotron for a primary marketing message or call to action -->\r\n    <div class="jumbotron" style="height:400px;">\r\n      <div class="container">\r\n        <h1></h1>\r\n\t\r\n        <p></p>\r\n      </div>\r\n    </div>\r\n\r\n    <div class="container">\r\n      <!-- Example row of columns -->\r\n      <div class="row">\r\n\r\n        <div class="col-md-4">\r\n        \t<div>\r\n        \t\t<h2>View Catalog</h2>\r\n\t\t        <p>I am wondering if this will update with the new deploy. id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>\r\n\t\t        <p><a class="btn btn-default" href="catalog" role="button">View details</a></p>\r\n        \t</div>\r\n        </div>\r\n\r\n        <div class="col-md-4">\r\n          <h2>Add to Catalog</h2>\r\n          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>\r\n          <p><a class="btn btn-default" href="#" role="button">View details</a></p>\r\n       </div>\r\n\r\n        <div class="col-md-4">\r\n          <h2>Help & Support</h2>\r\n          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>\r\n          <p><a class="btn btn-default" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" role="button">View details </a></p>\r\n        </div>\r\n      </div>\r\n    </div> <!-- /container -->\r\n\r\n     \r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "40": 42, "58": 52, "28": 0, "46": 3}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/index.html", "source_encoding": "utf-8", "uri": "index.html"}
__M_END_METADATA
"""
