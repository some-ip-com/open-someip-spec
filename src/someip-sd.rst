
:orphan:

.. This file is part of the Open SOME/IP Specification.
.. 
.. Copyright (c) 2025 Technica Engineering GmbH
.. 
.. This file is licensed under the SOME/IP Community Specification License.
.. You can find a copy of this license in the Open SOME/IP Specification repository.
..
.. see https://some-ip.com and https://github.com/some-ip-com/open-someip-spec/

.. ########################
.. SOME/IP-SD Specification
.. ########################


.. heading:: SOME/IP Service Discovery (SOME/IP-SD)
    :id: feat_req_someipsd_1
    :layout: focus
    :style: clean

.. rst-class:: break_before

SOME/IP Service Discovery (SOME/IP-SD)
###################################### 

.. heading:: General
    :id: feat_req_someipsd_182
    :layout: focus
    :style: clean

General
******* 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_183
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Service Discovery is used to locate service instances and to detect if service instances are running.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_184
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Inside the vehicular network service instance locations are commonly known; therefore, the state of the service instance is of primary concern. The location of the service (i.e. IP-Address, transport protocol, and port number) are of secondary concern.
    
.. heading:: Terms and Definitions
    :id: feat_req_someipsd_2
    :layout: focus
    :style: clean

Terms and Definitions
===================== 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_497
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The terms and definitions of SOME/IP RPC shall apply for SOME/IP-SD as well. See :need:`feat_req_someip_14`.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_351
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Offering a service instance shall mean that one ECU implements an instance of a service and tells other ECUs using SOME/IP-SD that they may use it.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_20
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Requiring a service instance shall mean to send a SOME/IP-SD message to the ECU implementing the required service instance with the meaning that this service instance is needed by the other ECU. This may be also sent if the service instance is not running; thus, was not offered yet.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_21
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Releasing a service instance shall mean to sent a SOME/IP-SD message to the ECU hosting this service instances with the meaning that the service instance is not longer needed.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_6
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The configuration and required data of a service instance the local ECU offers, shall be called Server-Service-Instance-Entry.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_8
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The configuration and required data of a service instance another ECU offers shall be called Client-Service-Instance-Entry.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_9
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Server-Service-Instance-Entry shall include one Interface Identifier of the interface the service is offered on.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_10
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Client-Service-Instance-Entry shall include one Interface Identifier of the interface the service is configured to be accessed with.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_11
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Multiple Server-Service-Instance-Entry entries shall be used, if an service instance needs to be offered on multiple interfaces.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_12
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Multiple Client-Service-Instance-Entry entries shall be used, if an service instance needs to be configured to be accessed using multiple different interfaces.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_494
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publishing an eventgroup shall mean to offer an eventgroup of an service instance to other ECUs using a SOME/IP-SD message.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_495
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribing an eventgroup shall mean to require an evengroup of an service instance using a SOME/IP-SD message.
    
.. heading:: SOME/IP-SD ECU-internal Interface
    :id: feat_req_someipsd_13
    :layout: focus
    :style: clean

SOME/IP-SD ECU-internal Interface
********************************* 

.. feat_req:: 🎯
    :id: feat_req_someipsd_17
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Service status shall be defined as up or down as well as required and released:
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_352
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* A service status of up shall mean that a service instance is available; thus, it can be accessed using the communication method specified and is able to fulfil its specified function.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_353
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* A service status of down shall mean the opposite of the service status up.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_354
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* A service status of required shall mean that service instance is needed by another software component in the system to function.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_355
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* A service status of released shall mean the opposite of the service status required.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_356
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The combination of service status up/down with required/released shall be support. Four different valid combinations shall exist (up+required, up+released, down+required, down+released).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_14
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery Interface shall inform local software components about the status of remote services (up/down).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_18
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery Interface shall offer the option to local software component to require or release a remote service instance.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_16
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery Interface shall inform local software components of the require/release status of local services.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_22
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery Interface shall offer the option to local software component to set a local service status (up/down).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_203
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Eventgroup status shall be defined in the same way the service status is defined.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_204
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Service Discovery shall be used to turn on/off the events of a given eventgroup. Only if another ECU requires an eventgroup the events of this eventgroup are sent. (See :need:`feat_req_someipsd_230`).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_23
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall be informed of link-up and link-down events of logical, virtual, and physical communication interfaces that the Service Discovery is bound to.
    
.. heading:: SOME/IP-SD Message Format
    :id: feat_req_someipsd_24
    :layout: focus
    :style: clean

SOME/IP-SD Message Format
************************* 

.. heading:: General Requirements
    :id: feat_req_someipsd_96
    :layout: focus
    :style: clean

General Requirements
==================== 

.. feat_req:: 🎯
    :id: feat_req_someipsd_27
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Service Discovery messages shall be supported over UDP.
Transporting Service Discovery messages over TCP shall be prepared for future usage cases.

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_26
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Service Discovery Messages shall start with a SOME/IP header as depicted Figure :need:`feat_req_someipsd_205`:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_28
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall use the Service-ID (16 Bits) of 0xFFFF.

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_29
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall use the Method-ID (16 Bits) of 0x8100.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_207
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall use a uint32 length field as specified by SOME/IP. That means that the length is measured in bytes and starts with the first byte after the length field and ends with the last byte of the SOME/IP-SD message.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_31
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Client-ID (16 Bits) and handle it based on SOME/IP rules.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_32
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Session-ID (16 Bits) and handle it based on SOME/IP requirements.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_33
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The Session-ID (SOME/IP header) shall be incremented for every SOME/IP-SD message sent.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_34
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Protocol-Version (8 Bits) of 0x01.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_30
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Interface-Version (8 Bits) of 0x01.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_36
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Message Type (8 bits) of 0x02 (Notification).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_37
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Return Code (8 bits) of 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_205
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Header Format

.. bitfield_directive:: images/bit_field/feat_req_someipsd_205.json

    
.. heading:: Header
    :id: feat_req_someipsd_97
    :layout: focus
    :style: clean

Header
====== 

.. feat_req:: 🎯
    :id: feat_req_someipsd_38
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After the SOME/IP header the SOME/IP-SD Header shall follow as depicted in Figure :need:`feat_req_someipsd_205`.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_39
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The SOME/IP-SD Header shall start out with an 8 Bit field called Flags.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_40
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The first flag of the SOME/IP-SD Flags field (highest order bit) shall be called Reboot Flag.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_41
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Reboot Flag of the SOME/IP-SD Header shall be set to one for all messages after reboot until the Session-ID in the SOME/IP-Header wraps around and thus starts with 0 again.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_87
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The second flag of the SOME/IP-SD Flags (second highest order bit) shall be called Unicast Flag and shall be set to 1 for Unicast and 0 for Multicast.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_100
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Unicast Flag of the SOME/IP-SD Header shall be set to Unicast (that means 1) for Request Messages and Subscribe Messages.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_42
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After the Flags the SOME/IP-SD Header shall have a field of 24 bits called Reserved that is set to 0 until further notice.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_101
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After the SOME/IP-SD Header the Entries Array shall follow.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_103
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After the Entries Array in the SOME/IP-SD Header an Option Array shall follow.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_44
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Entries Array and the Options Array of the SOME/IP-SD Header shall start with an length field as uint32 that counts the number of bytes of the following data; i.e. the Entries or the Options.
    
.. heading:: Entry Format
    :id: feat_req_someipsd_94
    :layout: focus
    :style: clean

Entry Format
============ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_46
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Two types of Entries exist: Type 1 Entries for Services and Type 2 Entries for Eventgroups.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_47
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A Type 1 Entry shall be 16 Bytes of size and include the following fields in this order as shown in Figure :need:`feat_req_someipsd_208`:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_49
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type Field [uint8]: encodes FindService (0x00), OfferService (0x01), and RequestService (0x02).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_50
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index First Option Run [uint8]: Index of the option in the option array.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_51
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index Second Option Run [uint8]: Index of the option in the option array.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_52
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Number of Options 1 [uint4]: Describes the number of options the first option run uses.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_53
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Number of Options 2 [uint4]: Describes the number of options the second option run uses.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_54
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service-ID [uint16]: Describes the Service-ID of the Service or Service-Instance concerned by the SD message.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_55
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID [uint16]: Describes the Service-Instance-ID of the Service Instance concerned by the SD message or is set to 0xFFFF if all service instances of a service are meant.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_56
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version [uint8]: Encodes the major version of the service.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_57
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL [uint24]: Describes the lifetime of the entry in seconds.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_58
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Minor Version [uint32]: Encodes the minor version of the service.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_208
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Service Entry Type

.. bitfield_directive:: images/bit_field/feat_req_someipsd_208.json

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_109
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A Type 2 Entry shall be 16 Bytes of size and include the following fields in this order as shown in Figure :need:`feat_req_someipsd_209`:

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_110
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type Field [uint8]: encodes FindEventgroup (0x04), Publish (0x05), and Subscribe (0x06).

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_111
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index First Option Run [uint8]: Index of the option in the option array.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_112
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index Second Option Run [uint8]: Index of the option in the option array.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_113
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Number of Options 1 [uint4]: Describes the number of options the first option run uses.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_114
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Number of Options 2 [uint4]: Describes the number of options the second option run uses.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_115
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service-ID [uint16]: Describes the Service-ID of the Service or Service-Instance concerned by the SD message.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_116
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID [uint16]: Describes the Service-Instance-ID of the Service Instance concerned by the SD message or is set to 0xFFFF if all service instances of a service are meant.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_117
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_118
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL [uint24]: Describes the lifetime of the entry in seconds.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_119
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint16]: Shall be set to 0x0000.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_120
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Eventgroup ID [uint16]: Transports the ID of an Eventgroup.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_209
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Eventgroup Entry Type

.. bitfield_directive:: images/bit_field/feat_req_someipsd_209.json

    
.. heading:: Options Format
    :id: feat_req_someipsd_104
    :layout: focus
    :style: clean

Options Format
============== 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_122
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In order to identify the option type every option shall start with:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_123
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Specifies the length of the option in Bytes.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_124
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Specifying the type of the option.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_133
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The length field shall not cover the length of the length field and type field.
    
.. heading:: Configuration Option
    :id: feat_req_someipsd_139
    :layout: focus
    :style: clean

Configuration Option
-------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_152
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The format of the Configuration Option shall be as follows:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_153
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Shall be set to the total number of bytes occupied by the configuration option, excluding the 16 bit length field and the 8 bit type flag.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_154
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Shall be set to 0x01.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_155
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_156
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* ConfigurationString [dyn length]: Shall carry the configuration string.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_149
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Configuration Option shall specify a set of name-value-pairs based on the DNS TXT and DNS-SD format.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_150
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The format of the configuration string shall start with a single byte length field that describes the number of bytes following this length field.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_151
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After each character sequence another length field and a following character sequence are expected until a length field set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_158
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After a length field set to 0x00 no characters follow.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_159
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A character sequence shall encode a key and an optionally a value.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_157
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The character sequences shall contain an equal character ("=", 0x03D) to divide key and value.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_162
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The key shall not include an equal character and shall be at least one non-whitespace character. The characters of "Key" shall be printable US-ASCII values (0x20-0x7E), excluding '=' (0x3D). 
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_161
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The "=" shall not be the first character of the sequence.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_160
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For a character sequence without an '=' that key shall be interpreted as present.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_217
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For a character sequence ending on an '=' that key shall be interpreted as present with empty value.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_218
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The configuration option shall be also used to encode hostname, servicename, and instancename (if needed).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_201
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_144` shows the format of the Configuration Option and Figure :need:`feat_req_someipsd_147` and example for the Configuration Option.

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_144
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Configuration Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_144.json

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_147
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Configuration Option Example

.. bitfield_directive:: images/bit_field/feat_req_someipsd_147.json

    
.. heading:: Load Balancing Option (informational)
    :id: feat_req_someipsd_145
    :layout: focus
    :style: clean

Load Balancing Option (informational)
------------------------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_146
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Load Balancing Option shall use the Type 0x02.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_174
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Load Balancing Option shall carry a Priority and Weight like the DNS-SRV records, which can be used to load balancing different service instances.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_175
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Format of the IPv4 Endpoint Option shall be as follows:
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_176
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Shall be set to 0x0005.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_177
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Shall be set to 0x02.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_178
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_179
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Priority [uint16]: Carries the Priority of this instance.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_180
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Weight [uint16]: Carries the Weight of this instance.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_200
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_148` shows the format of the Load Balancing Option.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_148
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Load Balancing Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_148.json

    
.. heading:: IPv4 Endpoint Option
    :id: feat_req_someipsd_126
    :layout: focus
    :style: clean

IPv4 Endpoint Option
-------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_127
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 Endpoint Option shall use the Type 0x04.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_128
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 Endpoint Option shall specify the IPv4-Address, the Layer 4 Protocol used, and the Layer 4 Port Number.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_129
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Format of the IPv4 Endpoint Option shall be as follows:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_130
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Shall be set to 0x0009.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_131
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Shall be set to 0x04.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_132
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_134
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* IPv4-Address [uint32]: Shall transport the IP-Address as four Bytes.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_135
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_136
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* L4-Proto [uint8]: Shall be set to the layer 4 protocol based on the IANA/IETF types (0x06: TCP, 0x11: UDP).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_171
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* L4-Port [uint16]: Shall be set to the port of the layer 4 protocol.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_199
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_141` shows the format of the IPv4 Endpoint Option.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_141
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD IPv4 Endpoint Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_141.json

    
.. heading:: IPv6 Endpoint Option
    :id: feat_req_someipsd_138
    :layout: focus
    :style: clean

IPv6 Endpoint Option
-------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_140
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 Endpoint Option shall use the Type 0x06.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_163
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 Endpoint Option shall specify the IPv6-Address, the Layer 4 Protocol used, and the Layer 4 Port Number.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_164
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Format of the IPv6 Endpoint Option shall be as follows:
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_165
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Shall be set to 0x0015.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_166
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Shall be set to 0x06.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_167
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_168
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* IPv4-Address [uint128]: Shall transport the IP-Address as 16 Bytes.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_169
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_170
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* L4-Proto [uint8]: Shall be set to the layer 4 protocol based on the IANA/IETF types (0x06: TCP, 0x11: UDP).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_172
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* L4-Port [uint16]: Shall be set to the port of the layer 4 protocol.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_197
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_142` shows the format of the IPv6 Endpoint Option.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_142
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD IPv6 Endpoint Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_142.json

    
.. heading:: Referencing Options from Entries
    :id: feat_req_someipsd_335
    :layout: focus
    :style: clean

Referencing Options from Entries
================================ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_336
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Using the following fields of the entries, options are referenced by the entries:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_337
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index First Option Run: Index into array of options for first option run. Index 0 means first of SOME/IP-SD packet.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_338
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index Second Option Run: Index into array of options for first option run. Index 0 means first of SOME/IP-SD packet.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_339
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Number of Options 1: Length of first option run. Length 0 means no option in option run.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_340
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Number of Options 2: Length of second option run. Length 0 means no option in option run.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_341
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Two different option runs exist: First Option Run and Second Option Run.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_346
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Rationale for the support of two option runs: Two different types of options are expected: options common between multiple SOME/IP-SD Entries and options different for each SOME/IP-SD Entry. Supporting to different options runs is the most efficient way to support these two types of options, while keeping the wire format highly efficient.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_342
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Each option run shall reference the first option and the number of options for this run.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_343
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the number of options is set to zero, the option run is considered empty.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_348
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For empty runs the Index (i.e. Index First Option Run and/or Index Second Option Run) shall be set to zero.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_347
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall accept and process incoming SD messages with option run length set to zero and option index not set to zero.
    
.. heading:: Example
    :id: feat_req_someipsd_212
    :layout: focus
    :style: clean

Example
======= 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_214
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_213` shows an example SOME/IP-SD PDU. The IP and UDP header are only shown in simplified form.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_213
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Example PDU

.. bitfield_directive:: images/bit_field/feat_req_someipsd_213.json

    
.. heading:: Service Discovery Messages
    :id: feat_req_someipsd_219
    :layout: focus
    :style: clean

Service Discovery Messages
************************** 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_235
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Using the previously specified header format, different entries and messages consisting of one or more entries can be built. The specific entries and there header layouts are explained in the following sections.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_256
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For all entries the following shall be true:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_241
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index First Option Run, Index Second Option Run, Number of Options 1, and Number of Options 2 shall be set according to the chained options.
    
.. heading:: Service Entries
    :id: feat_req_someipsd_224
    :layout: focus
    :style: clean

Service Entries
=============== 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_236
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Entries concerned with services shall be based on the Type 1 Entry Format as specified in :need:`feat_req_someipsd_47`.
    
.. heading:: Find Service Entry
    :id: feat_req_someipsd_220
    :layout: focus
    :style: clean

Find Service Entry
------------------ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_238
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Find Service Entry type shall be used for finding service instances.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_239
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Find Service Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_240
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x00 (FindService).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_242
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID shall be set to the Service ID of the service that shall be found.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_243
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID shall set to 0xFFFF, if all service instances shall be returned. It shall be set to the Instance ID of a specific service instance, if just a single service instance shall be returned.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_244
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to 0xFF, that means that services with any version shall be returned. If set to value different than 0xFF, services with this specific major version shall be returned only.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_245
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Minor Version shall be set to 0xFFFF FFFF, that means that services with any version shall be returned. If set to a value different to 0xFFFF FFFF, services with this specific minor version shall be returned only.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_246
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to the lifetime of the Find Service Entry. After this lifetime the Find Service Entry shall be considered not existing.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_264
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Find Service Entry shall be considered valid until the next reboot.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_265
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.
    
.. heading:: Stop Find Service Entry
    :id: feat_req_someipsd_223
    :layout: focus
    :style: clean

Stop Find Service Entry
----------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_248
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Stop Find Service Entry type shall be used to stop finding service instances.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_249
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Find Service Entries shall be used in communication with optional Service Directories (future use case).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_250
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Find Service Entries shall set the entry fields exactly like the Find Service Entry they are stopping, except:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_251
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to 0x000000.
    
.. heading:: Offer Service Entry
    :id: feat_req_someipsd_221
    :layout: focus
    :style: clean

Offer Service Entry
------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_252
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Offer Service Entry type shall be used to offer a service to other communication partners.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_253
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Offer Service Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_254
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x01 (OfferService).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_255
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID shall be set to the Service ID of the service instance offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_257
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID shall be set to the Instance ID of the service instance offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_258
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to the Major Version of the service instance offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_259
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Minor Version shall be set to the Minor Version of the service instance offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_260
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to the lifetime of the service instance. After this lifetime the service instance shall considered not been offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_266
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Offer Service Entry shall be considered valid until the next reboot.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_267
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.
    
.. heading:: Stop Offer Service Entry
    :id: feat_req_someipsd_225
    :layout: focus
    :style: clean

Stop Offer Service Entry
------------------------ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_261
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Stop Offer Service Entry type shall be used to stop offering service instances.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_262
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Offer Service Entries shall set the entry fields exactly like the Offer Service Entry they are stopping, except:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_263
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to 0x000000.
    
.. heading:: Request Service Entry
    :id: feat_req_someipsd_222
    :layout: focus
    :style: clean

Request Service Entry
--------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_268
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request Service Entry type shall be used to indicate that a service instance is required.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_269
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
An ECU shall consider a Request Service Entry as reason to start the specified service instance if configured to do so.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_271
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Request Service Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_272
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x02 (RequestService).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_273
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID shall be set to the Service ID of the service instance requested.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_274
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID shall be set to the Instance ID of the service instance requested.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_275
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to 0xFF (any).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_276
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Minor Version shall be set to 0xFFFF FFFF (any).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_277
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to the lifetime of the request. After this lifetime the service request shall be considered non-existing. This may lead to an ECU shutting down a service previously requested.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_278
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Request Service Entry shall be considered valid until the next reboot.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_279
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.
    
.. heading:: Stop Request Service Entry
    :id: feat_req_someipsd_226
    :layout: focus
    :style: clean

Stop Request Service Entry
-------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_280
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Stop Request Service Entry type shall be used to stop requests.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_281
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Offer Request Entries shall set the entry fields exactly like the Request Service Entry they are stopping, except:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_282
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to 0x000000.
    
.. heading:: Request Service Acknowledgment (RequestServiceAck) Entry
    :id: feat_req_someipsd_581
    :layout: focus
    :style: clean

Request Service Acknowledgment (RequestServiceAck) Entry
-------------------------------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_582
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request Service Acknowledgment Entry type shall be used to indicate that Request Service Entry was accepted.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_584
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Request Service Acknowledgment Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_585
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x03 (RequestServiceAck).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_586
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID, Instance ID, Major Version, Minor Version and TTL shall be the same value as in the request that is being answered.
    
.. heading:: Request Service Negative Acknowledgment (RequestServiceNack) Entry
    :id: feat_req_someipsd_593
    :layout: focus
    :style: clean

Request Service Negative Acknowledgment (RequestServiceNack) Entry
------------------------------------------------------------------ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_594
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request Service Negative Acknowledgment Entry type shall be used to indicate that Request Service Entry was NOT accepted.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_596
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Request Service Negative Acknowledgment Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_597
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x03 (RequestServiceAck).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_598
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID, Instance ID, Major Version and Minor Version shall be the same value as in the request that is being answered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_611
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The TTL shall set to 0x000000.
    
.. heading:: Eventgroup Entry
    :id: feat_req_someipsd_227
    :layout: focus
    :style: clean

Eventgroup Entry
================ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_237
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Entries concerned with services follow the Type 2 Entry Format as specified in :need:`feat_req_someipsd_109`.
    
.. heading:: Find Eventgroup Entries
    :id: feat_req_someipsd_228
    :layout: focus
    :style: clean

Find Eventgroup Entries
----------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_283
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Find Eventgroup Entry type shall be used for finding eventgroups.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_294
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Find Eventgroup Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_295
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x04 (FindEventgroup).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_296
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID shall be set to the Service ID of the service that includes the eventgroup that shall be found.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_297
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID shall set to 0xFFFF, if eventgroups of all service instances shall be returned. It shall be set to the Instance ID of a specific service instance, if just the eventgroup of a single service instance shall be returned.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_298
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to 0xFF, that means that eventgroups of services with any version shall be returned. If set to value different than 0xFF, eventgroups of services with this specific major version shall be returned only.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_300
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to the lifetime of the Find Eventgroup Entry. After this lifetime the Find Eventgroup Entry shall be considered not existing.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_301
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Find Eventgroup Entry shall be considered valid until the next reboot.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_302
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.
    
.. heading:: Stop Find Eventgroup Entry
    :id: feat_req_someipsd_231
    :layout: focus
    :style: clean

Stop Find Eventgroup Entry
-------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_303
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Stop Find Eventgroup Entry type shall be used to stop finding eventgroups.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_304
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Find Eventgroup Entries shall be used in communication with optional Service Directories (future use case).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_305
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Find Eventgroup Entries shall set the entry fields exactly like the Find Eventgroup Entry they are stopping, except:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_306
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to 0x000000.
    
.. heading:: Publish Eventgroup Entry
    :id: feat_req_someipsd_229
    :layout: focus
    :style: clean

Publish Eventgroup Entry
------------------------ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_307
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Publish Eventgroup Entry type shall be used to offer an eventgroup to other communication partners. This entry type can be considered comparable to the Offer Service Entry type.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_308
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish Eventgroup Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_309
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x05 (PublishEventgroup).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_310
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID shall be set to the Service ID of the service instance that includes the eventgroup published.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_311
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID shall be set to the Instance ID of the service instance that includes the eventgroup published.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_312
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to the Major Version of the service instance that includes the eventgroup published.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_314
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to the lifetime of the eventgroup. After this lifetime the eventgroup shall considered not been published.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_317
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* In most use cases eventgroups will have the same lifetime as the service instance they are part of. A longer lifetime of the eventgroup than the lifetime of the service instance it is part of shall not be allowed.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_315
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Publish Eventgroup Entry shall be considered valid until the next reboot.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_316
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.
    
.. heading:: Stop Publish Eventgroup Entry
    :id: feat_req_someipsd_232
    :layout: focus
    :style: clean

Stop Publish Eventgroup Entry
----------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_318
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Stop Publish Eventgroup Entry type shall be used to stop publishing eventgroups.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_319
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Publish Eventgroup Entries shall set the entry fields exactly like the Publish Eventgroup Entry they are stopping, except:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_320
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to 0x000000.
    
.. heading:: Subscribe Eventgroup Entry
    :id: feat_req_someipsd_230
    :layout: focus
    :style: clean

Subscribe Eventgroup Entry
-------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_321
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Subscribe Eventgroup Entry type shall be used to subscribe to an eventgroup. This can be considered comparable to the Request Service Entry type.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_322
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_323
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x06 (SubscribeEventgroup).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_324
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID shall be set to the Service ID of the service instance that includes the eventgroup subscribed to.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_325
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID shall be set to the Instance ID of the service instance that includes the eventgroup subscribed to.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_326
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to the Major Version of the service instance that includes the eventgroup subscribed to.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_328
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to the lifetime of the eventgroup. After this lifetime the eventgroup shall considered not been subscribed to.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_330
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Subscribe Eventgroup Entry shall be considered valid until the next reboot.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_331
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.
    
.. heading:: Stop Subscribe Eventgroup Entry
    :id: feat_req_someipsd_233
    :layout: focus
    :style: clean

Stop Subscribe Eventgroup Entry
------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_332
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Stop Subscribe Eventgroup Entry type shall be used to stop subscribing to eventgroups.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_333
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Subscribe Eventgroup Entries shall set the entry fields exactly like the Subscribe Eventgroup Entry they are stopping, except:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_334
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to 0x000000.
    
.. heading:: Subscribe Eventgroup Acknowledgement (SubscribeEventgroupAck) Entry
    :id: feat_req_someipsd_612
    :layout: focus
    :style: clean

Subscribe Eventgroup Acknowledgement (SubscribeEventgroupAck) Entry
------------------------------------------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_613
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request Eventgroup Acknowledgment Entry type shall be used to indicate that Request Eventgroup Entry was accepted.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_614
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup Acknowledgment Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_615
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x07 (SubscribeEventgroupAck).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_616
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID, Instance ID, Major Version, Minor Version and TTL shall be the same value as in the request that is being answered.
    
.. heading:: Subscribe Eventgroup Negative Acknowledgement (SubscribeEventgroupNack) Entry
    :id: feat_req_someipsd_617
    :layout: focus
    :style: clean

Subscribe Eventgroup Negative Acknowledgement (SubscribeEventgroupNack) Entry
----------------------------------------------------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_618
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request Eventgroup Negative Acknowledgment Entry type shall be used to indicate that Request Eventgroup Entry was NOT accepted.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_619
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Request Eventgroup Negative Acknowledgment Entries shall set the entry fields in the following way:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_620
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type shall be set to 0x07 (SubscribeEventgroupAck).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_621
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service ID, Instance ID, Major Version and Minor Version shall be the same value as in the request that is being answered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_622
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The TTL shall be set to 0x000000.
    
.. heading:: Service Discovery Communication Behavior
    :id: feat_req_someipsd_25
    :layout: focus
    :style: clean

Service Discovery Communication Behavior
**************************************** 

.. heading:: Startup Behavior
    :id: feat_req_someipsd_59
    :layout: focus
    :style: clean

Startup Behavior
================ 

.. feat_req:: 🎯
    :id: feat_req_someipsd_68
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall be in one of three phases in regard to a service instance:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_69
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Initial Wait Phase
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_70
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Repetition Phase
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_71
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Main Phase
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_72
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
As soon as the system has started and the link on a interface needed for a Service Instance is up, the service discovery enters the Initial Wait Phase for this service instance.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_62
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery implementation shall wait based on the INITIAL_DELAY after entering the Initial Wait Phase and before sending the first messages for the Service Instance.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_63
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
INITIAL_DELAY shall be defined as a minimum and a maximum delay.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_64
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The wait time shall be determined by choosing a random value between the minimum and maximum of INITIAL_DELAY.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_65
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall use the same random value for multiple entries of different types in order to pack them together for a reduced number of messages.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_66
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After sending the first message the Repetition Phase of this Service Instance/these Service Instances is entered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_67
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery implementation shall wait in the Repetitions Phase based on REPETITIONS_BASE_DELAY.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_76
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Between the messages sent in the Repetition Phase the delay is doubled.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_73
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall send out only REPETITIONS_MAX number of packets during the Repetition Phase.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_74
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If REPETITIONS_MAX is set to 0, the Repetition Phase shall be skipped and the Main Phase is entered for the Service Instance after the Initial Wait Phase.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_75
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After the Repetition Phase the Main Phase is being entered for a Service Instance.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_79
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In the Repetition Phase Offer Messages and Publish Messages shall be sent cyclically if a CYCLIC_OFFER_DELAY is configured.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_80
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
After entering the Main Phase 1*CYCLIC_OFFER_DELAY is waited before sending the first message.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_81
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
After a message for a specific Service Instance the Service Discovery waits for 1*CYCLIC_OFFER_DELAY before sending the next message for this Service Instance.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_631
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For Requests/Subscriptions the same cyclic behavior as for the Offers shall be implemented with the parameter CYCLIC_REQUEST_DELAY instead of CYCLIC_OFFER_DELAY.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_77
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Example:

Initial Wait Phase:

* Wait for random_delay in Range(INITIAL_DELAY_MIN, _MAX)
* Send message

Repetition Phase (REPETITIONS_BASE_DELAY=100ms, REPETITIONS_MAX=2):

* Wait 2^0*100ms
* Send message
* Wait 2^1*100ms
* Send message
* Wait 2^2*200ms

Main Phase (as long message is active and CYCLIC_OFFER_DELAY is defined):

* Send message
* Wait CYCLIC_OFFER_DELAY
    
.. heading:: Server Answer Behavior
    :id: feat_req_someipsd_61
    :layout: focus
    :style: clean

Server Answer Behavior
====================== 

.. feat_req:: 🎯
    :id: feat_req_someipsd_83
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall delay multicast/broadcast answers to Find Service Entries and Find Eventgroup Entries as well as multicast/broadcast answers to Request Service Entries and Subscribe Eventgroup Entries after a delay as defined in REQUEST_RESPONSE_DELAY.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_624
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The REQUEST_RESPONSE_DELAY shall not apply if unicast messages are answered with unicast messages.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_86
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The delay shall only apply to Find Service and Find Eventgroup Messages with Instance ID set ANY (0xFFFF).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_202
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Find Service and Find Eventgroup Messages with Instance ID other than 0xFFFF, shall answer without delay.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_84
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
REQUEST_RESPONSE_DELAY shall be specified by a minimum and a maximum.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_85
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The actual delay shall be randomly chosen between minimum and maximum of REQUEST_RESPONSE_DELAY.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_89
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Find messages received with the Unicast Flag set to 1, shall be answered with a unicast response if the last offer was sent when the last message was sent less than 1/2 CYCLIC_OFFER_DELAY (for requests/subscribes this is 1/2 CYCLIC_REQUEST_DELAY) ago.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_90
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Find messages received with the Unicast Flag set to 1, shall be answered with a multicast response if the last offer was sent 1/2 CYCLIC_OFFER_DELAY or longer ago (for requests/subscribes this is 1/2 CYCLIC_REQUEST_DELAY or longer).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_91
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Find messages received with Unicast Flag set to 0 (multicast), shall answered with a multicast response.
    
.. heading:: State Machines
    :id: feat_req_someipsd_627
    :layout: focus
    :style: clean

State Machines
============== 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_628
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In this section the state machines of the client and server are shown.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_629
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP Service State Machine Server

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_629.py

    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_630
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP Service State Machine Client

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_630.py

    
.. heading:: Announcing non-SOME/IP protocols with SOME/IP-SD
    :id: feat_req_someipsd_498
    :layout: focus
    :style: clean

Announcing non-SOME/IP protocols with SOME/IP-SD
************************************************ 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_499
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Besides SOME/IP other communication protocols are used within the vehicle; e.g. for Network Management, Diagnosis, or Flash Updates. Such communications protocols might need to communicate a service instance or have eventgroups as well.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_500
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
For Non-SOME/IP protocols a special Service-ID shall be used and further informational shall be added using the configuration option:

* Service-ID shall be set to 0xFFFE (reserved)
* Instance-ID shall be used as described for SOME/IP services and eventgroups.
* The Configuration Option shall be added and shall contain at least a entry with key "otherserv" and a configurable non-empty value.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_502
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP services shall not use the otherserv-string in the Configuration Option.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_503
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For FindService/OfferService/RequestService the otherserv-String shall be used when announcing non-SOME/IP service instances.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_501
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Example for valid otherserv-string: "otherserv=internaldiag".

Example for a invalid otherserv-string: "otherserv".
Example for a invalid otherserv-string: "otherserv=".
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_575
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD example PDU for Non-SOME/IP-SD

.. bitfield_directive:: images/bit_field/feat_req_someipsd_575.json

    
.. heading:: Publish/Subscribe with SOME/IP and SOME/IP-SD
    :id: feat_req_someipsd_137
    :layout: focus
    :style: clean

.. rst-class:: break_before

Publish/Subscribe with SOME/IP and SOME/IP-SD
############################################# 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_419
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In contrast to the SOME/IP request/response mechanism there may be cases where a client requires a set of parameters from a server, but does not want to request that information each time it is required. These are called notifications and concern events and fields.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_422
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Clients may register using the SOME/IP-SD at run-time with a server in order to receive notifications.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_425
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Notification interaction (extremely simplified)

.. plantuml:: images/plantuml/feat_req_someipsd_425.puml

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_428
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
With the SOME/IP-SD message PublishEventgroup the server offers to push notifications to clients.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_429
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When a server of a notification service starts up (e.g. after reset), it shall send a SOME/IP-SD PublishEventgroup into the network to discover all instances interested in the events and fields offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_430
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Each client in SD based notification implements the specific service-interfaces for the notification they wish to receive and signal their wish of receiving such notifications using the SOME/IP-SD SubscribeEventgroup message.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_431
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Each client shall respond to a SOME/IP-SD PublishEventgroup message from the server with a SOME/IP-SD SubscribeEventgroup message as long as the client is still interested in receiving the notifications/events of this eventgroup.

If the client is able to reliable detect the reboot of the server using the SOME/IP-SD messages reboot flag, the client may choose to only answer PublishEventgroup messages after the server reboots. The client make sure that this works reliable even when the SOME/IP-SD messages of the server are lost.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_632
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Publish/Subscribe with link loss at client (figure ignoring timings)

.. plantuml:: images/plantuml/feat_req_someipsd_632.puml

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_432
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The server sending SOME/IP-SD PublishEventgroup messages has to keep state of SubscribeEventgroup messages for this eventgroup instance in order to know if notifications/events have to be sent.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_433
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A client can deregister from a server by sending a SOME/IP-SD SubscribeEventgroup message with TTL=0 (Stop Offer Service).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_634
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Publish/Subscribe Registration/Deregistration behavior (figure ignoring timings)

.. plantuml:: images/plantuml/feat_req_someipsd_634.puml

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_435
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The SOME/IP-SD on the server shall delete the subscription, if a relevant SOME/IP error is received after sending the push-message.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_437
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the server loses its link on the ethernet link, it SHALL delete all the registered notifications.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_436
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the Ethernet link of the server comes up again, it shall trigger a SOME/IP-SD PublishEventgroup message.

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_633
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Publish/Subscribe with link loss at server (figure ignoring timings)

.. plantuml:: images/plantuml/feat_req_someipsd_633.puml

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_439
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After having not received an notification/event of an eventgroup subscribed to for a certain timeout the ECU shall send a new SubscribeEventgroup message. The timeout shall be configurable for each eventgroup.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_440
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A link-up event on the clients ethernet link shall start the Initial Wait Phase (consider UDP-NM and others). SOME/IP-SD SubscribeEventgroup message shall be sent out as described above.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_441
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After a client has sent a SubscribeEventgroup the server shall send a SubscribeEventgroupAck considering the specified delay behaviour.

If the initial value is of concern - e.g. for fields - the server shall immediately send the first notification/event; i.e. event. The client shall repeat the SubscribeEventgroup message, if he did not receive the notification/event in a configurable timeout.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_625
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Publish/Subscribe State Diagram (server behavior for unicast eventgroups).

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_625.py

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_626
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Publish/Subscribe State Diagram (server behavior for multicast eventgroups).

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_626.py

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_442
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Publish/Subscribe State Diagram (overall behavior).

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_442.py

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_444
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The registration of a client to receive notifications from a server may be implicit. Meaning the mechanism is pre-configured.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_445
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
To allow for cleanup of stale client registrations (to avoid that the list of listeners fills over time), a cleanup mechanism is required.
    