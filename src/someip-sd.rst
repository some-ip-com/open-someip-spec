
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
  
Service Discovery is used to locate service instances and to detect if service instances are running as well as implementing the Publish/Subscribe handling.
    
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
    :id: feat_req_someipsd_769
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Finding a service instance shall mean to send a SOME/IP-SD message in order to find a needed service instance.
    
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
  
The configuration and required data of a service instance the local ECU offers, shall be called Server-Service-Instance-Entry at the ECU offering this service (Server).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_8
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The configuration and required data of a service instance another ECU offers shall be called Client-Service-Instance-Entry at the ECU using this service (Client).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_9
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Server-Service-Instance-Entry shall include one Interface Identifier of the communication interface (e.g. Ethernet interface or virtual interface based on Ethernet VLANs) the service is offered on.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_10
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Client-Service-Instance-Entry shall include one Interface Identifier of the communication interface the service is configured to be accessed with.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_11
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Multiple Server-Service-Instance-Entry entries shall be used, if a service instance needs to be offered on multiple interfaces.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_12
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Multiple Client-Service-Instance-Entry entries shall be used, if a service instance needs to be configured to be accessed using multiple different interfaces.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_494
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publishing an eventgroup shall mean to offer an eventgroup of a service instance to other ECUs using a SOME/IP-SD message.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_495
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribing an eventgroup shall mean to require an eventgroup of a service instance using a SOME/IP-SD message.
    
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
  
* A service status of up shall mean that a service instance is available; thus, it is accessible using the communication method specified and is able to fulfill its specified function.
    
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
  
* The combination of service status up/down with required/released shall be supported. Four different valid combinations shall exist (up+required, up+released, down+required, down+released).
    
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
  
Service Discovery shall be used to turn on/off the events and notification events of a given eventgroup. Only if another ECU requires an eventgroup the events and notification events of this eventgroup are sent. (See Subscribe Event Group).
    
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
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_720
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
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
  
* Service Discovery messages shall use the Service ID (16 Bits) of 0xFFFF.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_29
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall use the Method ID (16 Bits) of 0x8100.
    
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
  
* Service Discovery messages shall have a Client ID (16 Bits) and handle it based on SOME/IP rules.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1138
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The Client ID shall be set to 0, since there exists only a single SOME/IP-SD instance.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1139
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If a Client ID Prefix is configured, it shall also apply to SOME/IP-SD.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_32
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Session ID (16 Bits) and handle it based on the SOME/IP requirements.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_33
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The Session ID (SOME/IP header) shall be incremented for every SOME/IP-SD message sent.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_774
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The Session ID (SOME/IP header) shall start with 1 and be 1 even after wrapping.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_775
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* The Session ID (SOME/IP header) shall not be set to 0.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1148
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* SOME/IP-SD Session ID handling is done per "communication relation", i.e. broadcast as well as unicast per peer (see :need:`feat_req_someipsd_41`).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_34
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Protocol Version (8 Bits) of 0x01.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_30
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Service Discovery messages shall have a Interface Version (8 Bits) of 0x01.
    
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
  
* Service Discovery messages shall have a Return Code (8 bits) of 0x00 (E_OK).
    
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

    
.. heading:: SOME/IP-SD Header
    :id: feat_req_someipsd_97
    :layout: focus
    :style: clean

SOME/IP-SD Header
================= 

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
  
The Reboot Flag of the SOME/IP-SD Header shall be set to one for all messages after reboot until the Session ID in the SOME/IP-Header wraps around and thus starts with 1 again. After this wrap around the Reboot Flag is set to 0.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_765
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The information for the reboot flag and the Session ID shall be kept for multicast and unicast separately as well as for every sender-receiver-relation (i.e. source address and destination address).

Note: This means you have to store a counter for Multicast sending and one counter per Unicast peer as well as two counters (1x Multicast, 1x Unicast) per SOME/IP-SD peer for receiving.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_863
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP-SD implementations shall reliably detect the reboots of their peer based on the information stated in :need:`feat_req_someipsd_765`.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_764
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The detection of a reboot shall be done as follows (with new the values of the current packet from the communication partner and old the last value received before):

* if old.reboot==0 and new.reboot==1 then Reboot detected
* if old.reboot==1 and new.reboot==1 and old.session_id>=new.session_id then Reboot detected

The following is not enough since we do not have reliable communication:

* if new.reboot==1 and old.session_id>=new.session_id then Reboot detected
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_871
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When the system detects the reboot of a peer, it shall update its state accordingly. Services and Subscriptions shall be expired if they are not updated again.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_872
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When the system detects the reboot of a peer, it shall reset the state of the TCP connections to this peer. The client shall reestablish the TCP as required by the Publish/Subscribe process later.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_87
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The second flag of the SOME/IP-SD Flags (second highest order bit) shall be called Unicast Flag and shall be set to 1, if SD message reception via unicast is supported.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_100
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Unicast Flag of the SOME/IP-SD Header shall be always set to Unicast (that means 1) for all SD Messages since this means that receiving using unicast is supported.
    
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
    :id: feat_req_someipsd_862
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The entries shall be processed exactly in the order they arrive.
    
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
  
The Entries Array and the Options Array of the SOME/IP-SD message shall start with a length field as uint32 that counts the number of bytes of the following data; i.e. the entries or the options.
    
.. heading:: Entry Format
    :id: feat_req_someipsd_94
    :layout: focus
    :style: clean

Entry Format
============ 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_771
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The service discovery shall work on different entries that shall be carried in the service discovery messages. The entries are used to synchronize the state of services instances and the Publish/Subscribe handling.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_46
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Two types of entries exist: A Service Entry Type for Services and an Eventgroup Entry Type for Eventgroups, which are used for different entries each.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_47
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A Service Entry Type shall be 16 Bytes of size and include the following fields in this order as shown in Figure :need:`feat_req_someipsd_208`:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_49
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type Field [uint8]: encodes FindService (0x00) and OfferService (0x01).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_50
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index First Option Run [uint8]: Index of this runs first option in the option array.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_51
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index Second Option Run [uint8]: Index of this runs first option in the option array.
    
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
  
* Service ID [uint16]: Describes the Service ID of the Service or Service-Instance this entry is concerned with.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_55
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID [uint16]: Describes the Service Instance ID of the Service Instance this entry is concerned with or is set to 0xFFFF if all service instances of a service are meant.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_56
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version [uint8]: Encodes the major version of the service (instance).
    
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
  
An Eventgroup Entry shall be 16 Bytes of size and include the following fields in this order as shown in Figure :need:`feat_req_someipsd_209`:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_110
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type Field [uint8]: encodes Subscribe (0x06) and SubscribeAck (0x07).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_111
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index First Option Run [uint8]: Index of this runs first option in the option array.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_112
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Index Second Option Run [uint8]: Index of this runs first option in the option array.
    
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
  
* Service ID [uint16]: Describes the Service ID of the Service or Service-Instance this entry is concerned with.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_116
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID [uint16]: Describes the Service Instance ID of the Service Instance this entry is concerned with or is set to 0xFFFF if all service instances of a service are meant.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_117
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version [uint8]: Encodes the major version of the service instance this eventgroup is part of.
    
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
    :id: feat_req_someipsd_772
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Options are used to transport additional information to the entries. This includes for instance the information how a service instance is reachable (IP-Address, Transport Protocol, Port Number).
    
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
  
The length field shall cover all bytes of the option except the length field and type field.
    
.. heading:: Configuration Option
    :id: feat_req_someipsd_139
    :layout: focus
    :style: clean

Configuration Option
-------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_755
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The configuration option shall be used to transport arbitrary configuration strings. This allows to encode additional information like the name of a service or its configuration.
    
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
    :id: feat_req_someipsd_684
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Multiple entries with the same key in a single Configuration Option shall be supported.
    
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
  
Figure :need:`feat_req_someipsd_144` shows the format of the Configuration Option and Figure :need:`feat_req_someipsd_147` an example for the Configuration Option.
    
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
    :id: feat_req_someipsd_754
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
This option shall be used to prioritize different instances of a service, so that a client chooses the service instance based on these settings. This option will be attached to Offer Service entries.
    
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
  
The Load Balancing Option shall carry a Priority and Weight like the DNS-SRV records, which shall be used to load balancing different service instances.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_770
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
This means when looking for all service instances of a service (Service Instance set to 0xFFFF), the client shall choose the service instance with highest priority. When having more than one service instance with highest priority (lowest value in Priority field) the service instance shall be chosen randomly based on the weights of the service instances.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_175
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Format of the Load Balancing Option shall be as follows:
    
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
  
* Priority [uint16]: Carries the Priority of this instance. Lower value means higher priority.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_180
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Weight [uint16]: Carries the Weight of this instance. Large value means higher probability to be chosen.
    
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

    
.. heading:: Protection Option (informational)
    :id: feat_req_someipsd_576
    :layout: focus
    :style: clean

Protection Option (informational)
--------------------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_753
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
This option shall be used to protect SD messages against changes of the transmission or lower layer protocols.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_577
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Protection option shall use the Type 0x03.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_578
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Protection option shall carry an Alive-Counter, ID, and a CRC to protect the whole message including the SOME/IP header.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_579
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The format of the Protection Option shall be as follows:

* Length [uint16]: Shall be set to 0x0009.
* Type [uint8]: Shall be set to 0x03.
* Reserved [uint8]: Shall be set to 0x00.
* Alive-Counter [uint32]: Shall be set to the value of the alive counter. If no alive counter exists, the value of the Request ID shall be used in this field.
* CRC [uint32]: Shall contain the value of the CRC of this message. The CRC polynomial shall be specified by the OEM.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_580
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If more than one Protection Option is contained in the SOME/IP message, they shall only cover the portion of the message in front of them. In addition, the use of multiple Protection options shall trigger a configurable development error.
    
.. heading:: IPv4 Endpoint Option
    :id: feat_req_someipsd_126
    :layout: focus
    :style: clean

IPv4 Endpoint Option
-------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_752
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 Endpoint Option shall be used by a SOME/IP-SD instance to signal the relevant endpoint(s). Endpoints include the local IP address, the transport layer protocol (e.g. UDP or TCP), and the port number of the sender.

These ports shall be used for the events and notification events as well. When using UDP the server uses the announced port as source port. With TCP the client needs to open a connection to this port before subscription, because this is the TCP connection the server uses for sending events and notification events.
    
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
  
The IPv4 Endpoint Option shall specify the IPv4-Address, the transport layer protocol (ISO/OSI layer 4) used, and its Port Number.
    
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
  
* Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol (ISO/OSI layer 4) based on the IANA/IETF types (0x06: TCP, 0x11: UDP).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_171
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the port of the transport layer protocol (ISO/OSI layer 4).
    
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

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_849
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The server shall use the IPv4 Endpoint Option with Offer Service entries to signal the endpoints it serves the service on. That is up to one UDP endpoint and up to one TCP endpoint.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_850
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The endpoints the server referenced with an Offer Service entry shall also be used as source of events. That is source IP address and source port numbers for the transport protocols in the endpoint option.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_848
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The client shall use the IPv4 Endpoint Options with Subscribe Eventgroup entries to signal its IP address and its UDP and/or TCP port numbers, on which it is ready to receive the events.
    
.. heading:: IPv6 Endpoint Option
    :id: feat_req_someipsd_138
    :layout: focus
    :style: clean

IPv6 Endpoint Option
-------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_751
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 Endpoint Option shall be used by a SOME/IP-SD instance to signal the relevant endpoint(s). Endpoints include the local IP address, the transport layer protocol (e.g. UDP or TCP), and the port number of the sender.

These ports shall be used for the events and notification events as well. When using UDP the server uses the announced port as source port. With TCP the client needs to open a connection to this port before subscription, because this is the TCP connection the server uses for sending events and notification events.
    
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
  
* IPv6-Address [uint128]: Shall transport the IP-Address as 16 Bytes.
    
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
  
* L4-Proto [uint8]: Shall be set to the transport layer protocol (ISO/OSI layer 4) based on the IANA/IETF types (0x06: TCP, 0x11: UDP).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_172
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* L4-Port [uint16]: Shall be set to the port of the transport layer protocol (ISO/OSI layer 4).
    
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

    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_851
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The server shall use the IPv6 Endpoint Option with Offer Service entries to signal the endpoints the services is available on. That is up to one UDP endpoint and up to one TCP endpoint.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_852
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The endpoints the server referenced with an Offer Service entry shall also be used as source of events. That is source IP address and source port numbers for the transport protocols in the endpoint option.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_853
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The client shall use the IPv6 Endpoint Option with Subscribe Eventgroup entries to signal the IP address and the UDP and/or TCP port numbers, on which it is ready to receive the events.
    
.. heading:: IPv4 Multicast Option
    :id: feat_req_someipsd_722
    :layout: focus
    :style: clean

IPv4 Multicast Option
--------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_749
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 Multicast Option is used by the server to announce the IPv4 multicast address, the transport layer protocol (ISO/OSI layer 4), and the port number the multicast events and multicast notification events are sent to. As transport layer protocol currently only UDP is supported.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_854
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 Multicast Option and not the IPv4 Endpoint Option shall be referenced by Subscribe Eventgroup Ack entries.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_723
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 Multicast Option shall use the Type 0x14.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_724
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 Multicast Option shall specify the IPv4-Address, the transport layer protocol (ISO/OSI layer 4) used, and its Port Number.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_725
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Format of the IPv4 Endpoint Option shall be as follows:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_726
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Shall be set to 0x0009.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_727
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Shall be set to 0x14.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_728
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_729
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* IPv4-Address [uint32]: Shall transport the multicast IP-Address as four Bytes.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_730
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_731
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol (ISO/OSI layer 4) based on the IANA/IETF types (0x11: UDP).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_732
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the port of the layer 4 protocol.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_733
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_734` shows the format of the IPv4 Multicast Option.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_734
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD IPv4 Multicast Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_734.json

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_855
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The server shall reference the IPv4 Multicast Option, which encodes the IPv4 Multicast Address and Port Number the server will send multicast events and notification events to.
    
.. heading:: IPv6 Multicast Option
    :id: feat_req_someipsd_736
    :layout: focus
    :style: clean

IPv6 Multicast Option
--------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_750
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 Multicast Option is used by the server to announce the IPv6 multicast address, the layer 4 protocol, and the port number the multicast events and multicast notifications events are sent to. For the transport layer protocol (ISO/OSI layer 4) currently only UDP is supported.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1083
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 Multicast Option and not the IPv6 Endpoint Option shall be referenced by Subscribe Eventgroup Ack messages.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_737
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 Multicast Option shall use the Type 0x16.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_738
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 Multicast Option shall specify the IPv6-Address, the transport layer protocol (ISO/OSI layer 4) used, and its Port Number.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_739
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The Format of the IPv6 Multicast Option shall be as follows:

* Length [uint16]: Shall be set to 0x0015.
* Type [uint8]: Shall be set to 0x16.
* Reserved [uint8]: Shall be set to 0x00.
* IPv6-Address [uint128]: Shall transport the multicast IP-Address as 16 Bytes.
* Reserved [uint8]: Shall be set to 0x00.
* Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol (ISO/OSI layer 4) based on the IANA/IETF types (0x11: UDP).
* Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the port of the transport layer protocol (ISO/OSI layer 4).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_747
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_748` shows the format of the IPv6 Multicast Option.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_748
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD IPv6 Multicast Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_748.json

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_856
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The server shall reference the IPv6 Multicast Option, which encodes the IPv6 Multicast Address and Port Number the server will send multicast events and notification events to.
    
.. heading:: IPv4 SD Endpoint Option
    :id: feat_req_someipsd_1080
    :layout: focus
    :style: clean

IPv4 SD Endpoint Option
----------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1081
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 SD Endpoint Option is used to transport the endpoint (i.e. IP-Address and Port) of the senders SD implementation.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1082
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 SD Endpoint Option shall be included in any SD Options Array up to 1 time.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1156
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 SD Endpoint Option shall only be included if the SOME/IP-SD message is transported over IPv4.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1151
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 SD Endpoint Option shall be the first option in the options array, if existing.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1152
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If more than one IPv4 SD Endpoint Option is received, only the first one shall be processed and all further IPv4 SD Endpoint Options shall be ignored.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1114
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 SD Endpoint Option shall be not referenced by any SD Entry.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1084
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the IPv4 SD Endpoint Option is included in the SD message, the receiving SD implementation shall use the content of this option instead of the Source IP Address and Source Port.

This is important for answering the received SD message (e.g. Offer after Find or Subscribe after Offer or Subscribe Ack after Subscribe) as well as the reboot detection (channel based on SD Endpoint Option and not out addresses).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1085
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 SD Endpoint Option shall use the Type 0x24.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1086
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv4 SD Endpoint Option shall specify the IPv4-Address, the transport layer protocol (ISO/OSI layer 4) used, and its Port Number.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1087
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Format of the IPv4 SD Endpoint Option shall be as follows:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1088
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Shall be set to 0x0015.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1089
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Shall be set to 0x24.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1090
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1091
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* IPv4-Address [uint32]: Shall transport the unicast IP-Address of SOME/IP-SD as four Bytes.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1092
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1093
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol of SOME/IP-SD (currently: 0x11 UDP).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1094
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the transport layer port of SOME/IP-SD (currently: 30490).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1095
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_1096` shows the format of the IPv4 SD Endpoint Option.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1096
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD IPv4 SD Endpoint Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_1096.json

    
.. heading:: IPv6 SD Endpoint Option
    :id: feat_req_someipsd_1097
    :layout: focus
    :style: clean

IPv6 SD Endpoint Option
----------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1098
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 SD Endpoint Option is used to transport the endpoint (i.e. IP-Address and Port) of the senders SD implementation.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1099
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 SD Endpoint Option shall be included in any SD message up to 1 time.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1155
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 SD Endpoint Option shall only be included if the SOME/IP-SD message is transported over IPv6.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1153
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 SD Endpoint Option shall be the first option in the options array, if existing.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1154
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If more than one IPv6 SD Endpoint Option is received, only the first one shall be processed and all further IPv6 SD Endpoint Options shall be ignored.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1113
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 SD Endpoint Option shall be not referenced by any SD Entry.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1100
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the IPv6 SD Endpoint Option is included in the SD message, the receiving SD implementation shall use the content of this option instead of the Source IP Address and Source Port for answering this SD messages.


This is important for answering the received SD messages (e.g. Offer after Find or Subscribe after Offer or Subscribe Ack after Subscribe) as well as the reboot detection (channel based on SD Endpoint Option and not out addresses).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1101
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 SD Endpoint Option shall use the Type 0x24.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1102
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IPv6 SD Endpoint Option shall specify the IPv4-Address, the transport layer protocol (ISO/OSI layer 4) used, and its Port Number.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1103
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Format of the IPv6 SD Endpoint Option shall be as follows:

    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1104
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Length [uint16]: Shall be set to 0x0015.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1105
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Type [uint8]: Shall be set to 0x24.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1106
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1107
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* IPv6-Address [uint128]: Shall transport the unicast IP-Address of SOME/IP-SD as 16 Bytes.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1108
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reserved [uint8]: Shall be set to 0x00.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1109
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol of SOME/IP-SD (currently: 0x11 UDP).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1110
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the transport layer port of SOME/IP-SD (currently: 30490).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1111
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someipsd_1112` shows the format of the IPv6 SD Endpoint Option.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1112
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD IPv6 SD Endpoint Option

.. bitfield_directive:: images/bit_field/feat_req_someipsd_1112.json

    
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
  
* Index Second Option Run: Index into array of options for second option run. Index 0 means first of SOME/IP-SD packet.
    
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
  
Rationale for the support of two option runs: Two different types of options are expected: options common between multiple SOME/IP-SD entries and options different for each SOME/IP-SD entry. Supporting two different options runs is the most efficient way to support these two types of options, while keeping the wire format highly efficient.
    
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
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_900
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall minimize the size of the SD messages by not duplicating Options without need.
    
.. heading:: Handling missing, redundant, and conflicting Options
    :id: feat_req_someipsd_1140
    :layout: focus
    :style: clean

Handling missing, redundant, and conflicting Options
---------------------------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_1142
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If an entry references an unknown option, this option shall be ignored.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1141
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If an entry references an redundant option (option that is not needed by this specific entry), this option shall be ignored.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1143
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Example: A Service needs only a TCP Endpoint but Endpoint Options for UDP and TCP are referenced by the Offer Service entry. UDP endpoint shall be ignored.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1144
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If an entry references two or more options that are in conflict, this entry shall be ignored or answered negatively.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1145
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Example: An Offer Service entry referencing two Endpoint Options stating two different UDP Ports shall be ignored.

Example: An Subscribe Eventgroup entry referencing two Endpoint Options stating two different UDP Ports shall be answered with a Subscribe Eventgroup Nack.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1146
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When two different Configuration Options are referenced by an entry, the configuration sets shall be merged.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1147
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the two Configuration Options have conflicting items (same name), all items shall be handled. There shall be no attempt been made to merge duplicate items.
    
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
  
Figure :need:`feat_req_someipsd_213` shows an example SOME/IP-SD PDU.
    
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
  
Using the previously specified header format, different entries and messages consisting of one or more entries can be built. The specific entries and their header layouts are explained in the following sections.
    
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
  
Entries concerned with services shall be based on the Service Entry Type Format as specified in :need:`feat_req_someipsd_47`.
    
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
  
The Find Service entry type shall be used for finding service instances and shall only be sent if the current state of a service is unknown (no current Service Offer was received and is still valid).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_239
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Find Service entries shall set the entry fields in the following way:
    
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
  
* Instance ID shall be set to 0xFFFF, if all service instances shall be returned. It shall be set to the Instance ID of a specific service instance, if just a single service instance shall be returned.
    
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
  
* TTL shall be set to the lifetime of the Find Service entry. After this lifetime the Find Service entry shall be considered not existing.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_264
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Find Service entry shall be considered valid until the next reboot.
    
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
  
The Offer Service entry type shall be used to offer a service to other communication partners.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_253
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Offer Service entries shall set the entry fields in the following way:
    
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
  
* Service ID shall be set to the Service ID of the service instance that is offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_257
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Instance ID shall be set to the Instance ID of the service instance that is offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_258
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to the Major Version of the service instance that is offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_259
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Minor Version shall be set to the Minor Version of the service instance that is offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_260
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* TTL shall be set to the lifetime of the service instance that is offered. After this lifetime the service instance shall be considered as not offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_266
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If set to 0xFFFFFF, the Offer Service entry shall be considered valid until the next reboot.
    
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
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_681
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Offer Service entries shall always reference at least an IPv4 or IPv6 Endpoint Option to signal how the service is reachable.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_756
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For each Transport Layer Protocol needed for the service (i.e. UDP and/or TCP) an IPv4 Endpoint option shall be added if IPv4 is supported.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_757
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For each Transport Layer Protocol needed for the service (i.e. UDP and/or TCP) an IPv6 Endpoint option shall be added if IPv6 is supported.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_858
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The IP addresses and port numbers of the Endpoint Options shall also be used for transporting events and notification events:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_758
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In the case of UDP this information is used for the source address and the source port of the events and notification events.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_762
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In the case of TCP this is the IP address and port the client needs to open a TCP connection to in order to receive events using TCP.
    
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
  
The Stop Offer Service entry type shall be used to stop offering service instances.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_262
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Offer Service entries shall set the entry fields exactly like the Offer Service entry they are stopping, except:
    
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
  
Entries concerned with services follow the Eventgroup Entry Type Format as specified in :need:`feat_req_someipsd_109`.
    
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
  
The Subscribe Eventgroup entry type shall be used to subscribe to an eventgroup. This is considered comparable to the Request Service entry type.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_322
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup entries shall set the entry fields in the following way:
    
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
    :id: feat_req_someipsd_718
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Major Version shall be set to the Major Version of the service instance of the eventgroup subscribed to.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_719
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Eventgroup ID shall be set to the Eventgroup ID of the eventgroup subscribed to.
    
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
  
* If set to 0xFFFFFF, the Subscribe Eventgroup entry shall be considered valid until the next reboot.
    
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
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_682
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup entries shall reference one or two IPv4 and/or one or two IPv6 Endpoint Options (one for UDP, one for TCP).
    
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
  
The Stop Subscribe Eventgroup entry type shall be used to stop subscribing to eventgroups.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_333
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Stop Subscribe Eventgroup entries shall set the entry fields exactly like the Subscribe Eventgroup entry they are stopping, except:

    
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
    
.. heading:: Subscribe Eventgroup Acknowledgement (Subscribe Eventgroup Ack) Entry
    :id: feat_req_someipsd_612
    :layout: focus
    :style: clean

Subscribe Eventgroup Acknowledgement (Subscribe Eventgroup Ack) Entry
--------------------------------------------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_613
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Subscribe Eventgroup Acknowledgment entry type shall be used to indicate that Subscribe Eventgroup entry was accepted.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_614
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup Acknowledgment entries shall set the entry fields in the following way:
    
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
  
* Service ID, Instance ID, Major Version, Eventgroup ID, TTL, and Reserved shall be the same value as in the Subscribe that is being answered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_763
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup Ack entries referencing events and notification events that are transported via multicast shall reference an IPv4 Multicast Option and/or and IPv6 Multicast Option. The Multicast Options state to which Multicast address and port the events and notification events will be sent to.
    
.. heading:: Subscribe Eventgroup Negative Acknowledgement (Subscribe Eventgroup Nack) Entry
    :id: feat_req_someipsd_617
    :layout: focus
    :style: clean

Subscribe Eventgroup Negative Acknowledgement (Subscribe Eventgroup Nack) Entry
------------------------------------------------------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someipsd_618
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Subscribe Eventgroup Negative Acknowledgment entry type shall be used to indicate that Subscribe Eventgroup entry was NOT accepted.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1137
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Reasons to not accept an Subscribe Eventgroup include (but are not limited to):

* Combination of Service ID, Instance ID, Eventgroup ID, and Major Version is unknown
* Required TCP-connection was not opened by client
* Problems with the references options occurred
* Resource problems at the Server
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_619
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup Negative Acknowledgment entries shall set the entry fields in the following way:
    
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
  
* Service ID, Instance ID, Major Version, Eventgroup ID, and Reserved shall be the same value as in the subscribe that is being answered.
    
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
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_869
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When the client receives a Subscribe Eventgroup Nack as answer on a Subscribe Eventgroup for which a TCP connection is required, the client shall check the TCP connection and shall restart the TCP connection if needed.

Note: Checking the TCP connection may involve a TCP Keep Alive or a SOME/IP Magic Cookie Message.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_870
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Rationale for :need:`feat_req_someipsd_869`:

The server might have lost the TCP connection and the client has not.

Checking the TCP connection might include the following:

* Checking whether data is received for e.g. other Eventgroups.
* Sending out a Magic Cookie message and waiting for the TCP ACK.
* Reestablishing the TCP connection.
    
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
  
For each Service Instance or Eventgroup the Service Discovery shall have at least these three phases in regard to sending entries:
    
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
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_864
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
An actual implemented state machine will need more than just states for these three phases. E.g. local services can be still down and remote services can be already known (no finds needed anymore).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_72
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
As soon as the system has started and the link on a interface needed for a Service Instance is up (server) or requested (client), the service discovery enters the Initial Wait Phase for this service instance.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_773
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Systems has started means here the needed applications and possible external sensors and actuators as well. Basically the functionality needed by this service instance has to be ready to offer a service and finding a service makes only sense after some application already needs it.
    
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
    :id: feat_req_someipsd_836
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall also pack entries together, when no random delay is involved. For example shall all Subscribe Eventgroup entries of a message be answered together in one message.
    
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
  
After each message sent in the Repetition Phase the delay is doubled.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_73
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall send out only up to REPETITIONS_MAX entries during the Repetition Phase.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_867
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Sending Find entries shall be stopped after receiving the corresponding Offer entries by jumping to the Main Phase in which no Find entries are sent.
    
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
    :id: feat_req_someipsd_79
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In the Main Phase Offer Messages shall be sent cyclically if a CYCLIC_OFFER_DELAY is configured.
    
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
    :id: feat_req_someipsd_866
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For Find entries (Find Service and Find Eventgroup) no cyclic messages are allowed in Main Phase.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_631
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Requests/Subscriptions entries shall not be triggered cyclically but shall be triggered by Offer entries, which are sent cyclically.
    
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
* Send message (Find Service and Offer Service entries)

Repetition Phase (REPETITIONS_BASE_DELAY=100ms, REPETITIONS_MAX=2):

* Wait 2^0*100ms
* Send message (Find Service and Offer Service entries)
* Wait 2^1*100ms
* Send message (Find Service and Offer Service entries)
* Wait 2^2*100ms

Main Phase (as long message is active and CYCLIC_OFFER_DELAY is defined):

* Send message (Offer Service entries)
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
  
The Service Discovery shall delay answers to entries that were transported in a multicast/broadcast SOME/IP-SD message using the configuration item REQUEST_RESPONSE_DELAY.

This applies to Find Service entries.

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_766
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The REQUEST_RESPONSE_DELAY shall also apply to unicast messages triggered by multicast messages (e.g. Subscribe Eventgroup after Offer Service).
    
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
    :id: feat_req_someipsd_824
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For basic implementations all Find Service entries (no matter of the state of the Unicast Flag) shall be answered with Offer Service entries transported using unicast.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_826
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
For optimization purpose the following behaviors shall optionally be supported:
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_89
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Find messages received with the Unicast Flag set to 1 in main phase, shall be answered with a unicast response if the last offer was sent less than 1/2 CYCLIC_OFFER_DELAY ago.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_90
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Find messages received with the Unicast Flag set to 1 in main phase, shall be answered with a multicast response if the last offer was sent 1/2 CYCLIC_OFFER_DELAY or longer ago.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_91
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Find messages received with Unicast Flag set to 0 (multicast), shall be answered with a multicast response. (Note: this was only needed in earlier migration scenarios and will go away in the future).
    
.. heading:: Shutdown Behavior
    :id: feat_req_someipsd_819
    :layout: focus
    :style: clean

Shutdown Behavior
================= 

.. feat_req:: 🎯
    :id: feat_req_someipsd_820
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When a server service instance of an ECU is being stopped, a Stop Offer Service entry shall be sent out.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_830
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When a server sends out a Stop Offer Service entry all subscriptions for this service instance shall be deleted on the server side.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_831
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When a client receives a Stop Offer Service entry, all subscriptions for this service instance shall be deleted on the client side.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_834
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When a client receives a Stop Offer Service entry, the client shall not send out Find Service entries but wait for Offer Service entry or change of status (application, network management, Ethernet link, or similar).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_822
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When a client service instance of an ECU is being stopped (i.e. the service instance is released), the SD shall send out Stop Subscribe Eventgroup entries for all subscribed Eventgroups.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_821
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When the whole ECUs is being shut down Stop Offer Service entries shall be sent out for all service entries and Stop Subscribe Eventgroup entries for Eventgroups.
    
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
  
SOME/IP Service State Machine Server

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_629.py

    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_630
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP Service State Machine Client

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_630.py

    
.. heading:: Error Handling
    :id: feat_req_someipsd_1162
    :layout: focus
    :style: clean

Error Handling
============== 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1164
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Figure :need:`feat_req_someipsd_1163` shows an simplified for the error handling of incoming SOME/IP-SD messages.

The following steps are taken:

* Check that at least enough bytes for an empty SOME/IP-SD message are present.
* For each entry that can be parsed:
* Check if the Service ID is known
* Check if the Instance ID of this Service ID is known
* Check if the Major Version of this Service Instance is known
* Check if the Eventgroup ID of the Service Instance with Major Version is known (only applicable for eventgroup entries)
* Check if the referenced Options exist in the options array and are syntactically ok
* Check if the TCP connection is already present (only applicable, if TCP is configured for Eventgroup and Subscribe Eventgroup entry was received)
* Check if enough resources are left (e.g. Socket Connections)
* If any of these check fails, you need to:
* Answer with an Subscribe Eventgroup NACK, if the original entry was an Subscribe Eventgroup entry :need:`feat_req_someipsd_1137`.
* Ignore, if the original entry was not a Subscribe Eventgroup entry

    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1163
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Error Handling

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_1163.py

    
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
  
Besides SOME/IP other communication protocols are used within the vehicle; e.g. for Network Management, Diagnosis, or Flash Updates. Such communication protocols might need to communicate a service instance or have eventgroups as well.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_500
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
For Non-SOME/IP protocols a special Service ID shall be used and further information shall be added using the configuration option:

* Service ID shall be set to 0xFFFE (reserved)
* Instance ID shall be used as described for SOME/IP services and eventgroups.
* The Configuration Option shall be added and shall contain at least a entry with key "otherserv" and a configurable non-empty value that is determined by the OEM.
    
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
  
For Find Service/Offer Service/Request Service entries the otherserv-String shall be used when announcing non-SOME/IP service instances.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_501
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Example for valid otherserv-string: "otherserv=internaldiag".

Example for an invalid otherserv-string: "otherserv".
Example for an invalid otherserv-string: "otherserv=".
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_575
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP-SD Example PDU for Non-SOME/IP-SD

.. bitfield_directive:: images/bit_field/feat_req_someipsd_575.json

    
.. heading:: Publish/Subscribe with SOME/IP and SOME/IP-SD
    :id: feat_req_someipsd_137
    :layout: focus
    :style: clean

Publish/Subscribe with SOME/IP and SOME/IP-SD
********************************************* 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_419
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In contrast to the SOME/IP request/response mechanism there are cases in which a client requires a set of parameters from a server, but does not want to request that information each time it is required. These are called notifications and concern events and fields.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_422
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
All clients needing events and/or notification events shall register using the SOME/IP-SD at run-time with a server.
    
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
  
With the SOME/IP-SD entry Offer Service the server offers to push notifications to clients; thus, it shall be used as trigger for Subscriptions.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_429
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When a server of a notification service starts up (e.g. after reset), it shall send a SOME/IP-SD Offer Service into the network to discover all instances interested in the events and fields offered.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_430
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Each client in SD based notification implements the specific service-interfaces for the notification they wish to receive and signal their wish of receiving such notifications using the SOME/IP-SD Subscribe Eventgroup entries.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_431
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Each client shall respond to a SOME/IP-SD Offer Service entry from the server with a SOME/IP-SD Subscribe Eventgroup entry as long as the client is still interested in receiving the notifications/events of this eventgroup.

If the client is able to reliably detect the reboot of the server using the SOME/IP-SD messages reboot flag, the client shall only answer Offer Service messages after the server reboots, if configured to do so (TTL set to maximum value). The client shall make sure that this works reliable even when the SOME/IP-SD messages of the server are lost.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1168
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the client subscribes to two or more eventgroups including one or more identical events or fields, the server shall not send duplicated events or notification events for the field. This does mean regular events and not initial events.

See :need:`feat_req_someipsd_1166` and :need:`feat_req_someipsd_1167`.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_632
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe with link loss at client (figure ignoring timings)

.. plantuml:: images/plantuml/feat_req_someipsd_632.puml

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_432
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The server sending Offer Service entries as implicit Publishes has to keep state of Subscribe Eventgroup messages for this eventgroup instance in order to know if notifications/events have to be sent.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_433
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A client shall deregister from a server by sending a SOME/IP-SD Subscribe Eventgroup message with TTL=0 (Stop Subscribe Eventgroup).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_634
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe Registration/Deregistration behavior (figure ignoring timings)

.. plantuml:: images/plantuml/feat_req_someipsd_634.puml

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_435
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The SOME/IP-SD on the server shall delete the subscription, if a relevant SOME/IP error is received after sending a event or notification event.

The error includes but is not limited to not being able to reach the communication partner and errors of the TCP connection.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_437
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the server loses its link on the relevant Ethernet interface, it SHALL delete all the registered notifications and close the TCP connection for those notifications as well.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_436
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the Ethernet link status of the server becomes up again, it shall trigger a SOME/IP-SD Offer Service message.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_633
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe with link loss at server (figure ignoring timings)

.. plantuml:: images/plantuml/feat_req_someipsd_633.puml

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_439
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After having not received a notification/event of an eventgroup subscribed to for a certain timeout the ECU shall send a new Subscribe Eventgroup entry. The timeout shall be configurable for each eventgroup.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_832
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
This timeout feature might be based on cyclic messages or message protected by Alive Counters (functional safety).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_440
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A link-up event on the clients Ethernet link shall start the Initial Wait Phase (consider UDP-NM and others). SOME/IP-SD Subscribe Eventgroup entry shall be sent out as described above.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_767
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The client shall open a TCP connection to the server before sending the Subscribe Eventgroup entry, if reliable events and notification events exist in the interface definition (e.g. FIBEX or ARXML).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_441
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
After a client has sent a Subscribe Eventgroup entry the server shall send a Subscribe Eventgroup Ack entry considering the specified delay behavior.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_844
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The client shall wait for the Subscribe Eventgroup Ack entry acknowledging an Subscribe Eventgroup entry. If this Subscribe Eventgroup Ack entry does not arrive before the next Subscribe Eventgroup entry is sent, the client shall do the following: send a Stop Subscribe Eventgroup entry and a Subscribe Eventgroup entry in the SOME/IP-SD message the Subscribe Eventgroup entry would have been sent with.

Note: This behavior exists to cope with short durations of communication loss. The receiver of a Stop Subscribe Eventgroup and Subscribe Eventgroup combination would sent out Initial Events to lower the effects of the loss of messages.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_691
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the initial value is of concern - i.e. for fields - the server shall immediately send the first notification/event; i.e. event on a new subscription. The client shall repeat the Subscribe Eventgroup entry, if it did not receive the notification/event in a configurable timeout.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_833
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
This means:

* It is not allowed to send initial values of events upon subscriptions (pure event and not field).
* The event messages of field notifiers shall be sent on subscriptions (field and not pure event).
* If a subscription was already valid and is updated by a Subscribe Eventgroup entry, no initial events shall be sent.
* Receiving Stop Subscribe / Subscribe combinations trigger initial events of field notifiers.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1167
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If a client subscribes to different eventgroups of the same Service Instance that all include the same field in different SOME/IP-SD messages, the Server shall send out the initial events for this field for every subscription separately.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1166
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If a client subscribes to different eventgroups of the same Service Instance that all include the same field in the same SOME/IP-SD message, the Server may choose to not send out the initial event for this field more than once.

Note: This means the Server can optimize by sending the initial events only once, if supported by its architecture.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_625
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe State Diagram (server behavior for unicast eventgroups).

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_625.py

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_626
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe State Diagram (server behavior for multicast eventgroups).

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_626.py

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_823
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe State Diagram (server behavior for adaptive unicast/multicast eventgroups).

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_823.py

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_442
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe State Diagram (overall behavior).

.. drawsvg_directive:: images/drawsvg/feat_req_someipsd_442.py

    
.. feat_req:: 🎯
    :id: feat_req_someipsd_444
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
An implicit registration of a client to receive notifications from a server shall be supported. Meaning the mechanism is pre-configured.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_445
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
To allow for cleanup of stale client registrations (to avoid that the list of listeners fills over time), a cleanup mechanism is required.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_818
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following entries shall be transported by unicast only:

* Subscribe Eventgroup
* Stop Subscribe Eventgroup
* Subscribe Eventgroup Ack
* Subscribe Eventgroup Nack
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_828
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
When sending a Subscribe Eventgroup entry as reaction of receiving an Offer Service entry, the timer controlling cyclic Subscribe Eventgroups entries shall be reset.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_829
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If no cyclic Subscribe Eventgroups are configured, the timer for cyclic Subscribe Eventgroups stays turned off.
    
.. heading:: Endpoint Handling for Services and Events
    :id: feat_req_someipsd_776
    :layout: focus
    :style: clean

Endpoint Handling for Services and Events
***************************************** 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_777
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
This section describes how the Endpoints encoded in the Endpoint and Multicast Options shall be set and used.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_778
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Discovery shall overwrite IP Addresses and Port Numbers with those transported in Endpoint and Multicast Options if the statically configured values are different from those in these options.
    
.. heading:: Service Endpoints
    :id: feat_req_someipsd_784
    :layout: focus
    :style: clean

Service Endpoints
================= 

.. feat_req:: 🎯
    :id: feat_req_someipsd_780
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Offer Service entries shall reference up to 1 UDP Endpoint Option and up to 1 TCP Endpoint Option. Both shall be of the same version Internet Protocol (IPv4 or IPv6).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_779
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The referenced Endpoint Options of the Offer Service entries denote the IP Address and Port Numbers the service instance is reachable at the server.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_781
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The referenced Endpoint Options of the Offer Service entries also denote the IP Address and Port Numbers the service instance sends the events from.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_797
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Events of this service instance shall not be sent from any other Endpoints than those given in the Endpoint Options of the Offer Service entries.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_782
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If an ECU offers multiple service instances, SOME/IP messages of these service instances shall be differentiated by the information transported in the Endpoint Options referenced by the Offer Service entries.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_783
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Therefore transporting an Instance ID in the SOME/IP header is not required.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_877
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A sender shall not reference Endpoint Options nor Multicast Options in a Find Service Entry.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_878
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A receiver shall ignore Endpoint Options and Multicast Options in a Find Service Entry.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_879
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Other Options (neither Endpoint nor Multicast Options), shall still be allowed to be used in a Find Service Entry.
    
.. heading:: Eventgroup Endpoints
    :id: feat_req_someipsd_785
    :layout: focus
    :style: clean

Eventgroup Endpoints
==================== 

.. feat_req:: 🎯
    :id: feat_req_someipsd_786
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup entries shall reference up to 1 UDP Endpoint Option and up to 1 TCP Endpoint Option for the Internet Protocol used (IPv4 or IPv6).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_787
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Endpoint Options referenced in the Subscribe Eventgroup entries is also used to send unicast UDP or TCP SOME/IP events for this Service Instance.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_798
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Thus the Endpoint Options referenced in the Subscribe Eventgroup entries are the IP Address and the Port Numbers on the client side.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_788
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
TCP events are transported using the TCP connection the client has opened to the server before sending the Subscribe Eventgroup entry. See :need:`feat_req_someipsd_752`.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_793
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The initial events shall be transported using unicast from Server to Client.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_789
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Subscribe Eventgroup Ack entries shall reference up to 1 Multicast Option for the Internet Protocol used (IPv4 or IPv6).
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_790
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The Multicast Option shall be set to UDP as transport protocol.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_791
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The client shall open the Endpoint specified in the Multicast Option referenced by the Subscribe Eventgroup Ack entry as fast as possible to not miss multicast events.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_792
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
If the server has to send multicast events very shortly (configurable time < 5 ms) after sending the Subscribe Eventgroup Ack entry, the server shall try to delay these events, so that the client is not missing it. If this event was sent as multicast anyhow, the server shall send this event using unicast as well.
    
.. heading:: Example
    :id: feat_req_someipsd_794
    :layout: focus
    :style: clean

Example
======= 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_796
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Figure :need:`feat_req_someipsd_795` shows an example with the different Endpoint and a Multicast Option:

* The Server offers the Service Instance on Server UDP-Endpoint SU and Server TCP-Endpoint ST
* The Client opens a TCP connection
* The Client sends a Subscribe Eventgroup entry with Client UDP-Endpoint CU (unicast) and a Client TCP-Endpoint CT.
* The Server answers with a Subscribe Eventgroup Ack entry with Multicast MU

Then the following operations happen:

* The Clients calls a method on the Server
* Request is sent from CU to SU and Response from SU to CU
* For TCP this would be: Request dyn to ST and Response from ST to CT
* The Server sends a Unicast UDP Event: SU to CU
* The Server sends a Unicast TCP Event: ST to CT
* The Server sends a Multicast UDP Event: SU to MU

Keep in mind that Multicast Endpoints use a Multicast IP Address on the receiver side, i.e. the client, and TCP cannot be used for Multicast communication.

 
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_795
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Publish/Subscribe Example for Endpoint Options and the usage of ports.

.. plantuml:: images/plantuml/feat_req_someipsd_795.puml

    
.. heading:: Security Considerations
    :id: feat_req_someipsd_1134
    :layout: focus
    :style: clean

Security Considerations
======================= 

.. feat_req:: 🎯
    :id: feat_req_someipsd_1135
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
A SOME/IP-SD implementation shall always check that the IP Addresses received in Endpoint options and SD Endpoint options are topological correct (reference IP Addresses in the IP subnet for which SOME/IP-SD is used) and shall ignore IP Addresses that are not topological correct as well as the entries referencing those options.

Note: This means that only Clients and Servers in the same subset are accessible.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_1136
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
An example for checking the IP Addresses (Endpoint-IP) for topological correctness is:
SOME/IP-SD-IP-Address AND Netmask = Endpoint-IP AND Netmask.
    
.. heading:: Mandatory Feature Set and Basic Behavior
    :id: feat_req_someipsd_806
    :layout: focus
    :style: clean

Mandatory Feature Set and Basic Behavior
**************************************** 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_807
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In this section the mandatory feature set of the Service Discovery and the relevant configuration constraints are discussed. This allow for bare minimum implementations without optional or informational features that might not be required for current use cases. 
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_815
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
The following information is defined as compliance check list(s). If a feature is not implemented, the implementation is considered not to comply to SOME/IP-SDs basic feature set.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_808
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following entry types shall be implemented:

* Find Service
* Offer Service
* Stop Offer Service
* Subscribe Eventgroup
* Stop Subscribe Eventgroup
* Subscribe Eventgroup Ack
* Subscribe Eventgroup Nack
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_809
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following option types shall be implemented, when IPv4 is required:

* IPv4 Endpoint Option
* IPv4 Multicast Option
* Configuration Option
* IPv4 SD Endpoint Option (receiving at least)
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_810
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following option types shall be implemented, if IPv6 is required:

* IPv6 Endpoint Option
* IPv6 Multicast Option
* Configuration Option
* IPv6 SD Endpoint Option (receiving at least)
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_857
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following option types shall be implemented, if non-SOME/IP services or additional configuration parameters are required:

* Configuration Option
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_811
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following behaviors/reactions shall be implemented on the Server side:

* The Server shall offer services including the Initial Wait Phase, the Repetition Phase, and the Main Phase depending on the configuration.
* The Server shall offer services using Multicast (Repetition Phase and Main Phase).
* The Server does not need to answer a Find Service in the Repetition Phase.
* The Server shall answer a Find Service in the Main Phase with an Offer Service using Unicast (no optimization based on unicast flag as in :need:`feat_req_someipsd_826`).
* The Server shall send a Stop Offer Service when shutting down.
* The Server shall receive a Subscribe Eventgroup as well as a Stop Subscribe Eventgroup and react according to this specification.
* The Server shall send a Subscribe Eventgroup Ack and Subscribe Eventgroup Nack using unicast.
* The Server shall support controlling the sending (i.e. fan out) of SOME/IP event messages based on the subscriptions of SOME/IP-SD. This might include sending events based on Multicast.
* The Server shall support the triggering of initial SOME/IP event messages.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_812
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following behaviors/reactions shall be implemented on the Client side:

* The Client shall find services using a Find Service entry and Multicast only in the repetition phase.
* The Client shall stop finding a service if the regular Offer Service arrives.
* The Client shall react to the Servers Offer Service with an unicast SD message that includes all Subscribe Eventgroups of the services offered in the message of the Server that the client currently wants to subscribe to.
* The Client shall interpret and react to the Subscribe Eventgroup Ack and Subscribe Eventgroup Nack as specified in this document.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_816
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The following behavior and configuration constraints shall be supported by the Client:

* The Client shall even handle Eventgroups if only the TTL of the SD Timings is specified. This means that of all the timings for the Initial Wait Phase, the Repetition Phase, and the Main Phase only TTL is configured. This means the client shall only react on the Offer Service by the Server.
* The Client shall answer to an Offer Service with a Subscribe Eventgroup even without configuration of the Request-Response-Delay, meaning it does not wait but answer instantaneously.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_813
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The Client and Server shall implement the Reboot Detection as specified in this document and react accordingly. This includes but is not limited to:

* Setting Session ID and Reboot Flag according to this specification.
* Keeping a Session ID counter only used for sending Multicast SD messages.
* Keeping Session ID counters for every Unicast relation for sending Unicast SD messages.
* Understanding Session ID and Reboot Flag according to this specification.
* Keeping a Multicast Session ID counter per ECU that exchanges Multicast SD messages with this ECU.
* Keeping a Unicast Session ID counter per ECU that exchanges Unicast SD messages with this ECU.
* Detecting reboot based on this specification and reaction accordingly.
* Correctly interpreting the IPv4 and IPv6 SD Endpoint Options in regard to Reboot Detection.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_814
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The Client and Server shall implement the "Endpoint Handling for Service and Events". This includes but is not limited to:

* Adding 1 Endpoint Option UDP to an Offer Services if UDP is needed.
* Adding 1 Endpoint Option TCP to an Offer Service if TCP is needed.
* Adding 1 Endpoint Option UDP to Subscribe Eventgroup if events over UDP are required.
* Adding 1 Endpoint Option TCP to Subscribe Eventgroup if events over TCP are required.
* Adding 1 Multicast Option UDP to Subscribe Eventgroup Ack if multicast events are required.
* Understanding and acting according to the Endpoint and Multicast Options transported as described above.
* Overwriting preconfigured values (e.g. IP Addresses and Ports) with the information of these Endpoint and Multicast Options.
* Interpreting incoming IPv4 and IPv6 Endpoint Options as SD endpoints instead of the Address and Port number in the outer layers.
    
.. feat_req:: 🎯
    :id: feat_req_someipsd_1157
    :reqtype: Requirement
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The Client and Server shall implement the "SD Endpoint option":

* Interpreting incoming IPv4 and IPv6 Endpoint Options as SD endpoints instead of the Address and Port number in the outer layers.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_946
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Allowed SOME/IP-SD Option types in relation to Entry types.
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier
      
      * -
        - Endpoint Option
        - Multicast Option
        - Configuration Option
        - Load Balancing Option
        - Protection Option
      * - **FindService** 
        - 0 
        - 0 
        - 0-1 
        - 0-1 
        - 0-1
      * - **OfferService** 
        - 1-2 
        - 0 
        - 0-1 
        - 0-1 
        - 0-1
      * - **StopOfferService** 
        - 1-2 
        - 0 
        - 0-1 
        - 0-1
        - 0-1
      * - **SubscribeEventgroup** 
        - 1-2 
        - 0 
        - 0-1 
        - 0-1
        - 0-1
      * - **StopSubscribeEventgroup** 
        - 1-2 
        - 0 
        - 0-1 
        - 0-1
        - 0-1
      * - **SubscribeEventgroupAck**
        - 0 
        - 0-1 
        - 0-1 
        - 0-1
        - 0-1
      * - **SubscribeEventgroupNack**
        - 0 
        - 0 
        - 0-1 
        - 0-1
        - 0-1

.. heading:: SOME/IP-SD Mechanisms and Errors
    :id: feat_req_someipsd_837
    :layout: focus
    :style: clean

SOME/IP-SD Mechanisms and Errors
******************************** 

.. feat_req:: ⓘ 
    :id: feat_req_someipsd_838
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
In this section SOME/IP-SD in cases of errors (e.g. lost or corrupted packets) is discussed. This is also understood as rationale for the mechanisms used and the configuration possible.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_842
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Soft State Protocol:

SOME/IP-SD was designed as soft state protocol, that means that entries come with a lifetime and need to be refreshed to stay valid (setting the TTL to the maximum value shall turn this off).

Using cyclic Offer Service entries and the TTL as aging mechanism SOME/IP-SD shall cope with many different cases of errors. Some examples:

* If a client or server leaves without sending a Stop entry or this Stop entry got lost, the system will fix itself after the TTL expiration.
* If an Offer Service entry does not arrive because the packet got lost, the system will tolerate this based on the value of the TTL.

Example configuration parameter for fast healing: cyclic delays 1s and TTL 3s.

    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_840
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Initial Wait Phase:

The Initial Wait Phase was introduced for two reasons: deskewing events of starting ECUs to avoid traffic bursts and allowing ECUs to collect multiple entries in SD messages.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_839
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Repetition Phase:

The Repetition Phase was introduced to allow for fast synchronization of clients and servers. If the clients startup later, it will find the server very fast. And if the server starts up later, the client is found very fast. The Repetition Phase increases the time between two messages exponentially to avoid that overload situations keep the system from synchronization.

An example configuration could be REPETITIONS_BASE_DELAY=30ms and REPETITIONS_MAX=3.
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_841
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Main Phase:

In the Main Phase the SD tries to stabilize the state and thus decreases the rate of packets by sending no Find Services anymore and only offers in the cyclic interval (e.g. every 1s).
    
.. feat_req:: ⓘ 
    :id: feat_req_someipsd_843
    :reqtype: Information
    :security: NO
    :safety: QM
    :satisfies: 
    :status: valid
    :collapse: True
  
Request-Response-Delay:

SOME/IP-SD shall allow to be configured to delay the answer to entries in multicast messages by the Request-Response-Delay (in FIBEX called Query-Response-Delay). This is useful in large systems with many ECUs. When sending a SD message with many entries in it, a lot of answers from different ECUs arrive at the same time and put a large stress on the ECU receiving all these answers.
    