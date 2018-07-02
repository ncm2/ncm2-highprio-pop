# -*- coding: utf-8 -*-

from ncm2_core import ncm2_core
import vim

old_get_sources_for_popup = ncm2_core.get_sources_for_popup

def get_sources_for_popup(data, names):
    global old_get_sources_for_popup
    names = old_get_sources_for_popup(data, names)
    return names[:1]

ncm2_core.get_sources_for_popup = get_sources_for_popup
