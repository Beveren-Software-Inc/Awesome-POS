# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = "6.3.0"


def console(*data):
    # Import frappe lazily to avoid import errors during package installation
    import frappe
    frappe.publish_realtime("toconsole", data, user=frappe.session.user)
