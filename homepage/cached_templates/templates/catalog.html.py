# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448145312.90388
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
        asset = context.get('asset', UNDEFINED)
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
        asset = context.get('asset', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n \r\n <div class="row">\r\n    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">\r\n      <table id="workOrderTable-Table" class="table table-striped table-hover tablesorter-bootstrap">\r\n        <caption class="active">\r\n          <div class="row ">\r\n              <div class="hidden-xs col-sm-4 col-md-4 col-lg-4">\r\n                  <h1 class="text-left">Catalog</h1>\r\n              </div>\r\n              <div class="hidden-xs col-sm-4 col-md-4 col-lg-4">\r\n              </div>\r\n              <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4 text-right tc-margin-top-20">\r\n              </div>\r\n          </div>\r\n        </caption>\r\n        <thead>\r\n          <tr class="active">\r\n            <th class="filter-select" data-placeholder="Search">Asset Code <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>\r\n            <th data-placeholder="Search">Description <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>\r\n            <th class="sorter-shortDate" data-placeholder="Date">Date Aquired <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>\r\n            <th id="dueDateHeader" class="filter-select" data-placeholder="Date">Assigned Location <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>\r\n            <th data-placeholder="Search">Assigned Organization <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>\r\n            <th class="sorter-shortDate" data-placeholder="All">Date Assigned <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>\r\n            <th class="filter-select" data-placeholder="All">Manufacturer <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>          \r\n            <th class="filter-select" data-placeholder="All">Part Number <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>          \r\n            <th class="filter-select" data-placeholder="All">Maintainence Note <span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></th>             <th class="filter-false"></th>\r\n          </tr>\r\n        </thead>\r\n')
        for a in asset:
            __M_writer('        <tbody>\r\n          <tr>\r\n           <td>')
            __M_writer(str( a.asset_code ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.description ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.date_acquired ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.location ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.organization_type ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.date_assigned ))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str( a.manufacturer ))
            __M_writer('</td>\r\n           <td>')
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
{"source_encoding": "utf-8", "uri": "catalog.html", "line_map": {"64": 38, "65": 39, "66": 39, "67": 40, "68": 40, "69": 41, "70": 41, "71": 42, "72": 42, "73": 43, "74": 43, "75": 46, "81": 75, "28": 0, "36": 1, "41": 53, "47": 3, "54": 3, "55": 32, "56": 33, "57": 35, "58": 35, "59": 36, "60": 36, "61": 37, "62": 37, "63": 38}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\red5\\homepage\\templates/catalog.html"}
__M_END_METADATA
"""
