# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448152574.125018
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/catalog.html'
_template_uri = 'catalog.html'
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
        asset = context.get('asset', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        asset = context.get('asset', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n \r\n <div class="row">\r\n    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">\r\n      <table id="workOrderTable-Table" class="table table-striped table-hover tablesorter-bootstrap">\r\n        <caption class="active">\r\n          <div class="row ">\r\n              <div class="hidden-xs col-sm-12 col-md-12 col-lg-12">\r\n                  <h1 class="text-left">Catalog</h1>\r\n                  <a href="/catalog.create/" class="pull-right btn btn-primary">Create New</a>\r\n              </div>\r\n          </div>\r\n        </caption>\r\n        <thead>\r\n          <tr class="active">\r\n            <th>Asset Code</th>\r\n            <th>Description</th>\r\n            <th>Date Aquired</th>\r\n            <th>Assigned Location</th>\r\n            <th>Assigned Organization</th>\r\n            <th>Date Assigned</th>\r\n            <th>Manufacturer</th>          \r\n            <th>Part Number</th>          \r\n            <th>Maintainence Note</th>\r\n          </tr>\r\n        </thead>\r\n')
        for a in asset:
            __M_writer('        <tbody>\r\n          <tr>\r\n           <td><a href="/catalog.edit/')
            __M_writer(str(a.id))
            __M_writer('">')
            __M_writer(str( a.asset_code ))
            __M_writer('</a></td>\r\n           <td>')
            __M_writer(str( a.description ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.date_acquired ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.location ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.organization_type ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.date_assigned ))
            __M_writer('</td>\r\n           <td>\r\n')
            if a.manufacturer == 'W':
                __M_writer('                Wal-Mart\r\n')
            elif a.manufacturer == 'L':
                __M_writer('                Lockheed Martin\r\n')
            elif a.manufacturer == 'N':
                __M_writer('                Naboo\r\n')
            else:
                __M_writer('                Best Buy\r\n')
            __M_writer('           </td>\r\n           <td>')
            __M_writer(str( a.part_num ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.maintenance_note ))
            __M_writer('</td>\r\n          </tr>\r\n')
        __M_writer('        </tbody>\r\n      </table>\r\n    </div>\r\n    <div class="hidden-xs hidden-sm hidden-md hidden-lg"></div>\r\n  </div><!-- /.row -->\r\n</div><!-- /.container-fluid -->\r\n \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 34, "65": 35, "66": 35, "67": 36, "68": 36, "69": 37, "70": 37, "71": 39, "72": 40, "73": 41, "74": 42, "75": 43, "76": 44, "77": 45, "78": 46, "79": 48, "80": 49, "81": 49, "82": 50, "83": 50, "84": 53, "90": 84, "28": 0, "36": 1, "41": 60, "47": 3, "54": 3, "55": 29, "56": 30, "57": 32, "58": 32, "59": 32, "60": 32, "61": 33, "62": 33, "63": 34}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/catalog.html", "uri": "catalog.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
