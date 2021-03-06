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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NURemoteVrsInfo(NURESTObject):
    """ Represents a RemoteVrsInfo in the VSD

        Notes:
            Represents a VRS present in a remote DC across WAN. SRIC populates this object. This is used for NFIX(Network Function Interconnect).
    """

    __rest_name__ = "remotevrsinfo"
    __resource_name__ = "remotevrsinfos"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a RemoteVrsInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> remotevrsinfo = NURemoteVrsInfo(id=u'xxxx-xxx-xxx-xxx', name=u'RemoteVrsInfo')
                >>> remotevrsinfo = NURemoteVrsInfo(data=my_dict)
        """

        super(NURemoteVrsInfo, self).__init__()

        # Read/Write Attributes
        
        self._label_stack = None
        self._last_updated_by = None
        self._next_hop = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._color = None
        self._vrs_ip = None
        self._external_id = None
        
        self.expose_attribute(local_name="label_stack", remote_name="labelStack", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="next_hop", remote_name="nextHop", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="color", remote_name="color", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_ip", remote_name="vrsIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def label_stack(self):
        """ Get label_stack value.

            Notes:
                Label stack associated with the VRS

                
                This attribute is named `labelStack` in VSD API.
                
        """
        return self._label_stack

    @label_stack.setter
    def label_stack(self, value):
        """ Set label_stack value.

            Notes:
                Label stack associated with the VRS

                
                This attribute is named `labelStack` in VSD API.
                
        """
        self._label_stack = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def next_hop(self):
        """ Get next_hop value.

            Notes:
                Next hop DCGW associated with the VRS

                
                This attribute is named `nextHop` in VSD API.
                
        """
        return self._next_hop

    @next_hop.setter
    def next_hop(self, value):
        """ Set next_hop value.

            Notes:
                Next hop DCGW associated with the VRS

                
                This attribute is named `nextHop` in VSD API.
                
        """
        self._next_hop = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def color(self):
        """ Get color value.

            Notes:
                The color encoded with a traffic engineering constraint such as minimum latency, hops, maximum bandwidth, etc. This is used for NFIX(Network Function Interconnect).

                
        """
        return self._color

    @color.setter
    def color(self, value):
        """ Set color value.

            Notes:
                The color encoded with a traffic engineering constraint such as minimum latency, hops, maximum bandwidth, etc. This is used for NFIX(Network Function Interconnect).

                
        """
        self._color = value

    
    @property
    def vrs_ip(self):
        """ Get vrs_ip value.

            Notes:
                IP of the VRS/Hypervisor

                
                This attribute is named `vrsIP` in VSD API.
                
        """
        return self._vrs_ip

    @vrs_ip.setter
    def vrs_ip(self, value):
        """ Set vrs_ip value.

            Notes:
                IP of the VRS/Hypervisor

                
                This attribute is named `vrsIP` in VSD API.
                
        """
        self._vrs_ip = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    