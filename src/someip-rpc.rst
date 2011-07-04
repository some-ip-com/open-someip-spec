
:orphan:

.. This file is part of the Open SOME/IP Specification.
.. 
.. Copyright (c) 2025 Technica Engineering GmbH
.. 
.. This file is licensed under the SOME/IP Community Specification License.
.. You can find a copy of this license in the Open SOME/IP Specification repository.
..
.. see https://some-ip.com and https://github.com/some-ip-com/open-someip-spec/

.. ##############################
.. SOME/IP Protocol Specification
.. ##############################


.. heading:: Introduction
    :id: feat_req_someip_2
    :layout: focus
    :style: clean

.. rst-class:: break_before

Introduction
############ 

.. feat_req:: ⓘ 
    :id: feat_req_someip_3
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
This document specifies the Scalable service-Oriented middlewarE over IP (SOME/IP) – an automotive/embedded RPC mechanism and the underlying serialization / wire format.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_4
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The basic motivation to specify “yet another RPC-Mechanism” instead of using an existing infrastructure/technology is the goal to have a technology that:

* Fulfills the hard requirements regarding resource consumption in an embedded world
* Is compatible through as many use-cases and communication partners as possible
* Is compatible with AUTOSAR at least on the wire-format level; i.e. can communicate with PDUs AUTOSAR can receive and send without modification to the AUTOSAR standard.
* Provides the features required by automotive use-cases
* Is scalable from tiny to large platforms
* Can be implemented on different operating system (i.e. AUTOSAR, GENIVI, and OSEK) and even embedded devices without operating system
    
.. heading:: Definition of terms
    :id: feat_req_someip_14
    :layout: focus
    :style: clean

Definition of terms
******************* 

.. feat_req:: ⓘ 
    :id: feat_req_someip_15
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Method – a method, procedure, function, or subroutine that can be called/invoked
* Parameters – input, output, or input/output arguments of a method

  * Input/output arguments are arguments shared for input and output

* Remote Procedure Call (RPC) – a method call from one ECU to another that is transmitted using messages
* Request – a message of the client to the server invoking a method
* Response – a message of the server to the client transporting results of a method invocation
* Request/Response communication – a RPC that consists of request and response
* Fire&Forget communication – a RPC call that consists only of a request message
* Event – a Fire&Forget callback that is only invoked on changes or cyclic and is sent from Server to Client
* Field – a representation of a remote property, which has up to one getter, up to one setter, and up to one notifier.
* Getter – a Request/Response call that allows read access to a field.

  * Rationale: The getter needs to return a value; thus, it needs to be a request/response call. 

* Setter – a Request/Response call that allows write access to a field.

  * Rationale: The setter is a request/response call as well in order for the client to know whether the setter-operation succeeded.

* Notifier – sends out events with a new value on change of the value of the field
* Service – a logical combination of zero or more methods, zero or more events, and zero or more fields (empty service is allowed)
* Eventgroup – a logical grouping of events and notification events inside a service in order to allow subscription
* Service Interface – the formal specification of the service including its methods, events, and fields
* Service Instance – software implementation of the software interface, which can exist more than once in the vehicle and more than once on an ECU
* Server – The ECU offering a service instance shall be called server in the context of this service instance.
* Client – The ECU using the service instance of a server shall be called client in the context of this service instance.
* Union or Variant – a data structure that can dynamically assume different data types
    
.. heading:: Definition of Identifiers
    :id: feat_req_someip_534
    :layout: focus
    :style: clean

Definition of Identifiers
========================= 

.. feat_req:: 🎯
    :id: feat_req_someip_538
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A service shall be identified using the Service-ID.
    
.. feat_req:: 🎯
    :id: feat_req_someip_539
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Service-IDs shall be of type 16 bit length unsigned integer (uint16).
    
.. feat_req:: 🎯
    :id: feat_req_someip_624
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service-ID of 0xFFFE shall be used to encode non-SOME/IP services.
    
.. feat_req:: 🎯
    :id: feat_req_someip_627
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service-ID of 0x0000 and 0xFFFF shall be reserved for special cases. A reference table is found at the end of this document in :need:`feat_req_someipids_505`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_541
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Different services within the same vehicle shall have different Service-IDs.
    
.. feat_req:: 🎯
    :id: feat_req_someip_542
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A service instance shall be identified using the Service-Instance-ID.
    
.. feat_req:: 🎯
    :id: feat_req_someip_543
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Service-Instance-IDs shall be of type 16 bit length unsigned integer (uint16).
    
.. feat_req:: 🎯
    :id: feat_req_someip_579
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service-Instance-IDs of 0x0000 and 0xFFFF shall not be used for a service, since 0x0000 is used to describe no service instance and 0xFFFF is used to describe all service instances.
    
.. feat_req:: 🎯
    :id: feat_req_someip_544
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Different service instances within the same vehicle shall have different Service-Instance-IDs.
    
.. feat_req:: 🎯
    :id: feat_req_someip_625
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Methods and events shall be identified inside a service using a 16bit Method-ID, which may be also called Event-ID for events and notifications.
    
.. feat_req:: 🎯
    :id: feat_req_someip_626
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Methods shall use Method-IDs with the highest bit set to 0, while the Method-IDs highest bit shall be set to 1 for events and notifications. This requirement may be overruled by the system department at anytime.
    
.. feat_req:: 🎯
    :id: feat_req_someip_545
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
An event group shall be identified using the Eventgroup-ID.
    
.. feat_req:: 🎯
    :id: feat_req_someip_546
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Eventgroup-IDs shall be of 16 bit length unsigned integer (uint16).
    
.. feat_req:: 🎯
    :id: feat_req_someip_547
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Different event groups within the same vehicle shall have different Eventgroup-IDs.
    
.. heading:: Specification of the SOME/IP on-wire format
    :id: feat_req_someip_29
    :layout: focus
    :style: clean

.. rst-class:: break_before

Specification of the SOME/IP on-wire format
########################################### 

.. feat_req:: 🎯
    :id: feat_req_someip_30
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Serialization describes the way data is represented in protocol data units (PDUs) transported over an IP-based automotive in-vehicle network.
    
.. heading:: Transport Protocol
    :id: feat_req_someip_31
    :layout: focus
    :style: clean

Transport Protocol
****************** 

.. feat_req:: 🎯
    :id: feat_req_someip_32
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP may be transported using UDP or TCP. The port numbers for SOME/IP have to be defined locally from the private port range 49152-65535 until further notice. When used in a vehicle the OEM will specify the ports used in the interface specification.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_33
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
It is recommended to use UDP for as many messages as possible and see TCP as fall-back for message requiring larger size. UDP allows the application to better control the timeouts and behavior when errors occurring.
    
.. heading:: Message Length Limitations
    :id: feat_req_someip_34
    :layout: focus
    :style: clean

Message Length Limitations
========================== 

.. feat_req:: ⓘ 
    :id: feat_req_someip_35
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In combination with regular Ethernet, IPv4 and UDP can transport packets with up to 1472 Bytes of data without fragmentation, while IPv6 uses additional 20 Bytes. Especially for small systems fragmentation shall be avoided, so the SOME/IP header and payload should be of limited length. The possible usage of security protocols further limits the maximal size of SOME/IP messages.
    
.. feat_req:: 🎯
    :id: feat_req_someip_36
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When using UDP as transport protocol SOME/IP messages may use up to 1416 Bytes for the SOME/IP header and payload, so that 1400 Bytes are available for the payload.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_38
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
See also :need:`feat_req_someip_164` for payload length.
    
.. heading:: Endianness
    :id: feat_req_someip_41
    :layout: focus
    :style: clean

Endianness
********** 

.. feat_req:: 🎯
    :id: feat_req_someip_42
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
All RPC-Headers shall be encoded in network byte order (big endian) [RFC 791]. The byte order of the parameters inside the payload shall be defined by the interface definition (i.e. FIBEX) and should be in network byte order when possible and if no other byte order is specified.
    
.. heading:: Header
    :id: feat_req_someip_43
    :layout: focus
    :style: clean

Header
****** 

.. feat_req:: 🎯
    :id: feat_req_someip_44
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For interoperability reasons the header layout shall be identical for all scales of the SOME/IP and is shown in the Figure :need:`feat_req_someip_45`. The fields are presented in transmission order; i.e. the fields on the top left are transmitted first. In the following sections the different header fields and their usage is being described.
    
.. feat_req:: 🎯
    :id: feat_req_someip_45
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP Header

.. bitfield_directive:: images/bit_field/feat_req_someip_45.json

    
.. heading:: IP-Address / port numbers
    :id: feat_req_someip_46
    :layout: focus
    :style: clean

IP-Address / port numbers
========================= 

.. feat_req:: 🎯
    :id: feat_req_someip_47
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Layout in Figure :need:`feat_req_someip_45` shows the basic header layout over IP and the transport protocol used. 
    
.. heading:: Mapping of IP Addresses and Ports
    :id: feat_req_someip_48
    :layout: focus
    :style: clean

Mapping of IP Addresses and Ports
--------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someip_49
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
For the response and error message the IP addresses and port number of the transport protocol shall match the request message. This means:

* Source IP address of response = destination IP address of request.
* Destination IP address of response = source IP address of request.
* Source port of response = destination port of request.
* Destination port of response = source port of request.
* The transport protocol (TCP or UDP) stays the same.
    
.. heading:: Message ID [32 Bit]
    :id: feat_req_someip_55
    :layout: focus
    :style: clean

Message ID [32 Bit]
=================== 

.. feat_req:: 🎯
    :id: feat_req_someip_56
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Message ID is a 32 Bit identifier that is used to dispatch the RPC call to a method of an application and to identify a notification. The Message ID has to uniquely identify a method.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_57
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The assignment of the Message ID is up to the user; however, the Message ID has to be unique for the whole system (i.e. the vehicle). The Message ID can be best compared to a CAN ID and should be handled with a comparable process. The next section describes how structure the Message IDs in order to ease the organization of Message IDs.
    
.. heading:: Structure of the Message ID
    :id: feat_req_someip_58
    :layout: focus
    :style: clean

Structure of the Message ID
--------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someip_59
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In order to structure the different methods and events, they are clustered into services. Services have a set of methods and events as well as a Service ID, which is only used for this service. The events may in addition be clustered into event groups, which simplify the registration of events.
    
.. feat_req:: 🎯
    :id: feat_req_someip_60
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For RPC calls we structure the ID in 2^16 services with 2^15 methods:

.. bitfield_directive:: images/bit_field/feat_req_someip_60.json

    
.. feat_req:: 🎯
    :id: feat_req_someip_66
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
With 16 Bit Service-ID and a 16 Bit Method-ID starting with a 0-Bit, this allows for up to 65536 services with up to 32768 methods each.
    
.. feat_req:: 🎯
    :id: feat_req_someip_67
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Since events (see Notification or Publish/Subscribe) are transported using RPC, the ID space for the events is further structured:

.. bitfield_directive:: images/bit_field/feat_req_someip_67.json

    
.. feat_req:: 🎯
    :id: feat_req_someip_628
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
This means that up to 32768 events or notifications per service are possible.
    
.. heading:: Length [32 Bit]
    :id: feat_req_someip_76
    :layout: focus
    :style: clean

Length [32 Bit]
=============== 

.. feat_req:: 🎯
    :id: feat_req_someip_77
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Length is a field of 32 Bits containing the length in Byte of the payload beginning with the Request ID/Client ID. The Length does not cover the portion of the header including the Message ID and the Length field.
    
.. heading:: Request ID [32 Bit]
    :id: feat_req_someip_78
    :layout: focus
    :style: clean

Request ID [32 Bit]
=================== 

.. feat_req:: 🎯
    :id: feat_req_someip_79
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request ID allows a client to differentiate multiple calls to the same method. Therefore, the Request ID has to be unique for a single client and server combination only. When generating a response message, the server has copy the Request ID from the request to the response message. This allows the client to map a response to the issued request even with more than one request outstanding.
    
.. feat_req:: 🎯
    :id: feat_req_someip_80
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Request IDs might be reused as soon as the response arrived or is not expected to arrive anymore (timeout). In most automotive use cases a very low number of outstanding requests are expected. For small systems without the possibility of parallel requests, the Request ID might always set to the same value.
    
.. heading:: Structure of the Request ID
    :id: feat_req_someip_82
    :layout: focus
    :style: clean

Structure of the Request ID
--------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someip_83
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request ID is constructed of the Client ID and Session ID:

.. bitfield_directive:: images/bit_field/feat_req_someip_83.json

    
.. feat_req:: 🎯
    :id: feat_req_someip_88
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Client ID is the unique identifier for the calling client inside the ECU. The Session ID is a unique identifier chosen by the client for each call. If session handling is not used, the Session ID shall be set to 0x0000.
    
.. heading:: Protocol Version [8 Bit]
    :id: feat_req_someip_89
    :layout: focus
    :style: clean

Protocol Version [8 Bit]
======================== 

.. feat_req:: 🎯
    :id: feat_req_someip_90
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Protocol Version is an 8 Bit field containing the SOME/IP protocol version, which currently shall be set to 0x01.
    
.. heading:: Interface Major Version [8 Bit]
    :id: feat_req_someip_91
    :layout: focus
    :style: clean

Interface Major Version [8 Bit]
=============================== 

.. feat_req:: 🎯
    :id: feat_req_someip_92
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Interface Major Version is an 8 Bit field that contains the Major Version of the Service Interface.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_93
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Rationale: This is required to catch mismatches in Service definitions and allows debugging tools to identify the Service Interface used, if version is used.
    
.. heading:: Message Type [8 Bit]
    :id: feat_req_someip_94
    :layout: focus
    :style: clean

Message Type [8 Bit]
==================== 

.. feat_req:: 🎯
    :id: feat_req_someip_95
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Message Type field is used to differentiate different types of messages and may contain the following values:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      * - Number 
        - Value 
        - Description
      * - 0x00
        - REQUEST
        - A request expecting a response (even void)
      * - 0x01
        - REQUEST_NO_RETURN
        - A fire&forget request
      * - 0x02
        - NOTIFICATION
        - A request of a notification/event callback expecting no response
      * - 0x40
        - REQUEST ACK
        - Acknowledgment for REQUEST (optional)
      * - 0x41
        - REQUEST_NO_RETURN ACK
        - Acknowledgment for REQUEST_NO_RETURN (informational)
      * - 0x42
        - NOTIFICATION ACK
        - ACK Acknowledgment for NOTIFICATION (informational)
      * - 0x80
        - RESPONSE
        - The response message
      * - 0x81
        - ERROR
        - The response containing an error
      * - 0xC0
        - RESPONSE ACK
        - Acknowledgment for RESPONSE (informational)
      * - 0xC1
        - ERROR ACK
        - Acknowledgment for ERROR (informational)

.. feat_req:: 🎯
    :id: feat_req_someip_141
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Regular request (message type 0x00) will be answered by a response (message type 0x80), when no error occurred. If errors occur an error message (message type 0x81) will be sent. It is also possible to send a request that does not have a response message (message type 0x01). For updating values through notification a callback interface exists (message type 0x02).
    
.. feat_req:: 🎯
    :id: feat_req_someip_142
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For all messages an optional acknowledgment (ACK) exists. These can be used in cases that the transport protocol (i.e. UDP) does not acknowledge a received message. ACKs are only transported when the interface specification requires it. Only the usage of the REQUEST_ACK is currently specified in this document. All other ACKs are currently informational and do not need to be implemented.
    
.. heading:: Return Code [8 Bit]
    :id: feat_req_someip_143
    :layout: focus
    :style: clean

Return Code [8 Bit]
=================== 

.. feat_req:: 🎯
    :id: feat_req_someip_144
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Return Code is used to signal whether a request was successfully been processed. For simplification of the header layout, every message transports the field Return Code.

The Return Codes are specified in detail in :need:`feat_req_someip_371`.

Messages of Type REQUEST, REQUEST_NO_RETURN, and Notification have to set the Return Code to 0x00 (E_OK). The allowed Return Codes for specific message types are:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      * - Message Type 
        - Allowed Return Codes
      * - REQUEST
        - N/A set to 0x00 (E_OK)
      * - REQUEST_NO_RETURN 
        - N/A set to 0x00 (E_OK)
      * - NOTIFICATION
        - N/A set to 0x00 (E_OK)
      * - RESPONSE
        - See Return Codes in [:need:`feat_req_someip_371`]
      * - ERROR
        - See Return Codes in [:need:`feat_req_someip_371`]. Shall not be 0x00 (E_OK).

.. heading:: Payload [variable size]
    :id: feat_req_someip_164
    :layout: focus
    :style: clean

Payload [variable size]
======================= 

.. feat_req:: 🎯
    :id: feat_req_someip_165
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In the payload field the parameters are carried. The serialization of the parameters will be specified in the following section.
    
.. feat_req:: 🎯
    :id: feat_req_someip_166
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The size of the payload field depends on the transport protocol used. With UDP the payload can be between 0 and 1400 Bytes. The limitation to 1400 Bytes is needed in order to allow for future changes to protocol stack (e.g. changing to IPv6 or adding security means). Since TCP supports segmentation of payloads, larger sizes are automatically supported.
    
.. heading:: Serialization of Parameters and Data Structures
    :id: feat_req_someip_167
    :layout: focus
    :style: clean

Serialization of Parameters and Data Structures
*********************************************** 

.. feat_req:: 🎯
    :id: feat_req_someip_168
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The serialization is based on the parameter list defined by the interface specification. To allow migration of the service interface the deserialization code shall ignore parameters attached to the end of previously known parameter list; i.e. parameters that were not defined in the interface specification used to generate or parameterize the deserialization code.
    
.. feat_req:: 🎯
    :id: feat_req_someip_169
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The interface specification defines the exact position of all parameters in the PDU and has to consider the memory alignment. The serialization shall not try to automatically align parameters but shall be aligned as specified in the interface specification. SOME/IP payload should be placed in memory so that the SOME/IP payload is suitable aligned. For infotainment ECUs an alignment of 8 Bytes (i.e. 64 bits) should be achieved, for all ECU at least an alignment of 4 Bytes shall be achieved.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_170
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In the following the deserialization of different parameters is specified.
    
.. heading:: Basic Datatypes
    :id: feat_req_someip_171
    :layout: focus
    :style: clean

Basic Datatypes
=============== 

.. feat_req:: 🎯
    :id: feat_req_someip_172
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The following basic datatypes shall be supported:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      * - Type 
        - Description 
        - Size [bit] 
        - Remark
      * - boolean
        - TRUE/FALSE value
        - 8
        - FALSE (0), TRUE (1)
      * - uint8
        - unsigned Integer
        - 8
        - 
      * - uint16
        - unsigned Integer
        - 16
        - 
      * - uint32
        - unsigned Integer
        - 32
        - 
      * - sint8
        - signed Integer
        - 8
        - 
      * - sint16
        - signed Integer
        - 16
        - 
      * - sint32
        - signed Integer
        - 32
        - 
      * - float32
        - floating point number
        - 32
        - IEEE 754 binary32 (Single Precision)
      * - float64
        - floating point number
        - 64
        - IEEE 754 binary64 (Double Precision)

.. feat_req:: 🎯
    :id: feat_req_someip_224
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Byte Order is specified for each parameter by the interface definition.
    
.. feat_req:: 🎯
    :id: feat_req_someip_623
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For infotainment applications uint64 and sint64 types shall be supported additionally.
    
.. heading:: Structured Datatypes (structs)
    :id: feat_req_someip_229
    :layout: focus
    :style: clean

Structured Datatypes (structs)
============================== 

.. feat_req:: 🎯
    :id: feat_req_someip_230
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The serialization of a struct shall be close to the in-memory layout. This means, only the parameters shall be serialized sequentially into the buffer. Especially for structs it is important to consider the correct memory alignment. Insert reserved/padding elements in the interface definition if needed for alignment, since the SOME/IP implementation shall not automatically add such padding.
    
.. feat_req:: 🎯
    :id: feat_req_someip_577
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If a SOME/IP implementation encounters an interface specification that leads to an PDU not correctly aligned (e.g. because of an unaligned struct), a SOME/IP implementation shall warn about a misaligned struct but shall not fail in generating the code.
    
.. feat_req:: 🎯
    :id: feat_req_someip_575
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A struct shall be serialized exactly as specified.
    
.. feat_req:: 🎯
    :id: feat_req_someip_574
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The SOME/IP implementation shall not automatically insert dummy/padding elements.
    
.. feat_req:: 🎯
    :id: feat_req_someip_231
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Serialization of Structs

.. drawsvg_directive:: images/drawsvg/feat_req_someip_231.py

    
.. feat_req:: 🎯
    :id: feat_req_someip_600
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The interface specification may add a length field of 8, 16 or 32 Bit in front of the Struct.
    
.. feat_req:: 🎯
    :id: feat_req_someip_602
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the length of the length field is not specified, a length of 0 has to be assumed and no length field is in the message.
    
.. feat_req:: 🎯
    :id: feat_req_someip_601
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length field of the struct describes the number of bytes of the struct. If the length is greater than the length of the struct as specified in the Interface Definition only the bytes specified in the Interface Specification shall interpreted and the other bytes shall be skipped based on the length field.

This allows for extensible structs which allow better migration of interfaces.
    
.. heading:: Strings (fixed length)
    :id: feat_req_someip_232
    :layout: focus
    :style: clean

Strings (fixed length)
====================== 

.. feat_req:: 🎯
    :id: feat_req_someip_233
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Strings are encoded using Unicode and are terminated with a “\0”-character. The length of the string (this includes the “\0”) in Bytes has to be specified in the interface definition. Fill unused space using “\0”.
    
.. feat_req:: 🎯
    :id: feat_req_someip_234
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Different Unicode encoding shall be supported including UTF-8, UTF-16BE, and UTF-16LE. Since these encoding have a dynamic length of bytes per character, the maximum length in bytes is up to three times the length of characters in UTF-8 plus 1 Byte for the termination with a “\0” or two times the length of the characters in UTF-16 plus 2 Bytes for a “\0”.
    
.. feat_req:: 🎯
    :id: feat_req_someip_235
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The String encoding shall be specified in the interface definition.
    
.. heading:: Strings (dynamic length)
    :id: feat_req_someip_236
    :layout: focus
    :style: clean

Strings (dynamic length)
======================== 

.. feat_req:: 🎯
    :id: feat_req_someip_237
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Strings with dynamic length start with a length field. The length is measured in Bytes and is followed by the “\0”-terminated string data. The interface definition shall also define the maximum number of bytes the string (including termination with “\0”) can occupy.
    
.. feat_req:: 🎯
    :id: feat_req_someip_582
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length of the length field may be 8, 16 or 32 Bit. Fixed length strings may be seen as having a 0 Bit length field.
    
.. feat_req:: 🎯
    :id: feat_req_someip_581
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If not specified otherwise in the interface specification the length of the length field is 32 Bit (default length of length field).
    
.. feat_req:: 🎯
    :id: feat_req_someip_562
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length of the Strings length field is not considered in the value of the length field; i.e. the length field does not count itself.
    
.. feat_req:: 🎯
    :id: feat_req_someip_238
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Supported encodings are defined as in :need:`feat_req_someip_232`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_239
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the interface definition hints the alignment of the next data element the string shall be extended with “\0” characters to meet the alignment.
    
.. heading:: Arrays (fixed length)
    :id: feat_req_someip_240
    :layout: focus
    :style: clean

Arrays (fixed length)
===================== 

.. feat_req:: 🎯
    :id: feat_req_someip_241
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length of fixed length arrays is defined by the interface definition. They can be seen as repeated elements. In :need:`feat_req_someip_253` dynamic length arrays are shown, which can be also used. 
    
.. heading:: One-dimensional
    :id: feat_req_someip_242
    :layout: focus
    :style: clean

One-dimensional
--------------- 

.. feat_req:: 🎯
    :id: feat_req_someip_243
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The one-dimensional arrays with fixed length n carry exactly n elements of the same type. The layout is shown in Figure :need:`feat_req_someip_244`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_244
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: One-dimensional array (fixed length)

.. drawsvg_directive:: images/drawsvg/feat_req_someip_244.py

    
.. heading:: Multidimensional
    :id: feat_req_someip_245
    :layout: focus
    :style: clean

Multidimensional
---------------- 

.. feat_req:: 🎯
    :id: feat_req_someip_246
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The serialization of multidimensional arrays follows the in-memory layout of multidimensional arrays in the C++ programming language (row-major order) and is shown in Figure :need:`feat_req_someip_247`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_247
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Multidimensional array (fixed length)

.. drawsvg_directive:: images/drawsvg/feat_req_someip_247.py

    
.. heading:: Optional Fields
    :id: feat_req_someip_251
    :layout: focus
    :style: clean

Optional Fields
=============== 

.. feat_req:: ⓘ 
    :id: feat_req_someip_252
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Optional Fields shall be encoded as array with 0 to 1 elements. For the serialization of arrays with dynamic length see :need:`feat_req_someip_253`.
    
.. heading:: Dynamic Length Arrays
    :id: feat_req_someip_253
    :layout: focus
    :style: clean

Dynamic Length Arrays
===================== 

.. feat_req:: 🎯
    :id: feat_req_someip_254
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The layout of arrays with dynamic length basically is based on the layout of fixed length arrays. To determine the size of the array the serialization adds a length field (default length 32 bit) in front of the data, which counts the bytes of the array. The length does not include the size of the length field. Thus, when transporting an array with zero elements the length is set to zero.
    
.. feat_req:: 🎯
    :id: feat_req_someip_621
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Interface Definition may define the length of the length field. Length of 0, 8, 16, and 32bit are allowed. If the length is set to 0 Bits, the number of elements in the array has to be fixed; thus, being an array with fixed length. 
    
.. feat_req:: 🎯
    :id: feat_req_someip_255
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The layout of dynamic arrays is shown in Figure :need:`feat_req_someip_256` and Figure :need:`feat_req_someip_258`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_256
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: One-dimensional array (dynamic length)

.. drawsvg_directive:: images/drawsvg/feat_req_someip_256.py

    
.. feat_req:: 🎯
    :id: feat_req_someip_257
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In the one-dimensional array one length field is used, which carries the number of bytes used for the array. The number of elements can be easily calculated by dividing by the size of an element.
    
.. feat_req:: 🎯
    :id: feat_req_someip_258
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: Multidimensional array (dynamic length)

.. drawsvg_directive:: images/drawsvg/feat_req_someip_258.py

    
.. feat_req:: 🎯
    :id: feat_req_someip_259
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In multidimensional arrays multiple length fields are needed.
    
.. feat_req:: 🎯
    :id: feat_req_someip_260
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The interface definition should define the maximal length of each dimension in order to allow for static buffer size allocation.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_261
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When measuring the length in Bytes, complex multi-dimensional arrays can be skipped over in deserialization.
    
.. heading:: Union / Variant
    :id: feat_req_someip_262
    :layout: focus
    :style: clean

Union / Variant
=============== 

.. feat_req:: 🎯
    :id: feat_req_someip_263
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A union (also called variant) is a parameter that can contain different types of elements. For example, if one defines a union of type uint8 and type uint16, the union may carry an element of uint8 or uint16. It is clear that that when using different types of elements the alignment of subsequent parameters may be distorted. To resolve this, padding might be needed.
    
.. feat_req:: 🎯
    :id: feat_req_someip_264
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The default serialization layout of unions in SOME/IP is as follows:

.. bitfield_directive:: images/bit_field/feat_req_someip_264.json

    
.. feat_req:: 🎯
    :id: feat_req_someip_573
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The order of the length and type field may be adjusted by the interface specification. If this is not specified, the default layout as in :need:`feat_req_someip_264` shall be used.
    
.. feat_req:: 🎯
    :id: feat_req_someip_563
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length of the length field shall be defined by the Interface Specification and shall be 32, 16, 8, or 0 bits
    
.. feat_req:: 🎯
    :id: feat_req_someip_571
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
An length field of 0 Bit means that no length field will be written to the PDU.
    
.. feat_req:: 🎯
    :id: feat_req_someip_572
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the length field is 0 Bit, all types in the union shall be of the same length.
    
.. feat_req:: 🎯
    :id: feat_req_someip_583
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the interface specification defines a union with a length field of 0 Bits and types with different length, a SOME/IP implementation shall warn about this and use the length of the longest element and pad all others with zeros (0x00).
    
.. feat_req:: 🎯
    :id: feat_req_someip_566
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the Interface Specification does not specify the length of the length field for a union, 32 bit length of the length field shall be used.
    
.. feat_req:: 🎯
    :id: feat_req_someip_272
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length field defines the size element and padding in bytes and does not include the size of the length field and type field.
    
.. feat_req:: 🎯
    :id: feat_req_someip_564
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length of the type field shall be defined by the Interface Specification and shall be 32, 16, or 8 bits.
    
.. feat_req:: 🎯
    :id: feat_req_someip_565
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the Interface Specification does not specify the length of the type field of a union, 32 bit length of the type field shall be used.
    
.. feat_req:: 🎯
    :id: feat_req_someip_273
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The type field describes the type of the element. Possible values of the type field are defined by the interface specification for each union separately. The types are encoded as in the interface specification in ascending order starting with 1. The 0 is reserved for the NULL type – i.e. an empty union. The usage of NULL shall be allowed by the Interface Definition.
    
.. feat_req:: 🎯
    :id: feat_req_someip_274
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The element is serialized depending on the type in the type field. In conjunction with the length field padding can be added behind the element. The deserializer shall skip bytes according to the length field. The value of the length field for each type shall be defined by the interface specification.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_275
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
By using a struct different padding layouts can be achieved.
    
.. heading:: Example:  Union of uint8/uint16 both padded to 32 bit
    :id: feat_req_someip_276
    :layout: focus
    :style: clean

Example:  Union of uint8/uint16 both padded to 32 bit
----------------------------------------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someip_277
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In this example a length of the length field is specified as 32 Bits. The union shall support a uint8 and a uint16 as elements. Both are padded to the 32 bit boundary (length=4).
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_278
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A uint8 will be serialized like this:

.. bitfield_directive:: images/bit_field/feat_req_someip_278.json

    
.. feat_req:: ⓘ 
    :id: feat_req_someip_289
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A uint16 will be serialized like this:

.. bitfield_directive:: images/bit_field/feat_req_someip_289.json

    
.. heading:: Example Map / Dictionary
    :id: feat_req_someip_299
    :layout: focus
    :style: clean

Example Map / Dictionary
======================== 

.. feat_req:: ⓘ 
    :id: feat_req_someip_300
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Maps or dictionaries can be easily described as an array of key-value-pairs. The most basic way to implement a map or dictionary would be an array of a struct with two fields: key and value. Since the struct has no length field, this is as efficient as a special map or dictionary type could be. When choosing key and value as uint16, a serialized map with 3 entries looks like this:

.. bitfield_directive:: images/bit_field/feat_req_someip_300.json

    
.. heading:: RPC Protocol specification
    :id: feat_req_someip_313
    :layout: focus
    :style: clean

.. rst-class:: break_before

RPC Protocol specification
########################## 

.. feat_req:: ⓘ 
    :id: feat_req_someip_314
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
This chapter describes the RPC protocol of SOME/IP.
    
.. heading:: Transport Protocol Bindings
    :id: feat_req_someip_315
    :layout: focus
    :style: clean

Transport Protocol Bindings
*************************** 

.. feat_req:: ⓘ 
    :id: feat_req_someip_316
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In order to transport SOME/IP messages of IP different transport protocols may be used. SOME/IP currently supports UDP and TCP. Their bindings are explained in the following sections, while Section :need:`feat_req_someip_450` discusses which transport protocol to choose.
    
.. heading:: UDP Binding
    :id: feat_req_someip_317
    :layout: focus
    :style: clean

UDP Binding
=========== 

.. feat_req:: 🎯
    :id: feat_req_someip_318
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The UDP binding of SOME/IP is straight forward by transporting SOME/IP messages in UDP packets. The SOME/IP messages shall not be fragmented. Therefore care shall be taken that SOME/IP messages are not too big, i.e. up to 1400 Bytes of SOME/IP payload. Messages with bigger payload shall not be transported over UDP but with e.g. TCP.
    
.. feat_req:: 🎯
    :id: feat_req_someip_319
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The header format allows transporting more than one SOME/IP message in a single UDP packet. The SOME/IP implementation can easily identify the end of a SOME/IP message by means of the SOME/IP length field. Based on the UDP lengths field SOME/IP can determine if there are additional SOME/IP messages in the UDP packet.
    
.. feat_req:: 🎯
    :id: feat_req_someip_584
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Each SOME/IP payload shall have its own SOME/IP header.
    
.. feat_req:: 🎯
    :id: feat_req_someip_320
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
As optimization the UDP binding of SOME/IP can use acknowledgment messages especially for request/response communication that triggers a long running operation at server side that shall be completed before sending a result (transport or processing acknowledgement). The acknowledgment messages are SOME/IP messages with exactly the same header fields but with the changed message type and without a payload. The use of these additional acknowledgment messages shall be configured by the interface specification.

An alternative would be to design a method with an return code or out parameter that specifies "operation still in progress", so that the requesting ECU can ask again after a certain time.
    
.. heading:: TCP Binding
    :id: feat_req_someip_323
    :layout: focus
    :style: clean

TCP Binding
=========== 

.. feat_req:: ⓘ 
    :id: feat_req_someip_324
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The TCP binding of SOME/IP is heavily based on the UDP binding. In contrast to the UDP binding, the TCP binding allows much bigger SOME/IP messages and the transport of SOME/IP messages after each other (pipelining).
    
.. feat_req:: 🎯
    :id: feat_req_someip_585
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Every SOME/IP payload shall have its own SOME/IP header.
    
.. feat_req:: 🎯
    :id: feat_req_someip_325
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In order to lower latency and reaction time, Nagle’s algorithm shall be turned off (TCP_NODELAY).
    
.. feat_req:: 🎯
    :id: feat_req_someip_326
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When the TCP connection is lost, outstanding requests should be handled as timeouts. Since TCP handles reliability, additional means of reliability are not needed. Error handling is discussed in detail in :need:`feat_req_someip_364`.
    
.. heading:: Allowing resync to TCP stream using Magic Cookies
    :id: feat_req_someip_619
    :layout: focus
    :style: clean

Allowing resync to TCP stream using Magic Cookies
------------------------------------------------- 

.. feat_req:: 🎯
    :id: feat_req_someip_586
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In order to allow resynchronization to SOME/IP over TCP in testing and integration scenarios the SOME/IP Magic Cookie Message (Figure :need:`feat_req_someip_589`) shall be used between SOME/IP messages over TCP. 
    
.. feat_req:: 🎯
    :id: feat_req_someip_591
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Before the first SOME/IP message transported in a TCP segment the SOME/IP Magic Cookie Message shall be included.
    
.. feat_req:: 🎯
    :id: feat_req_someip_592
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The implementation shall only include up to one SOME/IP Magic Cookie Message per TCP segment.
    
.. feat_req:: 🎯
    :id: feat_req_someip_593
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the implementation has no appropriate access to the message segmentation mechanisms and therefore cannot fulfill :need:`feat_req_someip_591` and :need:`feat_req_someip_592`, the implementation shall include SOME/IP Magic Cookie Messages based on the following heuristic:
    
.. feat_req:: 🎯
    :id: feat_req_someip_594
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Add SOME/IP Magic Cookie Message once every 10 seconds to the TCP connection as long as messages are transmitted over this TCP connection.
    
.. feat_req:: 🎯
    :id: feat_req_someip_609
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The layout of the Magic Cookie Message is based on SOME/IP. The fields are set as follows:

* Service ID = 0xFFFF
* Method ID = 0x0000 (for the direction Client to Server)
* Method ID = 0x8000 (for the direction Server to Client)
* Length = 0x0000 0008
* Client ID = 0xDEAD
* Session ID = 0xBEEF
* Protocol Version as specified above
* Interface Version = 0x01
* Message Type = 0x01 (for Client to Server Communication) or 0x02 (for Server to Client Communication)
* Return Code = 0x00
    
.. feat_req:: 🎯
    :id: feat_req_someip_607
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The layout of the Magic Cookie Messages is shown in Figure :need:`feat_req_someip_589`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_589
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: SOME/IP Magic Cookie Message for SOME/IP

.. drawsvg_directive:: images/drawsvg/feat_req_someip_589.py

    
.. heading:: Multiple Service-Instances
    :id: feat_req_someip_444
    :layout: focus
    :style: clean

Multiple Service-Instances
========================== 

.. feat_req:: 🎯
    :id: feat_req_someip_445
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
While different services can share the same port number, multiple Service Instances on a single ECU shall listen on different ports per instance. Instances on different ECUs are identified through different Instance IDs. Those are used for Service Discovery but are not contained in the SOME/IP header.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_446
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A Service Instance can be identified through the combination of the Service ID combined with the socket (i.e. IP-address, transport protocol (UDP/TCP), and port number). It is recommended that instances use the same port number for UDP and TCP. If a service instance uses UDP port x, only this instance of the service and not another instance of the same service should use exactly TCP port x for its services.
    
.. heading:: Request/Response Communication
    :id: feat_req_someip_327
    :layout: focus
    :style: clean

Request/Response Communication
****************************** 

.. feat_req:: 🎯
    :id: feat_req_someip_328
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
One of the most common communication patterns is the request/response pattern. One party (in the following called the client) sends a request message, which is answered by another party (the server).
    
.. feat_req:: 🎯
    :id: feat_req_someip_329
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
In the SOME/IP header the request message the client has to do the following:

* Construct the payload
* Set the Message ID based on the method the client wants to call
* Set the Length field to 8 bytes (for the second part of the SOME/IP header) + length of the serialized payload
* Optionally set the Request ID to a unique number (shall be unique for client only)
* Set the Protocol Version according :need:`feat_req_someip_89`.
* Set the Interface Version according to the interface definition
* Set the Message Type to Request (i.e. 0x00)
* Set the Return Code to 0x00
    
.. feat_req:: 🎯
    :id: feat_req_someip_338
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The server builds it header based on the header of the client and does in addition:

* Construct the payload
* Set the length to the 8 Bytes + new payload size
* Set the Message Type to RESPONSE (i.e. 0x80) or ERROR (i.e. 0x81)
* Set the Return Code.
    
.. heading:: Fire&Forget Communication
    :id: feat_req_someip_344
    :layout: focus
    :style: clean

Fire&Forget Communication
************************* 

.. feat_req:: 🎯
    :id: feat_req_someip_345
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Requests without response message are called Fire&Forget. The implementation is basically the same as for Request/Response with the following differences:

* There is no response message.
* The message type is set to REQUEST_NO_RETURN (i.e. 0x01)
    
.. feat_req:: 🎯
    :id: feat_req_someip_348
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Fire&Forget messages do no return an error. Error handling and return codes shall be implemented by the application when needed.
    
.. heading:: Notification
    :id: feat_req_someip_351
    :layout: focus
    :style: clean

Notification
************ 

.. feat_req:: ⓘ 
    :id: feat_req_someip_352
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Notifications describe a general Publish/Subscribe-Concept. Usually the server publishes a service to which a client subscribes. On certain events the server will send the client a notification, which could be for instance an updated value or an event that occurred.
    
.. feat_req:: 🎯
    :id: feat_req_someip_353
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP is used only for transporting the updated value and not for the publishing and subscription mechanisms. These mechanisms are implemented by SOME/IP-SD and are explained in Section :need:`feat_req_someip_360`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_354
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When more than one subscribed client on the same ECU exists, the system should handle the replication of notifications in order to save transmissions on the communication medium. This is especially important, when notifications are transported using multicast messages.
    
.. heading:: Strategy for sending notifications
    :id: feat_req_someip_355
    :layout: focus
    :style: clean

Strategy for sending notifications
================================== 

.. feat_req:: 🎯
    :id: feat_req_someip_356
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
For different use cases different strategies for sending notifications are possible and shall defined in the service interface. The following examples are common:

* Cyclic update – send an updated value in a fixed interval (e.g. every 10 ms)
* Update on change – send an update as soon as a “value” changes (e.g. door open)
* Epsilon change – only send an update when the difference to the last value is greater than a certain epsilon. This concept may be adaptive, i.e. the prediction is based on a history; thus, only when the difference between prediction and current value is greater than epsilon an update is transmitted.
    
.. heading:: Publish/Subscribe Handling
    :id: feat_req_someip_360
    :layout: focus
    :style: clean

Publish/Subscribe Handling
========================== 

.. feat_req:: 🎯
    :id: feat_req_someip_361
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Publish/Subscribe handling shall be implemented according to Section :need:`feat_req_someipsd_137`.
    
.. heading:: Fields
    :id: feat_req_someip_630
    :layout: focus
    :style: clean

Fields
****** 

.. feat_req:: 🎯
    :id: feat_req_someip_631
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A field shall be a combination of an optional getter, an optional setter, and an optional notification event.
    
.. feat_req:: 🎯
    :id: feat_req_someip_632
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A field shall have at least 1 getter or 1 setter or 1 notification event.
    
.. feat_req:: 🎯
    :id: feat_req_someip_633
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The getter of a field shall be a request/response call that has an empty payload in the request message and the value of the field in the payload of the response message.
    
.. feat_req:: 🎯
    :id: feat_req_someip_634
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The setter of a field shall be a request/response call that has the desired valued of the field in the payload of the request message and the value that was set to field in the payload of the response message.
    
.. feat_req:: 🎯
    :id: feat_req_someip_635
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The notifier shall be an event that transports the value of a field on change and follows the rules for events.
    
.. heading:: Error Handling
    :id: feat_req_someip_364
    :layout: focus
    :style: clean

Error Handling
************** 

.. feat_req:: ⓘ 
    :id: feat_req_someip_365
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The error handling can be done in the application or the communication layer below. Therefore different possible mechanisms exist.
    
.. heading:: Transporting Application Error Codes and Exceptions
    :id: feat_req_someip_366
    :layout: focus
    :style: clean

Transporting Application Error Codes and Exceptions
=================================================== 

.. feat_req:: 🎯
    :id: feat_req_someip_367
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For the error handling two different mechanisms are supported. All messages have a return code field to carry the return code. However, only responses (Message Types 0x80 and 0x81) use this field to carry a return code to the request (Message Type 0x00) they answer. All other messages set this field to 0x00 (see :need:`feat_req_someip_94`). For more detailed errors the layout of the Error Message (Message Type 0x81) can carry specific fields for error handling, e.g. an Exception String. Error Messages are sent instead of Response Messages.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_368
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
This can be used to handle all different application errors that might occur in the server. In addition, problems with the communication medium or intermediate components (e.g. switches) may occur, which have to be handled e.g. by means of reliable transport.
    
.. heading:: Return Code
    :id: feat_req_someip_369
    :layout: focus
    :style: clean

Return Code
=========== 

.. feat_req:: 🎯
    :id: feat_req_someip_597
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The system shall not return an error message for events/notifications.
    
.. feat_req:: 🎯
    :id: feat_req_someip_371
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The following Return Codes are currently defined and shall be implemented as described:
    


    .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      * - ID 
        - Name 
        - Description
      * - 0x00
        - E_OK
        - No error occurred
      * - 0x01
        - E_NOT_OK
        - An unspecified error occurred
      * - 0x02
        - E_UNKNOWN_SERVICE
        - The requested Service ID is unknown.
      * - 0x03
        - E_UNKNOWN_METHOD
        - The requested Method ID is unknown. Service ID is known.
      * - 0x04
        - E_NOT_READY
        - Service ID and Method ID are known. Application not running.
      * - 0x05
        - E_NOT_REACHABLE
        - System running the service is not reachable (internal errorcode only).
      * - 0x06
        - E_TIMEOUT
        - A timeout occurred (internal error code only).
      * - 0x07
        - E_WRONG_PROTOCOL_VERSION
        - Version of SOME/IP protocol not supported
      * - 0x08
        - E_WRONG_INTERFACE_VERSION
        - Interface version mismatch
      * - 0x09
        - E_MALFORMED_MESSAGE
        - Deserialization error (e.g. length or type incorrect).
      * - | 0x0a
          | -
          | 0x1f
        - RESERVED
        - Reserved for generic SOME/IP errors. These errors will be specified in future versions of this document.
      * - | 0x20
          | -
          | 0x3f
        - RESERVED 
        - Reserved for specific errors of services and methods. These errors are specified by the interface specification.

.. feat_req:: 🎯
    :id: feat_req_someip_598
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Generation and handling of return codes shall be configurable.
    
.. heading:: Error Message Format
    :id: feat_req_someip_421
    :layout: focus
    :style: clean

Error Message Format
==================== 

.. feat_req:: ⓘ 
    :id: feat_req_someip_422
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For a more flexible error handling, SOME/IP allows the user to specify a message layout specific for errors instead of using the message layout for response messages. This is defined by the interface specification and can be used to transport exceptions of higher level programming languages.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_423
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The recommended layout for the exception message is the following:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_424
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Union of specific exceptions. At least a generic exception without fields needs to exist.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_425
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Dynamic Length String for exception description.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_426
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The union gives the flexibility to add new exceptions in the future in a type-safe manner. The string is used to transport human readable exception descriptions to ease testing and debugging.
    
.. heading:: Communication Errors and Handling of Communication Errors
    :id: feat_req_someip_429
    :layout: focus
    :style: clean

Communication Errors and Handling of Communication Errors
========================================================= 

.. feat_req:: ⓘ 
    :id: feat_req_someip_430
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When considering the transport of RPC messages different reliability semantics exist:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_431
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Maybe – the message might reach the communication partner
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_432
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* At least once – the message reaches the communication partner at least once
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_433
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Exactly once – the message reaches the communication partner exactly once
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_434
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When using these terms in regard to Request/Response the term applies to both messages (i.e. request and response or error).
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_435
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
While different implementations may implement different approaches, SOME/IP currently achieves “maybe” reliability when using the UDP binding and “exactly once” reliability when using the TCP binding. Further error handling is left to the application.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_436
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For “maybe” reliability, only a single timeout is needed, when using request/response communication in combination of UDP as transport protocol. Figure :need:`feat_req_someip_437` shows the state machines for “maybe” reliability. The client’s SOME/IP implementation has to wait for the response for a specified timeout. If the timeout occurs SOME/IP shall signal E_TIMEOUT to the client.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_437
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: State Machines for Reliability "Maybe"

.. drawsvg_directive:: images/drawsvg/feat_req_someip_437.py

    
.. feat_req:: ⓘ 
    :id: feat_req_someip_438
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For “exactly once” reliability the TCP binding may be used, since TCP was defined to allow for reliable communication.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_439
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Additional mechanisms to reach higher reliability may be implemented in the application or in a SOME/IP implementation. Keep in mind that the communication does not have to implement these features. The next Section :need:`feat_req_someip_440` describes such optional reliability mechanisms.
    
.. heading:: Application based Error Handling
    :id: feat_req_someip_440
    :layout: focus
    :style: clean

Application based Error Handling
-------------------------------- 

.. feat_req:: ⓘ 
    :id: feat_req_someip_441
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The application can easily implement “at least once” reliability by using idempotent operations (i.e. operation that can be executed multiple times without side effects) and using a simple timeout mechanism. Figure :need:`feat_req_someip_443` shows the state machines for “at least once” reliability using implicit acknowledgements. When the client sends out the request it starts a timer with the timeout specified for the specific method. If no response is received before the timer expires (round transition at the top), the client will retry the operation. A Typical number of retries would be 2, so that 3 requests are sent.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_442
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The number of retries, the timeout values, and the timeout behavior (constant or exponential back off) are outside of the SOME/IP specification and may be added to the interface definition.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_443
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure: State Machines for Reliability "At least once" (idempotent operations)

.. drawsvg_directive:: images/drawsvg/feat_req_someip_443.py

    
.. heading:: Guidelines (informational)
    :id: feat_req_someip_449
    :layout: focus
    :style: clean

.. rst-class:: break_before

Guidelines (informational)
########################## 

.. heading:: Choosing the transport protocol
    :id: feat_req_someip_450
    :layout: focus
    :style: clean

Choosing the transport protocol
******************************* 

.. feat_req:: ⓘ 
    :id: feat_req_someip_451
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP directly support the two most used transport protocols of the Internet: User Datagram Protocol (UDP) and Transmission Control Protocol (TCP). While UDP is a very lean transport protocol supporting only the most important features (multiplexing and error detecting using a checksum), TCP adds additional features for achieving a reliable communication. TCP can not only handle bit errors but also segmentation, loss, duplication, reordering, and network congestion; thus, TCP is the more powerful transport protocol.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_452
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For use inside the vehicle, requirements are not the same as for the Internet. For many applications, we require a very short timeout to react in a very short time. These requirements are better met using UDP because the application itself can handle the unlikely event of errors. For example, in use cases with cyclic data it is often the best approach to just wait for the next data transmission instead of trying to repair the last one. The major disadvantage of UDP is that it does not handle segmentation; thus, only being able to transport smaller chunks of data.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_453
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Guideline:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_454
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Use UDP if very hard latency requirements (<100ms) in case of errors is needed
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_455
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Use TCP only if very large chunks of data need to be transported (> 1400 Bytes) and no hard latency requirements in the case of errors exists
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_456
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Try using external transport (Network File System, APIX link, 1722, …) when more suited for the use case. Just transport file handle or similar. This gives the designer more freedom (caching etc.).
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_457
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The transport protocol used is specified by the interface specification on a per-message basis. Methods, Events, and Fields should commonly only use a single transport protocol.
    
.. heading:: Serialization of Data Structures Containing Pointers
    :id: feat_req_someip_461
    :layout: focus
    :style: clean

Serialization of Data Structures Containing Pointers
**************************************************** 

.. feat_req:: ⓘ 
    :id: feat_req_someip_462
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For the serialization of data structures containing pointers (e.g. a tree in memory), the pointers cannot be just transferred using a data type (e.g. uint8) but shall be converted for transport. Different approaches for the serialization of pointers exist. We recommend the following approaches.
    
.. heading:: Array of data structures with implicit ID
    :id: feat_req_someip_463
    :layout: focus
    :style: clean

Array of data structures with implicit ID
========================================= 

.. feat_req:: ⓘ 
    :id: feat_req_someip_464
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When transporting a set of data structures with pointers that is small enough to fit into a single RPC message:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_465
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Store data structures (e.g. tree nodes) in array
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_466
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Use position in array as ID of stored data structure
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_467
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Replace pointers with IDs of the data structures pointed to
    
.. heading:: Array of data structures with explicit ID
    :id: feat_req_someip_468
    :layout: focus
    :style: clean

Array of data structures with explicit ID
========================================= 

.. feat_req:: ⓘ 
    :id: feat_req_someip_469
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
With larger sets of data structures additional problems have to be resolved. Since not all data structures fit into a single message the IDs have to be unique over different messages. This can be achieved in different ways:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_470
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Add an offset field to every message. The ID of an array element will be calculated by adding the offset to its position in the array. Keep in mind that the offset needs to be carefully been chosen. If for example every message can contain up to ten data structures (0-9), the offset could be chosen as 0, 10, 20, 30, and so on.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_471
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Store an explicit ID by using an array of structs. The first field in the struct will be an ID (e.g. uint32) and the second field the data structure itself. For security and reliability reasons the pointer (i.e. the memory address) should never be used directly as ID.
    
.. heading:: Compatibility rules for Interface Design (informational)
    :id: feat_req_someip_472
    :layout: focus
    :style: clean

.. rst-class:: break_before

Compatibility rules for Interface Design (informational)
######################################################## 

.. feat_req:: ⓘ 
    :id: feat_req_someip_473
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
As for all serialization formats migration towards a newer service interface is somewhat limited. Using a set of compatibility rules, SOME/IP allows for evolution of service interfaces. One can do the following additions and enhancements in a non-breaking way:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_474
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Add new method to a service
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_475
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Shall be implemented at server first.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_476
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Add parameter to the end of a method’s in or out parameters
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_477
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* When the receiver adds them first, a default value has to be defined
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_478
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* When the sender adds them first, the receiver will ignore them
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_479
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Add an exception to the list of exceptions a method can throw
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_480
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Should update client first
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_481
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* If exception is unknown, “unknown exception” needs to thrown. The exception description string however can be copied over.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_482
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Add new type to union
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_483
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Should update receiver first
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_484
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Can be skipped if unknown (sender updates first)
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_485
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Define a new data type for new methods
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_486
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Define a new exception for new methods
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_487
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Not of all these changes can be introduced at the client or server side first. In some cases only the client or server can be changed first. For example, when sending an additional parameter with a newer implementation, the older implementation can only skip this parameter.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_488
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When the receiver of a message adds for example a new parameter to be received, it has to define a default value. This is needed in the case of a sender with an older version of the service sends the message without the additional parameter.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_489
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Some changes in the interface specification can be implemented in a non-breaking way:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_490
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Delete Parameters in Functions
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_491
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Need to add default value first at receiver first and parameters need to be at end of list
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_492
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Remove Exceptions from functions
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_493
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Trivial at server side
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_494
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Client needs to throw “unknown exception”, if encountering old exception
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_495
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Renaming parameters, functions, and services is possible since the names are not transmitted. The generated code only looks at the IDs and the ordering of parameters, which shall not be changed in migration.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_605
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the struct is configured by the interface specification to have a length field, the following is possible:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_498
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Adding / deleting fields to/from the end of structs
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_496
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Currently not supported are the following changes:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_497
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Reordering parameters
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_499
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Replace supertype by subtype (as in object oriented programming languages)
    