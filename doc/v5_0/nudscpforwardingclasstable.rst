.. _nudscpforwardingclasstable:

nudscpforwardingclasstable
===========================================

.. class:: nudscpforwardingclasstable.NUDSCPForwardingClassTable(bambou.nurest_object.NUMetaRESTObject,):

DSCP Mapping Tables define a list of mappings from customer's DSCP markings to Forwarding Classes. They can be referenced in QoS policies.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the dscp-fc mapping table.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the dscp-fc mapping table.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nudscpforwardingclassmapping.NUDSCPForwardingClassMapping<nudscpforwardingclassmapping>`                                                                   ``dscp_forwarding_class_mappings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

