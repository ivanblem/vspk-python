# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from bambou import NURESTObject


class NUConnectionendpoint(NURESTObject):
    """ Represents a Connectionendpoint in the VSD

        Notes:
            None
    """

    __rest_name__ = "connectionendpoint"
    __resource_name__ = "connectionendpoints"

    
    ## Constants
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_END_POINT_TYPE_SOURCE = "SOURCE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Connectionendpoint instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> connectionendpoint = NUConnectionendpoint(id=u'xxxx-xxx-xxx-xxx', name=u'Connectionendpoint')
                >>> connectionendpoint = NUConnectionendpoint(data=my_dict)
        """

        super(NUConnectionendpoint, self).__init__()

        # Read/Write Attributes
        
        self._ip_address = None
        self._ip_type = None
        self._name = None
        self._description = None
        self._end_point_type = None
        
        self.expose_attribute(local_name="ip_address", remote_name="IPAddress", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_point_type", remote_name="endPointType", attribute_type=str, is_required=False, is_unique=False, choices=[u'SOURCE'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ip_address(self):
        """ Get ip_address value.

            Notes:
                IP Address of the end point.

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        """ Set ip_address value.

            Notes:
                IP Address of the end point.

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        self._ip_address = value

    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                IPv4 or IPv6 (only IPv4 supported for now).

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IPv4 or IPv6 (only IPv4 supported for now).

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the connection endpoint.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the connection endpoint.

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the connection endpoint.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the connection endpoint.

                
        """
        self._description = value

    
    @property
    def end_point_type(self):
        """ Get end_point_type value.

            Notes:
                Indicates if this endpoint is the source/destination of a network connection.

                
                This attribute is named `endPointType` in VSD API.
                
        """
        return self._end_point_type

    @end_point_type.setter
    def end_point_type(self, value):
        """ Set end_point_type value.

            Notes:
                Indicates if this endpoint is the source/destination of a network connection.

                
                This attribute is named `endPointType` in VSD API.
                
        """
        self._end_point_type = value

    

    