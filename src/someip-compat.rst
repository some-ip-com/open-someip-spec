
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
    