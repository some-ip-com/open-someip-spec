
:orphan:

.. This file is part of the Open SOME/IP Specification.
.. 
.. Copyright (c) 2025 Technica Engineering GmbH
.. 
.. This file is licensed under the SOME/IP Community Specification License.
.. You can find a copy of this license in the Open SOME/IP Specification repository.
..
.. see https://some-ip.com and https://github.com/some-ip-com/open-someip-spec/

.. ###########################################################
.. Reserved and special identifiers for SOME/IP and SOME/IP-SD
.. ###########################################################


.. heading:: Reserved and special identifiers for SOME/IP and SOME/IP-SD.
    :id: feat_req_someipids_504
    :layout: focus
    :style: clean

.. rst-class:: break_before

Reserved and special identifiers for SOME/IP and SOME/IP-SD.
############################################################ 

.. feat_req:: ⓘ 
    :id: feat_req_someipids_554
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In this chapter an overview of reserved and special identifiers are shown.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipids_505
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Reserved and special Service-IDs:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier
      :widths: 30 70
      
      * - Service ID 
        - Description
      * - 0x0000 
        - Reserved
      * - 0xFFFE 
        - Reserved for announcing non-SOME/IP service instances.
      * - 0xFFFF 
        - SOME/IP and SOME/IP-SD special service (e.g.Magic Cookie,SOME/IP-SD, ...).

.. feat_req:: ⓘ 
    :id: feat_req_someipids_636
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Reserved and special Method-IDs/Event-IDs:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      * - Method ID/Event ID 
        - Description
      * - 0x0000 
        - Reserved
      * - 0x7FFF 
        - Reserved
      * - 0x8000 
        - Reserved
      * - 0xFFFF 
        - Reserved

.. feat_req:: ⓘ 
    :id: feat_req_someipids_555
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Reserved and special Eventgroup-IDs:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      * - Eventgroup ID 
        - Description
      * - 0x0000 
        - Reserved
      * - 0xFFFF 
        - All Eventgroups

.. feat_req:: ⓘ 
    :id: feat_req_someipids_530
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Method-IDs and Event-IDs of Service 0xFFFF:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      * - Method ID / Event ID 
        - Description
      * - 0x0000 
        - SOME/IP Magic Cookie Messages
      * - 0x8000 
        - SOME/IP Magic Cookie Messages
      * - 0x8100 
        - SOME/IP-SD messages (events)
