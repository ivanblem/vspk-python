.. _nuoverlaymirrordestination:

nuoverlaymirrordestination
===========================================

.. class:: nuoverlaymirrordestination.NUOverlayMirrorDestination(bambou.nurest_object.NUMetaRESTObject,):

Overlay mirror destinations are pointed to by advanced forwarding policies as the destination for redirected traffic. Targets can be of two types, L3 or virtual wire. For L3 targets a virtual IP should be provided as it allows the system to track among which of the end-points belonging to the overlay mirror destination is the active one. For this type of redirect the packet's destination MAC address is changed to match that of the Virtual IP. For virtual-wire redirection targets, the packets are untouched and forwarded directly to the end-point.


Attributes
----------


- ``esi``: ESI id, globally unique

- ``name``: Name of this overlay mirror destination

- ``last_updated_by``: ID of the user who last updated the object.

- ``redundancy_enabled``: Allow/Disallow redundant appliances and VIP

- ``template_id``: Template to which this overlay mirror destination belongs to

- ``description``: Description of this overlay mirror destination

- ``destination_type``: Determines the type of destination : redirection target or overlay mirror destination

- ``virtual_network_id``: Auto Generated by VSD. Each overlay mirror destination with redundancy=enable and EndpointType != none will have a globally unique ESI & VNID generated by VSD

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_point_type`` (**Mandatory**): EndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a mirror destination. Possible value is VIRTUAL_WIRE

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``trigger_type``: Trigger type, THIS IS READ ONLY. Possible values are NONE, GARP.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`numirrordestinationgroup.NUMirrorDestinationGroup<numirrordestinationgroup>`

