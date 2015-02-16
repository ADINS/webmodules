# -*- coding: utf-8 -*-
import logging
import simplejson
import os
import openerp
import time
import random
import werkzeug.utils

from openerp import http
from openerp.http import request
from openerp.addons.web.controllers.main import module_boot, login_redirect

_logger = logging.getLogger(__name__)


class PosController(http.Controller):

    @http.route('/test/index', type='http', auth='user')
    def start(self, debug=False, **k):
        cr, uid, context, session = request.cr, request.uid, request.context, request.session

        if not session.uid:
            return login_redirect()
        
        modules =  simplejson.dumps(module_boot(request.db))
        init =  """
                 var wc = new s.web.WebClient();
                 wc.show_application = function(){
                     wc.action_manager.do_action("pos.ui");
                 };
                 wc.setElement($(document.body));
                 wc.start();
                 """
        init = """
                alert("Hello world);
              """
        html = request.registry.get('ir.ui.view').render(cr, session.uid,'mytestview.index',{
            'modules': modules,
            'init': init,
        })

        return html
