# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2013 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


class BackendAdapter(object):
    """ Base Backend Adapter for the connectors """

    model_name = None  # define in sub-classes

    @classmethod
    def match(cls, model):
        """ Identify the class to use
        """
        if cls.model_name is None:
            raise NotImplementedError
        if hasattr(model, '_name'):  # model instance
            model_name = model._name
        else:
            model_name = model  # str
        return cls.model_name == model_name
