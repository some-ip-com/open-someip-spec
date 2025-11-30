
:orphan:

.. This file is part of the Open SOME/IP Specification.
.. 
.. Copyright (c) 2025 Technica Engineering GmbH
.. 
.. This file is licensed under the SOME/IP Community Specification License.
.. You can find a copy of this license in the Open SOME/IP Specification repository.
..
.. see https://some-ip.com and https://github.com/some-ip-com/open-someip-spec/

.. ###########################
.. Migration and Compatibility
.. ###########################


.. heading:: Migration and Compatibility
    :id: feat_req_someipcompat_712
    :layout: focus
    :style: clean

.. rst-class:: break_before

Migration and Compatibility
########################### 

.. heading:: Supporting forward compatibility
    :id: feat_req_someipcompat_1196
    :layout: focus
    :style: clean

Supporting forward compatibility
******************************** 

.. feat_req:: ⓘ 
    :id: feat_req_someipcompat_1205
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
This section shows requirements for compatibility, so that vehicles can be further enhanced with additional ECUs and functions. These requirements may exist already earlier in this document but are repeated here in order to ease understanding.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_1197
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
FindService entries shall always set the Minor Version to ANY (0xffff ffff), so that changing the Minor Version of a Service does not require changes on the peer.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_1216
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
ECUs shall subscribe to Eventgroups independently of the Minor Version of the Service.

Note: Changes that only affect the Minor Version changes are compatible changes.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_1198
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall support receiving longer SOME/IP messages as configured and cut off the bytes on the end that were not configured.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_1199
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall support receiving longer dynamic length elements in SOME/IP messages (e.g. arrays or structs with length field) and cut off the bytes at the end of this element that were not configured.

    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_1200
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall support setting default values to parameters in order to allow receiving SOME/IP messages that do not carry the new parameters yet or shall support missing parameters by another mean.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_1201
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall support receiving unknown SOME/IP messages (using nPDU or single) and dropping them (e.g. new events in an old eventgroup).
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_1202
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall allow every client to access every SOME/IP Service Instance and Eventgroup that is configured on the port.

Note: This means it is forbidden to limit the resources, so that a client can only access the Services that are currently configured. If another Eventgroup or Service Instance is available on this socket, the SOME/IP implementation may not limit access to it by means of resources.
    
.. heading:: Supporting multiple versions of the same service.
    :id: feat_req_someipcompat_713
    :layout: focus
    :style: clean

Supporting multiple versions of the same service.
************************************************* 

.. feat_req:: 🎯
    :id: feat_req_someipcompat_714
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In order to support migrations scenarios ECUs shall support serving as well as using different incompatible versions of the same service.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_799
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In order to support a Service with more than one version the following is required:
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_800
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The server shall offer the service instance of this service once per major version.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_802
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The client shall find the service instances once per supported major version or shall use the major version as 0xFF (all versions).
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_804
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The client shall subscribe to events of the service version it needs.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_803
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* All SOME/IP-SD entries shall use the same Service IDs and Instance IDs but different Major Versions.
    
.. feat_req:: 🎯
    :id: feat_req_someipcompat_801
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The server has to demultiplex messages based on the socket it arrives, the Message ID, and the Major Version.
    