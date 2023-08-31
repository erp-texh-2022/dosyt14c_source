# -*- coding: utf-8 -*-
# Part of dosyt. See LICENSE file for full copyright and licensing details.


{
    "name": "Website Jitsi",
    'category': 'Hidden',
    'version': '1.0',
    "summary": "Create Jitsi room on website.",
    'website': 'https://www.dosyt.com/page/events',
    "description": "Create Jitsi room on website.",
    "depends": [
        "website"
    ],
    "data": [
        'views/assets.xml',
        'views/chat_room_templates.xml',
        'views/chat_room_views.xml',
        'views/res_config_settings.xml',
        'security/ir.model.access.csv',
    ],
    'application': False,
    'license': 'LGPL-3',
}
