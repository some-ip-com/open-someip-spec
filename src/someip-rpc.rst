
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
  
This document specifies the Scalable service-Oriented MiddlewarE over IP (SOME/IP) – an automotive/embedded RPC mechanism and the underlying serialization / on-wire format.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_697
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The only valid abbreviation is SOME/IP. Other abbreviations (e.g. Some/IP) are wrong and shall not be used.
    
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

* Fulfills the hard requirements regarding resource consumption in an embedded world.
* Is compatible through as many use cases and communication partners as possible.
* Is compatible with AUTOSAR at least on the on-wire format level; i.e. can communicate with PDUs AUTOSAR can receive and send without modification to the AUTOSAR standard.
* Provides the features required by automotive use cases.
* Is scalable from tiny to large platforms.
* Can be implemented on different operating system (e.g. AUTOSAR, GENIVI, and OSEK) and even embedded devices without operating system.
    
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
  
* Method – a method, procedure, function, or subroutine that is called/invoked.
* Parameters – input, output, or input/output arguments of a method or an event.

  * Input/output arguments are arguments shared for input and output.

* Remote Procedure Call (RPC) – a method call from one ECU to another that is transmitted using messages.
* Request – a message of the client to the server invoking a method.
* Response – a message of the server to the client transporting results of a method invocation.
* Request/Response communication – an RPC that consists of request and response.
* Fire&Forget communication – an RPC call that consists only of a request message.
* Event – a "Fire&Forget callback" that is only invoked on changes or cyclically and is sent from Server to Client.
* Field – a representation of a remote property, which has up to one getter, up to one setter, and up to one notifier.

  * The field shall contain at least a getter, a setter, or a notifier.
  * A field does represent a status and thus has an valid value at all times on which getter, setter, and notifier act upon.

* Notification Event – an event message the notifier of an field sends. The message of such a notifier cannot be distinguished from the event message; therefore, when referring to the message of an event, this shall also be true for the messages of notifiers of fields.
* Initial Event – the first transmission of a Notification Event of a Field after start of subscription to transport the initial (i.e. current) values of that Field.
* Getter – a Request/Response call that allows read access to a field.
* Setter – a Request/Response call that allows write access to a field.

  * The getter needs to return a value; thus, it needs to be a request/response call. The setter is a request/response call as well in order for the client to know whether the setter-operation succeeded.

* Notifier – sends out event message with a new value on change of the value of the field
* Service – a logical combination of zero or more methods, zero or more events, and zero or more fields (empty service is allowed, e.g. for announcing non-SOME/IP services in SOME/IP-SD).
* Eventgroup – a logical grouping of events and notification events of fields inside a service in order to allow subscription
* Service Interface – the formal specification of the service including its methods, events, and fields
* Service Instance – software implementation of the service interface, which can exist more than once in the vehicle and more than once on an ECU
* Server – The ECU offering a service instance shall be called server in the context of this service instance.
* Client – The ECU using the service instance of a server shall be called client in the context of this service instance.
* Union or Variant – a data structure that dynamically assumes different data types.
* Endpoint – the combination of IP address, Layer 4 protocol, and port number.
    
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
  
A service shall be identified using the Service ID.
    
.. feat_req:: 🎯
    :id: feat_req_someip_539
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Service IDs shall be of type 16 bit length unsigned integer (uint16).
    
.. feat_req:: 🎯
    :id: feat_req_someip_624
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service ID of 0xFFFE shall be used to encode non-SOME/IP services.
    
.. feat_req:: 🎯
    :id: feat_req_someip_627
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service ID of 0x0000 and 0xFFFF shall be reserved for special cases. A reference table is found at the end of this document in :need:`feat_req_someipids_505`.
    
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
  
A service instance shall be identified using the Service Instance ID.
    
.. feat_req:: 🎯
    :id: feat_req_someip_543
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Service Instance IDs shall be of type 16 bit length unsigned integer (uint16).
    
.. feat_req:: 🎯
    :id: feat_req_someip_579
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Service Instance IDs of 0x0000 and 0xFFFF shall not be used for a service instance, since 0x0000 is reserved and 0xFFFF is used to describe all service instances.
    
.. feat_req:: 🎯
    :id: feat_req_someip_544
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Different service instances within the same vehicle shall have different Service Instance IDs.

This means that two different camera services shall have two different Service Instance IDs SI-ID-1 and SI-ID-2. For all vehicles of a vehicle project SI-ID-1 shall be the same. The same is true for SI-ID-2. If considering another vehicle project, different IDs may be used but it makes sense to use the same IDs among different vehicle projects for ease in testing and integration.
    
.. feat_req:: 🎯
    :id: feat_req_someip_625
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Methods and events shall be identified inside a service using a 16 bit Method-ID, which is also called Event-ID for events and notifications.
    
.. feat_req:: 🎯
    :id: feat_req_someip_626
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Methods shall use Method-IDs with the highest bit set to 0, while the Method-IDs highest bit shall be set to 1 for events and notifications of fields.
    
.. feat_req:: 🎯
    :id: feat_req_someip_545
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
An eventgroup shall be identified using the Eventgroup ID.
    
.. feat_req:: 🎯
    :id: feat_req_someip_546
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Eventgroup IDs shall be of 16 bit length unsigned integer (uint16).
    
.. feat_req:: 🎯
    :id: feat_req_someip_547
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Different eventgroups of a service shall have different Eventgroup IDs.
    
.. heading:: Specification of the SOME/IP on-wire format
    :id: feat_req_someip_29
    :layout: focus
    :style: clean

.. rst-class:: break_before

Specification of the SOME/IP on-wire format
########################################### 

.. feat_req:: ⓘ 
    :id: feat_req_someip_30
    :reqtype: Information
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
  
SOME/IP shall be transported using UDP and/or TCP based on the configuration. For dynamic ports the ECU private port range is 49152-65535 until further notice. When used in a vehicle the OEM will specify the ports used in the interface specification.
    
.. feat_req:: 🎯
    :id: feat_req_someip_659
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The IP addresses and port numbers an ECU shall use, shall be taken from the configuration file(s), i.e. FIBEX or ARXML.
    
.. feat_req:: 🎯
    :id: feat_req_someip_660
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The client shall take the IP address and port number the server announces using SOME/IP-SD (see :need:`feat_req_someipsd_752`) for communicating with the server.
    
.. feat_req:: 🎯
    :id: feat_req_someip_658
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A very common port number for SOME/IP-SD is 30490/UDP but this shall be another port number is specified in the configuration.
    
.. feat_req:: 🎯
    :id: feat_req_someip_676
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The port 30490 (UDP and TCP as well) shall be only used for SOME/IP-SD and not used for applications communicating over SOME/IP.
    
.. feat_req:: 🎯
    :id: feat_req_someip_661
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
If an ECU needs to dynamically use a port number, it shall follow the rules of IETF and IANA for that:

* Ephemeral ports from range 49152-65535 (or what is defined for ECU)
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_33
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
It is recommended to use UDP for as many messages as possible and see TCP as fall-back for message requiring larger size. UDP allows the application to better control of timings and behavior when errors occur.
    
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
  
In combination with regular Ethernet, IPv4 and UDP can transport packets with up to 1472 bytes of data without fragmentation, while IPv6 uses additional 20 bytes. Especially for small systems fragmentation shall be avoided, so the SOME/IP header and payload shall be of limited length. The possible usage of security protocols further limits the maximal size of SOME/IP messages.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_36
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Best practice:

When using UDP as transport protocol SOME/IP messages use up to 1416 bytes for the SOME/IP header and payload, so that 1400 bytes are available for the payload.
    
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
  
All RPC-Headers shall be encoded in network byte order (big endian) [RFC 791]. The byte order of the parameters inside the payload shall be defined by the interface definition (e.g. FIBEX, ARXML, or FRANCA IDL) and shall be in network byte order when possible and if no other byte order is specified.
    
.. feat_req:: 🎯
    :id: feat_req_someip_675
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
This means that Length and Type fields shall be always in network byte order.
    
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
  
For interoperability reasons the header layout shall be identical for all implementations of SOME/IP and is shown in the Figure :need:`feat_req_someip_45`. The fields are presented in transmission order; i.e. the fields on the top left are transmitted first. In the following sections the different header fields and their usage is being described.
    
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
    
.. heading:: Mapping of IP Addresses and Ports in Response and Error Messages
    :id: feat_req_someip_48
    :layout: focus
    :style: clean

Mapping of IP Addresses and Ports in Response and Error Messages
---------------------------------------------------------------- 

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
    
.. heading:: Message ID [32 bit]
    :id: feat_req_someip_55
    :layout: focus
    :style: clean

Message ID [32 bit]
=================== 

.. feat_req:: 🎯
    :id: feat_req_someip_56
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Message ID is a 32 bit identifier that is used to dispatch the RPC call to a method of an application and to identify an event. The Message ID has to uniquely identify a method or event of a service.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_57
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The assignment of the Message ID is up to the user; however, the Message ID has to be unique for the whole system (i.e. the vehicle). The Message ID can be best compared to a CAN ID and should be handled with a comparable process. The next section describes how to structure the Message IDs in order to ease the organization of Message IDs.
    
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
  
In order to structure the different methods, events, and fields, they are clustered into services. Services have a set of methods, events, and fields as well as a Service ID, which is only used for this service. The events and notification events may in addition be assigned into a number eventgroups, which simplify the registration of events and notifies.

An event shall be part of zero to many eventgroups and an eventgroup shall  contain zero to many events.
A field shall be part of zero to many eventgroups and an eventgroup can contain zero to many fields.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_670
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Currently empty eventgroups are not used and events as well as fields are mapped to at least one eventgroup.
    
.. feat_req:: 🎯
    :id: feat_req_someip_60
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For RPC calls, the ID shall be structured in 2^16 services with 2^15 methods:

.. bitfield_directive:: images/bit_field/feat_req_someip_60.json

    
.. feat_req:: 🎯
    :id: feat_req_someip_66
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
With 16 bit Service ID and a 16 bit Method-ID starting with a 0-bit, this allows for up to 65536 services with up to 32768 methods each.
    
.. feat_req:: 🎯
    :id: feat_req_someip_67
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Since events and notifications (see Notification or Publish/Subscribe) are transported using RPC, the ID space for the events is further structured:

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
    
.. heading:: Length [32 bit]
    :id: feat_req_someip_76
    :layout: focus
    :style: clean

Length [32 bit]
=============== 

.. feat_req:: 🎯
    :id: feat_req_someip_77
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Length is a field of 32 bits containing the length in byte of the payload beginning with the Request ID/Client ID until the end of the SOME/IP-message.
    
.. feat_req:: 🎯
    :id: feat_req_someip_798
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP messages with a length value < 8 bytes shall be ignored.
    
.. heading:: Request ID [32 bit]
    :id: feat_req_someip_78
    :layout: focus
    :style: clean

Request ID [32 bit]
=================== 

.. feat_req:: 🎯
    :id: feat_req_someip_79
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Request ID allows a client to differentiate multiple calls to the same method. Therefore, the Request ID has to be unique for a single client and server combination only. When generating a response message, the server has to copy the Request ID from the request to the response message. This allows the client to map a response to the issued request even with more than one request outstanding.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_80
    :reqtype: Information
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
  
The Request ID shall be constructed of the Client ID and Session ID:

.. bitfield_directive:: images/bit_field/feat_req_someip_83.json

    
.. feat_req:: 🎯
    :id: feat_req_someip_699
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Client ID is the unique identifier for the calling client inside the ECU.

Note:
This means that the implementer of an ECU can define the Client-IDs as required by his implementation and the Server does not need to know this layout or definitions because it just copies the complete Request-ID in the response.
    
.. feat_req:: 🎯
    :id: feat_req_someip_701
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Client ID shall also support being unique in the overall vehicle by having a configurable prefix or fixed value (e.g. the most significant byte of Client ID being the diagnostics address or a configured Client ID for a given application/SW-C).

For example:

.. bitfield_directive:: images/bit_field/feat_req_someip_701.json

    
.. feat_req:: 🎯
    :id: feat_req_someip_88
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Session ID is a unique identifier chosen by the client for each call.
    
.. feat_req:: 🎯
    :id: feat_req_someip_700
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If session handling is not used, the Session ID shall be set to 0x0000.
    
.. feat_req:: 🎯
    :id: feat_req_someip_649
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If session handling is used, the Session ID shall start with 0x0001.
    
.. feat_req:: 🎯
    :id: feat_req_someip_677
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
When the Session ID reaches 0xFFFF, it shall start with 0x0001 again.
    
.. feat_req:: 🎯
    :id: feat_req_someip_669
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Request/Response methods shall use session handling.
    
.. feat_req:: 🎯
    :id: feat_req_someip_667
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Events, notification events, and Fire&Forget methods shall use session handling if required by the application.

This could be for example because of functional safety reasons or because SOME/IP-TP is required (see SOME/IP-TP).
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_668
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The handling of the Request ID in SOME/IP-SD messages is discussed later in this specification. See SOME/IP-SD.
    
.. heading:: Protocol Version [8 bit]
    :id: feat_req_someip_89
    :layout: focus
    :style: clean

Protocol Version [8 bit]
======================== 

.. feat_req:: 🎯
    :id: feat_req_someip_90
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Protocol Version is an 8 bit field containing the SOME/IP protocol version, which currently shall be set to 0x01.
    
.. heading:: Interface Version [8 bit]
    :id: feat_req_someip_91
    :layout: focus
    :style: clean

Interface Version [8 bit]
========================= 

.. feat_req:: 🎯
    :id: feat_req_someip_92
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Interface Version is an 8 bit field that contains the Major Version of the Service Interface.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_93
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Rationale:
This is required to catch mismatches in Service definitions and allows debugging tools to identify the Service Interface used, if versioning is used.
    
.. heading:: Message Type [8 bit]
    :id: feat_req_someip_94
    :layout: focus
    :style: clean

Message Type [8 bit]
==================== 

.. feat_req:: 🎯
    :id: feat_req_someip_95
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Message Type field is used to differentiate different types of messages and shall contain one of the following values:
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_684
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
List of supported Message Types.
    


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
        - EXCEPTION
        - The response containing an error
      * - 0xC0
        - RESPONSE ACK
        - Acknowledgment for RESPONSE (informational)
      * - 0xC1
        - EXCEPTION ACK
        - Acknowledgment for ERROR (informational)

.. feat_req:: 🎯
    :id: feat_req_someip_141
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Regular request (message type 0x00) will be answered by a response (message type 0x80), when no error occurred. If errors occur a regular response message with a return code not equal to 0 will be sent. This could be a response message (0x80) or an exception message (message type 0x81). It is also possible to send a request that does not have a response message (message type 0x01). For updating values through notification a callback interface exists (message type 0x02).
    
.. feat_req:: 🎯
    :id: feat_req_someip_726
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If no EXCEPTION message (message type 0x81) is configured, errors shall only be transported in regular RESPONSE messages (message type 0x80).
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_142
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For all messages an optional acknowledgment (ACK) exists. ACKs have the 0x40 bit of the Message Type set to one, while the regular Message Types do not.

ACKs are currently reserved but not used.
    
.. feat_req:: 🎯
    :id: feat_req_someip_761
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The 3rd highest bit of the Message Type (=0x20) shall be called TP-Flag and shall be set to 1 to signal that the current SOME/IP message is a segment. The other bits of the Message Type are set as specified in this Section.

For further information about SOME/IP-TP see SOME/IP-TP :need:`feat_req_someiptp_759`.

Note:
Segments of the Message Type Request (0x00) have the Message Type (0x20), segments of the Message Type Response (0x80) have the Message Type (0xa0), and so on.
    
.. heading:: Return Code [8 bit]
    :id: feat_req_someip_143
    :layout: focus
    :style: clean

Return Code [8 bit]
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
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_683
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
List of allowed Return Codes.
    


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
      * - EXCEPTION
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
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_166
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Best practice:

The size of the SOME/IP payload field depends on the transport protocol used. With UDP the SOME/IP payload should be between 0 and 1400 bytes.

The limitation to 1400 bytes is needed in order to allow for future changes to protocol stack (e.g. changing to IPv6 or adding security means). Since TCP supports segmentation of payloads, larger sizes are automatically supported.
    
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
  
The interface specification defines the exact position of all parameters in the PDU and has to consider the memory alignment. The serialization shall not try to automatically align parameters but shall be aligned as specified in the interface specification.

The SOME/IP payload should be placed in memory so that the SOME/IP payload is suitable aligned. For infotainment ECUs an alignment of 8 bytes (i.e. 64 bits) should be achieved, for all ECU at least an alignment of 4 bytes shall be achieved.
    
.. feat_req:: 🎯
    :id: feat_req_someip_711
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Alignment is always calculated from start of SOME/IP message.

Note:
If a parameter has to be aligned to x bytes, padding shall be inserted so that the relative position from start of the SOME/IP message (i.e. the position of the first header byte) modulo x equals 0.
    
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
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_682
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
List of supported basic datatypes.
    


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
      * - uint64
        - unsigned Integer
        - 64
        - not supported on all platforms, see [:need:`feat_req_someip_623`]
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
      * - sint64
        - signed Integer
        - 64
        - not supported on all platforms, see [:need:`feat_req_someip_623`]
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
  
The byte Order is specified for each parameter by the interface definition.
    
.. feat_req:: 🎯
    :id: feat_req_someip_623
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Uint64 and sint64 types shall be supported at least on infotainment ECUs.
    
.. feat_req:: 🎯
    :id: feat_req_someip_817
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Booleans shall only use the lowest bit. All other bits are reserved (i.e. shall be set to 0 on sending and shall ignore values on receiving).
    
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
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_652
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
So if for example a struct includes an uint8 and an uint32, they are just written sequentially into the buffer. This means that there is no padding between the uint8 and the first byte of the uint32; therefore, the uint32 might not be aligned.
    
.. feat_req:: 🎯
    :id: feat_req_someip_577
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If a SOME/IP generator or similar encounters an interface specification that leads to an PDU not correctly aligned (e.g. because of an unaligned struct), the SOME/IP generator shall warn about a misaligned struct but shall not fail in generating the code.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_671
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Warning about unaligned structs or similar shall not be done in the implementation but only in the tool chain used to generate the implementation.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_672
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Messages of legacy busses like CAN and FlexRay are usually not aligned. Warnings can be turned off or be ignored in such cases.
    
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
  
The interface specification may add a length field of 8, 16 or 32 bits in front of the Struct.
    
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
  
The length field of the struct describes the number of bytes of the struct. If the length is greater than the length of the struct as specified in the Interface Definition only the bytes specified in the Interface Specification shall be interpreted and the other bytes shall be skipped based on the length field.

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
  
Strings are encoded using Unicode and are terminated with a “\0”-character despite having a fixed length. The length of the string (this includes the “\0”) in bytes has to be specified in the interface definition. Fill unused space using “\0”.
    
.. feat_req:: 🎯
    :id: feat_req_someip_234
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Different Unicode encoding shall be supported including UTF-8, UTF-16BE, and UTF-16LE. Since these encoding have a dynamic length of bytes per character, the maximum length in bytes is up to six times the length of characters in UTF-8 plus 1 byte for the termination with a “\0” or two times the length of the characters in UTF-16 plus 2 bytes for a “\0”.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_687
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
:need:`feat_req_someip_234` states that an UTF-8 character can be up to 6 bytes and an UTF-16 character can be up to 4 bytes.
    
.. feat_req:: 🎯
    :id: feat_req_someip_639
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
UTF-16LE and UTF-16BE strings shall be zero terminated with a "\0" character. This means they shall end with (at least) two 0x00 bytes.
    
.. feat_req:: 🎯
    :id: feat_req_someip_640
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
UTF-16LE and UTF-16BE strings shall have an even length.
    
.. feat_req:: 🎯
    :id: feat_req_someip_641
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For UTF-16LE and UTF-16BE strings having a odd length the last byte shall be ignored. The two bytes before shall be 0x00 bytes (termination).
    
.. feat_req:: 🎯
    :id: feat_req_someip_662
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
All strings shall always start with a Byte Order Mark (BOM). The BOM shall be included in fixed-length-strings as well as dynamic-length strings.
    
.. feat_req:: 🎯
    :id: feat_req_someip_800
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The BOM counts towards the length of the string.
    
.. feat_req:: 🎯
    :id: feat_req_someip_666
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The receiving SOME/IP implementation shall check the BOM against the Interface Specification and might need to handle this as an error based on this specification.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_665
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The BOM may be added by the application or the SOME/IP implementation.
    
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
  
Strings with dynamic length start with a length field. The length is measured in bytes and is followed by the “\0”-terminated string data. The interface definition shall also define the maximum number of bytes of the string (including termination with “\0”).
    
.. feat_req:: 🎯
    :id: feat_req_someip_642
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
:need:`feat_req_someip_639`, :need:`feat_req_someip_640`, and :need:`feat_req_someip_641` shall also be valid for strings with dynamic length.
    
.. feat_req:: 🎯
    :id: feat_req_someip_582
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Dynamic length strings shall have a length field of 8, 16, 32 bit. This length is defined by the Interface Specification.

Note:
Fixed length strings may be seen as having a 0 bit length field.
    
.. feat_req:: 🎯
    :id: feat_req_someip_581
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If not specified otherwise in the interface specification the length of the length field is 32 bit (default length of length field).
    
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
  
If the interface definition states the alignment of the next data element the string shall be extended with “\0” characters to meet the alignment.
    
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
  
The length of fixed length arrays is defined by the interface definition.

Note:
They can be seen as repeated elements. Fixed length arrays are easier for use in very small devices.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_694
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In :need:`feat_req_someip_253` dynamic length arrays are shown, which can be also used. However, dynamic length arrays might need more resources on the ECU using them.
    
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

    
.. heading:: Optional Parameters / Optional Elements
    :id: feat_req_someip_251
    :layout: focus
    :style: clean

Optional Parameters / Optional Elements
======================================= 

.. feat_req:: ⓘ 
    :id: feat_req_someip_252
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Optional Elements shall be encoded as array with 0 to 1 elements. For the serialization of arrays with dynamic length see :need:`feat_req_someip_253`.
    
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
  
The layout of arrays with dynamic length basically is based on the layout of fixed length arrays. To determine the size of the array the serialization adds a length field (default length: 32 bits) in front of the data, which counts the bytes of the array. The length does not include the size of the length field. Thus, when transporting an array with zero elements the length is set to zero.
    
.. feat_req:: 🎯
    :id: feat_req_someip_621
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The Interface Definition shall define the length of the length field. Length of 0, 8, 16, and 32 bits are allowed.

If the length of the length field is set to 0 bits, the number of elements in the array has to be fixed; thus, being an array with fixed length. 
    
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
  
In the one-dimensional array one length field is used, which carries the number of bytes used for the array.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_674
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The number of static length elements can be easily calculated by dividing by the size of an element.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_673
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In the case of dynamical length elements the number of elements cannot be calculated but the elements must be parsed sequentially.
    
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
  
If static buffer size allocation is required, the interface definition shall define the maximal length of each dimension.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_696
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
:need:`feat_req_someip_260` even supports that different length columns and different length rows in the same dimension. See k_1 and k_2 in Figure :need:`feat_req_someip_258`.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_261
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Rationale:
When measuring the length in bytes, complex multi-dimensional arrays can be skipped over in deserialization.
    
.. heading:: Enumeration
    :id: feat_req_someip_650
    :layout: focus
    :style: clean

Enumeration
=========== 

.. feat_req:: 🎯
    :id: feat_req_someip_651
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The interface definition might specify an enumeration based on unsigned integer datatypes (uint8, uint16, uint32, uint64).
    
.. feat_req:: 🎯
    :id: feat_req_someip_799
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall support sending and receiving undefined enumeration values, if not configured otherwise.
    
.. heading:: Bitfield
    :id: feat_req_someip_688
    :layout: focus
    :style: clean

Bitfield
======== 

.. feat_req:: 🎯
    :id: feat_req_someip_689
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Bitfields shall be transported as basic datatypes uint8/uint16/uint32.
    
.. feat_req:: 🎯
    :id: feat_req_someip_690
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The interface definition shall be able to define the name of each bit.
    
.. feat_req:: 🎯
    :id: feat_req_someip_691
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The interface definition shall be able to define the names of the values a bit can be set to.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_692
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Each SOME/IP implementation may choose to de/serialize a bitfield or hand up the uint8/uint16/uint32 to the application.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_693
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A SOME/IP implementation may allow turning the de/serialization of a bitfield on or off. This means that only the uint8/uint16/uint32 value would be passed to an application.
    
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
  
A union (also called variant) is a parameter that can contain different types of elements. For example, if one defines a union of type uint8 and type uint16, the union shall carry an element of uint8 or uint16.

It is clear that that when using different types of elements with different length the alignment of subsequent parameters is possibly distorted. To resolve this, padding might be needed.
    
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
  
The order of the length and type field is adjustable by the interface specification. If this is not specified the default layout as in :need:`feat_req_someip_264` shall be used.
    
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
  
A length of the length field of 0 bits means that no length field will be written to the PDU.
    
.. feat_req:: 🎯
    :id: feat_req_someip_572
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the length of the length field is 0 bits, all types in the union shall be of the same length.
    
.. feat_req:: 🎯
    :id: feat_req_someip_583
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If the interface specification defines a union with a length field of 0 bits and types with different length, a SOME/IP implementation shall warn about this and use the length of the longest element and pad all others with zeros (0x00).
    
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
  
The length field defines the size of the element and padding in bytes and does not include the size of the length field and type field.
    
.. feat_req:: 🎯
    :id: feat_req_someip_564
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The length of the type field may be defined by the Interface Specification and shall be 32, 16, or 8 bits.
    
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
  
The type field describes the type of the element. Possible values of the type field are defined by the interface specification for each union separately. The types are encoded as in the interface specification in ascending order starting with 1. The 0 is reserved for the NULL type – i.e. an empty union. The Interface Definition shall allow or disallow the usage of NULL for a Union/Variant.
    
.. feat_req:: 🎯
    :id: feat_req_someip_274
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The element is serialized depending on the type in the type field. This also defines the length of the data. All bytes behind the data that are covered by the length, are padding. The deserializer shall skip such bytes according to the length field. The value of the length field for each type shall be defined by the interface specification.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_275
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
By using a struct different padding layouts can be achieved.
    
.. heading:: Example:  Union of uint8/uint16 both padded to 32 bits
    :id: feat_req_someip_276
    :layout: focus
    :style: clean

Example:  Union of uint8/uint16 both padded to 32 bits
------------------------------------------------------ 

.. feat_req:: ⓘ 
    :id: feat_req_someip_277
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
In this example a length of the length field is specified as 32 bits. The union shall support a uint8 and a uint16 as elements. Both are padded to the 32 bit boundary (length=4 bytes).
    
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
    
.. feat_req:: 🎯
    :id: feat_req_someip_648
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If a server runs different instances of the same service, messages belonging to different service instances shall be mapped to the service instance by the transport protocol port on the server side.
    
.. feat_req:: 🎯
    :id: feat_req_someip_702
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
All Transport Protocol Bindings shall support transporting more than one SOME/IP message in a Transport Layer PDU (i.e. UDP packet or TCP segment). This is called nPDU feature and support shall cover receiving and sending.
    
.. feat_req:: 🎯
    :id: feat_req_someip_741
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
If an ECU has a cyclic send task (meaning it sends only every x ms), the ECU shall support the nPDU feature even without configuration to minimize the number of IP packets transporting SOME/IP messages.

Note:
The nPDU feature works only on SOME/IP messages using the same socket. This requirement does not mean to combine SOME/IP messages of different sockets.
    
.. feat_req:: 🎯
    :id: feat_req_someip_664
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The receiving SOME/IP implementation shall be capable of receiving unaligned SOME/IP messages transported by UDP or TCP.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_663
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Rationale for :need:`feat_req_someip_664`: When transporting multiple SOME/IP payloads in UDP or TCP the alignment of the payloads can be only guaranteed, if the length of every payloads is a multiple of the alignment size (e.g. 32 bits).
    
.. feat_req:: 🎯
    :id: feat_req_someip_732
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Every ECU (independent of the number of controllers, cores, and IP addresses) shall support the internal de/multiplexing of SOME/IP messages, so that SOME/IP messages do not need to be sent more than once to this ECU and the maximum efficiency can be achieved (this means that the ECU transports all SOME/IP messages to/from another ECU on exactly a single port number pair).
    
.. feat_req:: 🎯
    :id: feat_req_someip_733
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The port numbers for the protocol bindings are defined by the configuration data files (e.g. FIBEX or ARXML).
    
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
  
The UDP binding of SOME/IP is straight forward by transporting SOME/IP messages in UDP packets. The SOME/IP messages shall not be fragmented. Therefore care shall be taken that SOME/IP messages are not too big, i.e. up to 1400 bytes of SOME/IP payload. Messages with bigger payload shall not be transported over UDP but with TCP or SOME/IP-TP see :need:`feat_req_someiptp_759`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_319
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The header format allows transporting more than one SOME/IP message in a single UDP packet. The SOME/IP implementation shall identify the end of a SOME/IP message by means of the SOME/IP length field. Based on the UDP length field, SOME/IP shall determine if there are additional SOME/IP messages in the UDP packet.
    
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
    
.. feat_req:: 🎯
    :id: feat_req_someip_811
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The UDP Binding shall support unicast and multicast transmission depending on the configuration.
    
.. feat_req:: 🎯
    :id: feat_req_someip_812
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The UDP Binding shall support multicast eventgroups with initial events of fields being transported via unicast.
    
.. feat_req:: 🎯
    :id: feat_req_someip_814
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP clients shall support receiving via unicast and/or via multicast depending on the configuration and SOME/IP-SD.
    
.. feat_req:: 🎯
    :id: feat_req_someip_813
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The UDP Binding shall support dynamic switching of eventgroups between unicast and multicast based on the number of subscriptions and the configuration parameter Multicast-Threshold:

* Multicast-Threshold=0: Unicast only
* Multicast-Threshold=1: Multicast only
* Multicast-Threshold>1: with number of subscribed clients < Multicast-Threshold use unicast, else multicast.
    
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
  
The TCP binding of SOME/IP is heavily based on the UDP binding. In contrast to the UDP binding, the TCP binding allows much bigger SOME/IP messages and uses the robustness features of TCP (coping with loss, reorder, duplication, etc.).
    
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
  
When the TCP connection is lost, outstanding requests shall be handled as timeouts. Since TCP handles reliability, additional means of reliability are not needed. Error handling is discussed in detail in :need:`feat_req_someip_364`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_644
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The client and server shall use a single TCP connection for all methods, events, and notifications of a service instance. When having more than one instance of a service a TCP connection per services instance is needed.
    
.. feat_req:: 🎯
    :id: feat_req_someip_645
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The TCP connection shall be used for as many services as possible to minimize the number of TCP connections between the client and the server (basically only one connection per TCP port of server).
    
.. feat_req:: 🎯
    :id: feat_req_someip_646
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The TCP connection shall be opened by the client, when the first method call shall be transport or the client wants to receive the first notifications.
    
.. feat_req:: 🎯
    :id: feat_req_someip_647
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The client is responsible for reestablishing the TCP connection whenever it fails.
    
.. feat_req:: 🎯
    :id: feat_req_someip_678
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The TCP connection shall be closed by the client, when the TCP connection is not required anymore.
    
.. feat_req:: 🎯
    :id: feat_req_someip_679
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The TCP connection shall be closed by the client, when all Services using the TCP connections are not available anymore (stopped or timed out).
    
.. feat_req:: 🎯
    :id: feat_req_someip_680
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The server shall not stop the TCP connection when stopping all services the TCP connection was used for but give the client enough time to process the control data to shutdown the TCP connection itself.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_681
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Rational for :need:`feat_req_someip_680`: When the server closes the TCP connection before the client recognized that the TCP is not needed anymore, the client will try to reestablish the TCP connection.
    
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
  
Each TCP segment shall start with a SOME/IP Magic Cookie Message.
    
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
* Protocol Version as specified above (:need:`feat_req_someip_90`)
* Interface Version = 0x01
* Message Type = 0x01 (for Client to Server Communication) or  0x02 (for Server to Client Communication)
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
    :id: feat_req_someip_636
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Service-Instances of the same Service are identified through different Instance IDs. It shall be supported that multiple Service-Instances reside on different ECUs as well as multiple Service-Instances of one or more Services reside on one single ECU.
    
.. feat_req:: 🎯
    :id: feat_req_someip_445
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
While different Services shall be able to share the same port number of the transport layer protocol used, multiple Service-Instances of the same service on one single ECU shall listen on different ports per Service-Instance.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_637
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Rational for :need:`feat_req_someip_445`: While Instance IDs are used for Service Discovery, they are not contained in the SOME/IP header.
    
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

.. feat_req:: ⓘ 
    :id: feat_req_someip_328
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
One of the most common communication patterns is the request/response pattern. One communication partner (in the following called the client) sends a request message, which is answered by another communication partner (the server).
    
.. feat_req:: 🎯
    :id: feat_req_someip_329
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
For the SOME/IP request message the client has to do the following for payload and header:

* Construct the payload
* Set the Message ID based on the method the client wants to call
* Set the Length field to 8 bytes (for the part of the SOME/IP header after length field) + length of the serialized payload
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
  
The server builds its header based on the header of the client and does in addition:

* Construct the payload
* Set the length to the 8 bytes + new payload size
* Set the Message Type to RESPONSE (i.e. 0x80) or EXCEPTION (i.e. 0x81)
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
  
Fire&Forget messages shall not return an error. Error handling shall be implemented by the application when needed.
    
.. heading:: Events
    :id: feat_req_someip_351
    :layout: focus
    :style: clean

Events
****** 

.. feat_req:: ⓘ 
    :id: feat_req_someip_352
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Events describe a general Publish/Subscribe-Concept. Usually the server publishes a service and the client subscribes to one of the services eventgroups. On certain events the server will send the client an event, which could be for example an updated value or an event that occurred.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_353
    :reqtype: Information
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
  
When more than one subscribed client on the same ECU exists, the system shall handle the replication of events in order to save transmissions on the communication medium. This is especially important, when events are transported using multicast messages.
    
.. feat_req:: 🎯
    :id: feat_req_someip_804
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP implementations should support sending events (but not notification events of fields) to a subset of the subscribed clients.
    
.. feat_req:: 🎯
    :id: feat_req_someip_806
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Sending events to a subset of the subscribed clients shall be controlled by the application.
    
.. feat_req:: 🎯
    :id: feat_req_someip_807
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Events shall not be sent to clients that are not subscribed.

Note:
Events sent via multicast are not sent to the client but to the multicast addresses; therefore, multicast communication is not affected by this requirement.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_808
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
When designing a service with selective event sending, make sure that this works even if the feature is not supported by the sender.

Example with using a handle:

* Client A <-> Server: Request-Response-Call (parameters) returns (handle1, ...)
* Client A <-> Server: Request-Response-Call (parameters) returns (handle2, ...)
* Client B <-> Server: Request-Response-Call (parameters) returns (handle3, ...)
* Server -> Client A: Selective Event E1 (handle2, ...)

If Event E1 is being sent to all clients instead of only Client A, Client B could filter based on the handle; thus, compatibility is not broken. Only efficiency is lowered.

    
.. heading:: Strategy for sending notifications
    :id: feat_req_someip_355
    :layout: focus
    :style: clean

Strategy for sending notifications
================================== 

.. feat_req:: ⓘ 
    :id: feat_req_someip_356
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
For different use cases different strategies for sending notifications are possible and shall be defined in the service interface. The following examples are common:

* Cyclic update – send an updated value in a fixed interval (e.g. every 100 ms for safety relevant messages with Alive)
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
  
A field shall be a combination of an optional getter, an optional setter, and an optional notifier.
    
.. feat_req:: 🎯
    :id: feat_req_someip_632
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A field without a setter and without a getter and without a notifier shall not exist.
    
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
  
The setter of a field shall be a request/response call that has the desired value of the field in the payload of the request message and the value that was set to the field in the payload of the response message.

Note:
If the value of the request payload was adapted (e.g. because it was out of limits) the adapted value will be transported in the response payload.
    
.. feat_req:: 🎯
    :id: feat_req_someip_635
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The notifier shall send a notification event message that transports the value of a field on change and follows the rules for events.
    
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
  
For the error handling two different mechanisms are supported. All messages have a return code field to carry the return code. However, only responses (Message Types 0x80 and 0x81) use this field to carry a return code to the request (Message Type 0x00) they answer. All other messages set this field to 0x00. See :need:`feat_req_someip_94`.

For more detailed errors the layout of the Exception Message (Message Type 0x81) can carry specific fields for error handling, e.g. an Exception String. Exception Messages can be only sent instead of Response Messages, if configured.
    
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
    :id: feat_req_someip_727
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
A SOME/IP message with a return code unequal 0x00 is called error message. The message type can be RESPONSE or EXCEPTION.
    
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
    :id: feat_req_someip_654
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The system shall not return an error message for fire&forget methods.
    
.. feat_req:: 🎯
    :id: feat_req_someip_655
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For request/response methods the error message shall copy over the fields of the SOME/IP header (i.e. Message ID, Request ID, and Interface Version) but not the payload. In addition Message Type and Return Code have to be set to the appropriate values.
    
.. feat_req:: 🎯
    :id: feat_req_someip_703
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The SOME/IP implementation shall not use an unknown protocol version but write a supported protocol version in the header.
    
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
        - E_UNKNOWN_SERVICE (optional)
        - The requested Service ID is unknown.
      * - 0x03
        - E_UNKNOWN_METHOD (optional)
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
        - E_WRONG_PROTOCOL_VERSION (obsolete)
        - Version of SOME/IP protocol not supported
      * - 0x08
        - E_WRONG_INTERFACE_VERSION
        - Interface version mismatch
      * - 0x09
        - E_MALFORMED_MESSAGE
        - Deserialization error, so that payload cannot be deserialized.
      * - 0x0a 
        - E_WRONG_MESSAGE_TYPE 
        - An unexpected message type was received (e.g. REQUEST_NO_RETURN for a method defined as REQUEST.)
      * - | 0x0b
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
    
.. feat_req:: 🎯
    :id: feat_req_someip_721
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
The SOME/IP message shall be checked in the following order:

* Length field >= 8?
* Protocol Version supported?
* Service ID supported?
* Interface Version of this service supported?
* Method ID supported?
* Message Type supported?
* Message Type as specified in IDL?
* Payload parseable?
    
.. feat_req:: 🎯
    :id: feat_req_someip_704
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Implementations shall not answer with errors to SOME/IP message already carrying an error (i.e. return code is not equal to 0x00).
    
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
    
.. heading:: Error Processing Overview
    :id: feat_req_someip_717
    :layout: focus
    :style: clean

Error Processing Overview
========================= 

.. feat_req:: 🎯
    :id: feat_req_someip_719
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Figure :need:`feat_req_someip_718` shows the SOME/IP error handling as an example flow chart. This does not include the application based error handling but just covers the error handling in messaging and RPC.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_720
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
Important things that are reflected in this flow chart:

* Error handling is based on the message type received (e.g. only methods can be answered with a return code).
* Errors shall be checked in a defined order (see :need:`feat_req_someip_721`).
    
.. feat_req:: 🎯
    :id: feat_req_someip_718
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP Error Handling

.. drawsvg_directive:: images/drawsvg/feat_req_someip_718.py

    
.. feat_req:: 🎯
    :id: feat_req_someip_816
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The error codes E_UNKNOWN_SERVICE and E_UNKNOWN_METHOD are optional. This means they may be sent on Request messages of Request/Response methods, if the Service ID or the Method-ID are wrong.
    
.. feat_req:: 🎯
    :id: feat_req_someip_818
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The error code E_WRONG_PROTOCOL_VERSION is obsolete since it should be only sent, if the Version of SOME/IP changed (meaning the header layout) and the message type is Request. This cannot be implemented correctly.
    
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

.. rst-class:: compact
  
When considering the transport of RPC messages different reliability semantics exist:

* Maybe – the message might reach the communication partner
* At least once – the message reaches the communication partner at least once
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
  
While different implementations may implement different approaches, SOME/IP currently achieves “maybe” reliability when using the UDP Bindings including SOME/IP-TP and “exactly once” reliability when using the TCP binding. Further error handling is left to the application.
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_436
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
For “maybe” reliability, only a single timeout is needed, when using request/response communication in combination of UDP as transport protocol. Figure :need:`feat_req_someip_437` shows the state machines for “maybe” reliability. The client’s SOME/IP implementation has to wait for the response for a specified timeout. If the timeout occurs SOME/IP shall signal E_TIMEOUT to the client application.
    
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
  
SOME/IP directly supports the two most used transport protocols of the Internet: User Datagram Protocol (UDP) and Transmission Control Protocol (TCP). While UDP is a very lean transport protocol supporting only the most important features (multiplexing and error detecting using a checksum), TCP adds additional features for achieving a reliable communication. TCP can not only handle bit errors but also segmentation, loss, duplication, reordering, and network congestion; thus, TCP is the more powerful transport protocol.
    
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
  
* Use TCP only if very large chunks of data need to be transported (> 1400 bytes) and no hard latency requirements in the case of errors exists
    
.. feat_req:: ⓘ 
    :id: feat_req_someip_456
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
* Try using external transport or transfer mechanisms (Network File System, APIX link, 1722, …) when more suited for the use case. In this case SOME/IP can transport a file handle or a comparable identifier. This gives the designer additional freedom (e.g. in regard to caching).
    
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
  
* Add an offset field to every message. The ID of an array element will be calculated by adding the offset to its position in the array. Keep in mind that the offset needs to be carefully chosen. If for example every message can contain up to ten data structures (0-9), the offset could be chosen as 0, 10, 20, 30, and so on.
    
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
  
As for all serialization formats migration towards a newer service interface is limited. Using a set of compatibility rules, SOME/IP allows for evolution of service interfaces. One can do the following additions and enhancements in a non-breaking way:
    
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
  
* If exception is unknown, “unknown exception” needs to be thrown. The exception description string however can be used.
    
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
  
Not all of these changes can be introduced at the client or server side first. In some cases only the client or server can be changed first. For example, when sending an additional parameter with a newer implementation, the older implementation can only skip this parameter.
    
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
  
* Need to add default value at receiver first and parameters need to be at end of list
    
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
  
* Replace supertype by subtype (as in object oriented programming languages with inheritance)
    
.. heading:: Transporting CAN and FlexRay Frames
    :id: feat_req_someip_500
    :layout: focus
    :style: clean

.. rst-class:: break_before

Transporting CAN and FlexRay Frames
################################### 

.. feat_req:: ⓘ 
    :id: feat_req_someip_501
    :reqtype: Information
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
SOME/IP allows to tunnel of CAN and FlexRay frames as well. However, the Message ID space needs to be coordinated between both use cases.
    
.. feat_req:: 🎯
    :id: feat_req_someip_502
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The full SOME/IP Header shall be used for transporting/tunneling CAN/FlexRay.
    
.. feat_req:: 🎯
    :id: feat_req_someip_504
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
The AUTOSAR Socket-Adapter uses the Message ID and Length to construct the needed internal PDUs but does not look at other fields. Therefore, the CAN ID (11 or 29 bits) and/or the FlexRay ID (6+6+11 bits) have to be encoded into the Message ID field. The CAN ID shall be aligned to the least significant bit of the Message ID. An 11 bit CAN identifier would be therefore transported in the bit position 21 to 31. Refer also to :need:`feat_req_someip_620`
    
.. feat_req:: 🎯
    :id: feat_req_someip_505
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Especially with the use of 29 bit CAN-IDs or FlexRay-IDs a lot of the Message ID space is used. In this case it is recommended to bind SOME/IP and CAN/FlexRay transports to different transport protocol ports, so that different ID spaces for the Message IDs exist.
    
.. feat_req:: 🎯
    :id: feat_req_someip_506
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Keep in mind that when transporting a CAN frame of 8 byte over Ethernet an overhead of up to 100 bytes might be needed in the near future (using IPv6 and/or security mechanisms). So it is recommended to use larger RPC calls as shown in the first part of the document instead of small CAN like communication.
    
.. feat_req:: 🎯
    :id: feat_req_someip_567
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Client ID and Session ID shall be set to 0x0000.
    
.. feat_req:: 🎯
    :id: feat_req_someip_606
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Depending on the direction, the Message Type shall be set to 0x02 (service provider sends) or 0x00 (service provider receives). The Return Code shall be always set to 0x00.
    
.. feat_req:: 🎯
    :id: feat_req_someip_638
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
At least for 11 bit CAN-IDs the layout of the Message ID shall be followed :need:`feat_req_someip_60` and :need:`feat_req_someip_67`. This means that the 16th bit from the left shall be set to 0 or 1 according to the Message ID (0x00 or 0x02).
    
.. feat_req:: 🎯
    :id: feat_req_someip_568
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Protocol Version shall be set according to :need:`feat_req_someip_90`.
    
.. feat_req:: 🎯
    :id: feat_req_someip_569
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True
  
Interface Version shall be set according to interface specifications.
    
.. feat_req:: 🎯
    :id: feat_req_someip_620
    :reqtype: Requirement
    :security: TBD
    :safety: TBD
    :satisfies: 
    :status: valid
    :collapse: True

.. rst-class:: compact
  
If SOME/IP is used for transporting CAN messages with 11 bits of CAN-ID, the following layout of the Message ID is recommended (example):

* Service ID shall be set to a value defined by theOEM, e.g. 0x1234
* Event ID is split into 4 bits specifying the CAN bus, and 11 bits for the CAN-ID.

This is just an example and the actual layout shall be specified by the System Department.
    