.. _nuospfinstance:

nuospfinstance
===========================================

.. class:: nuospfinstance.NUOSPFInstance(bambou.nurest_object.NUMetaRESTObject,):

The OSPF instance is the highest hierarchical OSPF configuration object in a domain. The OSPF instance allows you to assign global import and export routing policies for OSPF traffic in the domain. 


Attributes
----------


- ``name`` (**Mandatory**): Name of OSPF Instance

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of OSPF Instance

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``preference``: Preference for OSPF Internal Routes.

- ``associated_export_routing_policy_id``: Export OSPF Routing Policy ID 

- ``associated_import_routing_policy_id``: Import OSPF Routing Policy ID

- ``super_backbone_enabled``: Flag to determine whether SuperBackbone is enabled or not.

- ``export_limit``: This command configures the maximum number of routes (prefixes) that can be exported into OSPF from the route table.

- ``export_to_overlay``: Flag which determines whether the routes learnt through BGP and OSPF will be exported to VSC or not. This flag also exists in the NSGRoutingPolicyBinding entity. The NSGRoutingPolicyBinding flag takes precedence over this one.

- ``external_id``: External object ID. Used for integration with third party systems

- ``external_preference``: Preference for OSPF External Routes.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuospfarea.NUOSPFArea<nuospfarea>`                                                                                                                         ``ospf_areas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nudomain.NUDomain<nudomain>`

