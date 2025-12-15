
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

SOME/IP Service Discovery (SOME/IP-SD)
######################################

.. heading:: SOME/IP Service Discovery (SOME/IP-SD)
   :id: feat_req_someipsd_1
   :h: 1


General
*******

.. heading:: General
   :id: feat_req_someipsd_182
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_183
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP-SD is used to locate service instances and to detect if service instances are running
   as well as implementing the Publish/Subscribe handling.

.. feat_req::
   :id: feat_req_someipsd_184
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Inside the vehicular network service instance locations are commonly known; therefore,
   the state of the service instance is of primary concern. The location of the service
   (i.e. IP-Address, transport protocol and port number) are of secondary concern.

.. heading:: Terms and Definitions
   :id: feat_req_someipsd_2
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_497
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The terms and definitions of SOME/IP RPC shall apply for SOME/IP-SD as well.
   See :need:`feat_req_someip_14` and :need:`feat_req_someipsd_351`.

.. feat_req::
   :id: feat_req_someipsd_351
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Terms and Definitions

   .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      *  -  Term
         -  Definition
      *  -  Offering a service instance
         -  Offering a service instance shall mean that one ECU implements an instance of a service and tells other ECUs using SOME/IP-SD that they may use it.
      *  -  Finding a service instance
         -  Finding a service instance shall mean to send a SOME/IP-SD message in order to find a needed service instance.
      *  -  Subscribing to an eventgroup
         -  Subscribing an eventgroup shall mean that a client requests a server to send the content of an eventgroup of a service instance using a SOME/IP-SD message.
      *  -  unicast event
         -  Events and Field notifiers, which are transmitted via unicast. The IP and Port Numbers of the sender are defined by the endpoint options of the offered service instance. The IP and Port Numbers are defined by the endpoint options of the subscribe eventgroup by the client.
      *  -  multicast event
         -  Events and field notifiers which are transmitted via multicast. The IP and Port Number of the sender are defined by the endpoint option of the offered service instance. The IP and Port Numbers are defined by the multicast endpoint option.
      *  -  server multicast endpoint
         -  Multicast endpoint (including IP multicast address, port, and protocol) provided by the server to announce where the server service transmits multicast events to. This is SOME/IP feature since the beginning and is supported by all SOME/IP implementations.
      *  -  client unicast endpoint
         -  Unicast endpoint (including IP multicast address, port, and protocol) provided by the client service to announce where the client service expects to receive unicast events from the corresponding server service.
      *  -  client multicast endpoint
         -  Multicast endpoint (including IP multicast address, port, and protocol) provided by the client service to announce where the client service expects to receive events from the corresponding server service. This could be used alternatively to a client unicast endpoint. Note: This is currently an AUTOSAR proprietary extension to SOME/IP. Other SOME/IP standards may only allow Servers to sent Multicast Endpoints.
      *  -  Security Association
         -  The protected connection or association based on a security protocol, like IPsec or MACsec. This also includes the state of the security protocol. Note: While this only somewhat also applies to TLS and DTLS, in the following TLS and DTLS are included, when the term is used.
      *  -  Secured Port
         -  A TCP or UDP Port that is protected by a security protocol based on a Security Association.

SOME/IP-SD ECU-internal Interface
*********************************

.. heading:: SOME/IP-SD ECU-internal Interface
   :id: feat_req_someipsd_13
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_17
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Service status shall be defined as up or down as well as required and released:

   *  A service status of up shall mean that a service instance is available; thus,
      it is accessible using the communication method specified and is able to fulfill its specified function.
   *  A service status of down shall mean the opposite of the service status up.
   *  A service status of required shall mean that service instance is needed by another software
      component in the system to function.
   *  A service status of released shall mean the opposite of the service status required.
   *  The combination of service status up/down with required/released shall be supported.
      Four different valid combinations shall exist (up+required, up+released, down+required, down+released).

.. feat_req::
   :id: feat_req_someipsd_14
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD ECU-internal Interface shall inform local software components about the status of remote services (up/down).

.. feat_req::
   :id: feat_req_someipsd_18
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD ECU-internal Interface shall offer the option to local software component to
   require or release a remote service instance.

.. feat_req::
   :id: feat_req_someipsd_16
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD ECU-internal Interface shall inform local software components of the
   require/release status of local services.

.. feat_req::
   :id: feat_req_someipsd_22
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD ECU-internal Interface shall offer the option to local software component to set
   a local service status (up/down).

.. feat_req::
   :id: feat_req_someipsd_203
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Eventgroup status shall be defined in the same way the service status is defined.

.. feat_req::
   :id: feat_req_someipsd_204
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP-SD shall be used to turn on/off the events and notification events of a given eventgroup.
   Only if another ECU requires an eventgroup, the events and notification events of this eventgroup
   are sent (See SubscribeEventgroup).

.. feat_req::
   :id: feat_req_someipsd_23
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP-SD shall be informed of link-up and link-down events of logical, virtual,
   and physical communication interfaces that the SOME/IP-SD is bound to.

.. feat_req::
   :id: feat_req_someipsd_1184
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For ECUs with included Ethernet Switch, the link-up and link-down shall be based solely on
   switch ports transporting SOME/IP-SD for this instance of SOME/IP-SD.
   If at least one such switch port has a link, this shall be considered as link-up.
   If exactly all such switch ports do not have a link, this is considered as link-down.

.. feat_req::
   :id: feat_req_someipsd_1221
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If an Ethernet port cannot be used after link-up of the PHY due to security functions
   (e.g. 802.1X) or similar, this port shall not be considered as link-up by SOME/IP-SD until
   the security function enables communication.

SOME/IP-SD Message Format
*************************

.. heading:: SOME/IP-SD Message Format
   :id: feat_req_someipsd_24
   :h: 2

General Requirements
====================

.. heading:: General Requirements
   :id: feat_req_someipsd_96
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_27
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP-SD messages shall be supported over UDP.

.. feat_req::
   :id: feat_req_someipsd_26
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP-SD Messages shall start with a SOME/IP header as depicted Figure :need:`feat_req_someipsd_205`:

   *  SOME/IP-SD messages shall use the Service ID (16 bits) of 0xFFFF.
   *  SOME/IP-SD messages shall use the Method ID (16 bits) of 0x8100.
   *  SOME/IP-SD messages shall use a uint32 length field as specified by SOME/IP. That means that
      the length is measured in bytes and starts with the first byte after the length field and ends
      with the last byte of the SOME/IP-SD message.
   *  SOME/IP-SD messages shall have a Client ID (16 bits) and handle it based on SOME/IP rules.
   *  The Client ID shall be set to 0, since there exists only a single SOME/IP-SD instance.
   *  If a Client ID Prefix is configured, it shall also apply to SOME/IP-SD.
   *  SOME/IP-SD messages shall have a Session ID (16 bits) and handle it based on the SOME/IP requirements.
   *  The Session ID (SOME/IP header) shall be incremented for every sent SOME/IP-SD message.
   *  The Session ID (SOME/IP header) shall start with 1 and be 1 even after wrapping.
   *  The Session ID (SOME/IP header) shall not be set to 0.
   *  SOME/IP-SD Session ID handling is done per "communication relation", i.e. broadcast as well
      as unicast per peer (see :need:`feat_req_someipsd_41`).

   *  Note: This means that the first SD message sent out to the multicast address has
      Session ID 0x0001 as well as the first SD message sent out to any unicast communication partner
      has the Session ID 0x0001 as well.

   *  SOME/IP-SD messages shall have a Protocol Version (8 bits) of 0x01.
   *  SOME/IP-SD messages shall have an Interface Version (8 bits) of 0x01.
   *  SOME/IP-SD messages shall have a Message Type (8 bits) of 0x02 (Notification).
   *  SOME/IP-SD messages shall have a Return Code (8 bits) of 0x00 (E_OK).

.. feat_req::
   :id: feat_req_someipsd_205
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD Header Format

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_205.json


SOME/IP-SD Header
=================

.. heading:: SOME/IP-SD Header
   :id: feat_req_someipsd_97
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_38
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After the SOME/IP header the SOME/IP-SD Header shall follow as depicted in Figure :need:`feat_req_someipsd_205`.

.. feat_req::
   :id: feat_req_someipsd_39
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD Header shall start out with an 8 bit field called Flags.

.. feat_req::
   :id: feat_req_someipsd_40
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The first flag of the SOME/IP-SD Flags field (highest order bit) shall be called Reboot Flag.

.. feat_req::
   :id: feat_req_someipsd_41
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Reboot Flag of the SOME/IP-SD Header shall be set to one for all messages after reboot until
   the Session ID in the SOME/IP-Header wraps around and thus starts with 1 again.
   After this wrap around the Reboot Flag is set to 0.

.. feat_req::
   :id: feat_req_someipsd_765
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The information for the reboot flag and the Session ID shall be kept for multicast and unicast
   separately as well as for every sender-receiver-relation (i.e. source address and destination address).

   Note: This means you have to store a counter for Multicast sending and one counter per Unicast
   peer as well as two counters (1x Multicast, 1x Unicast) per SOME/IP-SD peer for receiving.

.. feat_req::
   :id: feat_req_someipsd_863
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP-SD implementations shall reliably detect the reboots of their peer based on the
   information stated in :need:`feat_req_someipsd_765`.

.. feat_req::
   :id: feat_req_someipsd_764
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The detection of a reboot shall be done as follows (with new the values of the current packet
   from the communication partner and old the last value received before):

   *  if old.reboot==0 and new.reboot==1 then Reboot detected
   *  if old.reboot==1 and new.reboot==1 and old.session_id>=new.session_id then Reboot detected

   The following is not enough since we do not have reliable communication:

   *  if new.reboot==1 and old.session_id>=new.session_id then Reboot detected

.. feat_req::
   :id: feat_req_someipsd_871
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When the system detects the reboot of a peer, it shall update its state accordingly.
   Services and Subscriptions shall be expired if they are not updated again.

.. feat_req::
   :id: feat_req_someipsd_872
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When the system detects the reboot of a peer, it shall reset the state of the TCP connections to
   this peer. The client shall reestablish the TCP as required by the Publish/Subscribe process later.

.. feat_req::
   :id: feat_req_someipsd_87
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The second flag of the SOME/IP-SD Flags (second highest order bit) shall be called Unicast Flag
   and shall be set to 1, if SD message reception via unicast is supported.

.. feat_req::
   :id: feat_req_someipsd_100
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Unicast Flag of the SOME/IP-SD Header shall be always set to Unicast (that means 1)
   for all SD Messages since this means that receiving using unicast is supported.

.. feat_req::
   :id: feat_req_someipsd_1187
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The third flag (third highest order bit) of the SOME/IP-SD Flags shall be defined as
   the Explicit Initial Data Control Flag. This flag indicates whether the ECU is capable of
   processing initial data requests signaled via the ‘Initial Data Requested’ flag inside Eventgroup Entries.

   Note: Most of the SOME/IP implementations do not support this flag.

.. feat_req::
   :id: feat_req_someipsd_1188
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Explicit Initial Data Control Flag shall be set to ‘1’ in the SOME/IP-SD header only
   when the sending ECU supports this feature. Otherwise, the flag shall be set to ‘0’.
   A receiving ECU must check the Explicit Initial Data Control Flag of the sending ECU.
   If the sending ECU has set the flag to ‘1’, the receiving ECU shall process the
   ‘Initial Data Requested’ flag within Eventgroup Entries, otherwise, shall ignore the
   ‘Initial Data Requested’ flag and operate using its default initial data handling mechanism.

.. feat_req::
   :id: feat_req_someipsd_1180
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Undefined bits within the Flag field shall be set to ‘0’ when sending and ignored on receiving.

.. feat_req::
   :id: feat_req_someipsd_42
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After the Flags the SOME/IP-SD Header shall have a field of 24 bits called Reserved that is set to 0 until further notice.

.. feat_req::
   :id: feat_req_someipsd_101
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After the SOME/IP-SD Header the Entries Array shall follow.

.. feat_req::
   :id: feat_req_someipsd_862
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The entries shall be processed exactly in the order they arrive.

.. feat_req::
   :id: feat_req_someipsd_1170
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   :need:`feat_req_someipsd_862` shall not lead to closing and reopening a socket because of a
   single SOME/IP-SD message. The socket shall stay open in this case.

.. feat_req::
   :id: feat_req_someipsd_103
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After the Entries Array in the SOME/IP-SD Header an Option Array shall follow.

.. feat_req::
   :id: feat_req_someipsd_44
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Entries Array and the Options Array of the SOME/IP-SD message shall start with a length
   field as uint32 that counts the number of bytes of the following data; i.e. the entries or the options.

Entry Format
============

.. heading:: Entry Format
   :id: feat_req_someipsd_94
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_771
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD shall work on different entries that shall be carried in the SOME/IP-SD messages.
   The entries are used to synchronize the state of services instances and the Publish/Subscribe handling.

.. feat_req::
   :id: feat_req_someipsd_46
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Two types of entries exist: A Service Entry Type for Services and an Eventgroup Entry Type
   for Eventgroups, which are used for different entries each.

.. feat_req::
   :id: feat_req_someipsd_47
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A Service Entry Type shall be 16 bytes of size and include the following fields in this order as
   shown in Figure :need:`feat_req_someipsd_208`:

   *  Type Field [uint8]: encodes FindService (0x00) and OfferService (0x01).
   *  Index First Option Run [uint8]: Index of this runs first option in the option array.
   *  Index Second Option Run [uint8]: Index of this runs first option in the option array.
   *  Number of Options 1 [uint4]: Describes the number of options the first option run uses.
   *  Number of Options 2 [uint4]: Describes the number of options the second option run uses.
   *  Service ID [uint16]: Describes the Service ID of the Service or Service-Instance this entry is concerned with.
   *  Instance ID [uint16]: Describes the Service Instance ID of the Service Instance this entry is
      concerned with or is set to 0xFFFF if all service instances of a service are meant.
   *  Major Version [uint8]: Encodes the major version of the service (instance).
   *  TTL [uint24]: Describes the lifetime of the entry in seconds.
   *  Minor Version [uint32]: Encodes the minor version of the service.

.. feat_req::
   :id: feat_req_someipsd_208
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD Service Entry Type

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_208.json


.. feat_req::
   :id: feat_req_someipsd_109
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   An Eventgroup Entry shall be 16 bytes of size and include the following fields in this order as
   shown in Figure :need:`feat_req_someipsd_209`:

   *  Type Field [uint8]: encodes Subscribe (0x06) and SubscribeAck (0x07).
   *  Index First Option Run [uint8]: Index of this runs first option in the option array.
   *  Index Second Option Run [uint8]: Index of this runs first option in the option array.
   *  Number of Options 1 [uint4]: Describes the number of options the first option run uses.
   *  Number of Options 2 [uint4]: Describes the number of options the second option run uses.
   *  Service ID [uint16]: Describes the Service ID of the Service or Service-Instance this entry is concerned with.
   *  Instance ID [uint16]: Describes the Service Instance ID of the Service Instance this entry is
      concerned with or is set to 0xFFFF if all service instances of a service are meant.
   *  Major Version [uint8]: Encodes the major version of the service instance this eventgroup is part of.
   *  TTL [uint24]: Describes the lifetime of the entry in seconds.
   *  Reserved [uint8]: Shall be set to 0x00, if not specified otherwise
      (see :need:`feat_req_someipsd_614` and :need:`feat_req_someipsd_619`).
   *  Initial Data Requested Flag [1 bit] (I Flag): Shall be set to 1, if initial data shall be sent by the server.
   *  Reserved2 [uint3]: Shall be set to 0x0, if not specified otherwise
      (see :need:`feat_req_someipsd_614` and :need:`feat_req_someipsd_619`).
   *  Counter [uint4]: Is used to differentiate identical SubscribeEventgroups. Set to 0x0 if not used.
   *  Eventgroup ID [uint16]: Transports the ID of an Eventgroup.

.. feat_req::
   :id: feat_req_someipsd_209
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD Service Entry Type

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_209.json


Options Format
==============

.. heading:: Options Format
   :id: feat_req_someipsd_104
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_772
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Options are used to transport additional information to the entries.
   This includes for instance the information how a service instance is reachable
   (IP-Address, Transport Protocol, Port Number).

.. feat_req::
   :id: feat_req_someipsd_122
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   In order to identify the option type every option shall start with:

   *  Length [uint16]: Specifies the length of the option in bytes.
   *  Type [uint8]: Specifying the type of the option.

.. feat_req::
   :id: feat_req_someipsd_133
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The length field shall cover all bytes of the option except the length field and type field.

Configuration Option
-------------------- 

.. heading:: Configuration Option
   :id: feat_req_someipsd_139
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_755
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The configuration option shall be used to transport arbitrary configuration strings.
   This allows to encode additional information like the name of a service or its configuration.

.. feat_req::
   :id: feat_req_someipsd_152
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The format of the Configuration Option shall be as follows:

   *  Length [uint16]: Shall be set to the total number of bytes occupied by the configuration option,
      excluding the 16 bit length field and the 8 bit type flag.
   *  Type [uint8]: Shall be set to 0x01.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  ConfigurationString [dynamic length]: Shall carry the configuration string.

.. feat_req::
   :id: feat_req_someipsd_149
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Configuration Option shall specify a set of name-value-pairs based on the DNS TXT and DNS-SD
   (https://www.ietf.org/rfc/rfc6763.txt) format.

.. feat_req::
   :id: feat_req_someipsd_150
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The format of the configuration string shall start with a single byte length field that describes
   the number of bytes following this length field.

.. feat_req::
   :id: feat_req_someipsd_151
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After each character sequence another length field and a following character sequence are expected
   until a length field set to 0x00.

.. feat_req::
   :id: feat_req_someipsd_158
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After a length field set to 0x00 no characters follow.

.. feat_req::
   :id: feat_req_someipsd_159
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A character sequence shall encode a key and an optionally a value.

.. feat_req::
   :id: feat_req_someipsd_157
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The character sequences shall contain an equal character ("=", 0x03D) to divide key and value.

.. feat_req::
   :id: feat_req_someipsd_162
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The key shall not include an equal character and shall be at least one non-whitespace character.
   The characters of "Key" shall be printable US-ASCII values (0x20-0x7E), excluding '=' (0x3D).

.. feat_req::
   :id: feat_req_someipsd_161
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The "=" shall not be the first character of the sequence.

.. feat_req::
   :id: feat_req_someipsd_160
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For a character sequence without an '=' that key shall be interpreted as present.

.. feat_req::
   :id: feat_req_someipsd_217
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For a character sequence ending on an '=' that key shall be interpreted as present with empty value.

.. feat_req::
   :id: feat_req_someipsd_684
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Multiple entries with the same key in a single Configuration Option shall be supported.

.. feat_req::
   :id: feat_req_someipsd_218
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The configuration option shall be also used to encode hostname, servicename, and instancename (if needed).

.. feat_req::
   :id: feat_req_someipsd_201
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_144` shows the format of the Configuration Option and
   Figure :need:`feat_req_someipsd_147` an example for the Configuration Option.

.. feat_req::
   :id: feat_req_someipsd_144
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD Configuration Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_144.json


.. feat_req::
   :id: feat_req_someipsd_147
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD Configuration Option Example

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_147.json

Load Balancing Option (informational)
-------------------------------------

.. heading:: Load Balancing Option (informational)
   :id: feat_req_someipsd_145
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_754
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   This option shall be used to prioritize different instances of a service, so that a client
   chooses the service instance based on these settings. This option will be attached to OfferService entries.

.. feat_req::
   :id: feat_req_someipsd_146
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The Load Balancing Option shall use the Type 0x02.

.. feat_req::
   :id: feat_req_someipsd_174
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The Load Balancing Option shall carry a Priority and Weight like the DNS-SRV records,
   which shall be used to load balancing different service instances.

.. feat_req::
   :id: feat_req_someipsd_770
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   This means when looking for all service instances of a service (Service Instance set to 0xFFFF),
   the client shall choose the service instance with highest priority.
   When having more than one service instance with highest priority (lowest value in Priority field)
   the service instance shall be chosen randomly based on the weights of the service instances.

.. feat_req::
   :id: feat_req_someipsd_175
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The Format of the Load Balancing Option shall be as follows:

   *  Length [uint16]: Shall be set to 0x0005.
   *  Type [uint8]: Shall be set to 0x02.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  Priority [uint16]: Carries the Priority of this instance. Lower value means higher priority.
   *  Weight [uint16]: Carries the Weight of this instance. Large value means higher probability to be chosen.

.. feat_req::
   :id: feat_req_someipsd_200
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_148` shows the format of the Load Balancing Option.

.. feat_req::
   :id: feat_req_someipsd_148
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD Load Balancing Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_148.json


IPv4 Endpoint Option
--------------------

.. heading:: IPv4 Endpoint Option
   :id: feat_req_someipsd_126
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_752
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 Endpoint Option shall be used by a SOME/IP-SD instance to signal the relevant endpoint(s).
   Endpoints include the local IP address, the transport layer protocol (e.g. UDP or TCP),
   and the port number of the sender.

   These ports shall be used for the events and notification events as well.
   When using UDP the server uses the announced port as source port.
   With TCP the client needs to open a connection to this port before subscription,
   because this is the TCP connection the server uses for sending events and notification events.

.. feat_req::
   :id: feat_req_someipsd_127
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 Endpoint Option shall use the Type 0x04.

.. feat_req::
   :id: feat_req_someipsd_128
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 Endpoint Option shall specify the IPv4-Address,
   the transport layer protocol (ISO/OSI layer 4) used, and its Port Number.

.. feat_req::
   :id: feat_req_someipsd_129
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Format of the IPv4 Endpoint Option shall be as follows:

   *  Length [uint16]: Shall be set to 0x0009.
   *  Type [uint8]: Shall be set to 0x04.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  IPv4-Address [uint32]: Shall transport the IP-Address as four bytes.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol (ISO/OSI layer 4)
      based on the IANA/IETF types (0x06: TCP, 0x11: UDP).
   *  Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the port of
      the transport layer protocol (ISO/OSI layer 4).

.. feat_req::
   :id: feat_req_someipsd_199
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_141` shows the format of the IPv4 Endpoint Option.

.. feat_req::
   :id: feat_req_someipsd_141
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD IPv4 Endpoint Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_141.json


.. feat_req::
   :id: feat_req_someipsd_849
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The server shall use the IPv4 Endpoint Option with OfferService entries to signal the endpoints
   it serves the service on. That is up to one UDP endpoint and up to one TCP endpoint.

.. feat_req::
   :id: feat_req_someipsd_850
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The endpoints the server referenced by an OfferService entry shall also be used as source of events.
   That is source IP address and source port numbers for the transport protocols in the endpoint option.

.. feat_req::
   :id: feat_req_someipsd_848
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The client shall use the IPv4 Endpoint Option with SubscribeEventgroup entries to signal its IP
   address and its UDP and/or TCP port numbers, on which it is ready to receive the events.

IPv6 Endpoint Option
--------------------

.. heading:: IPv6 Endpoint Option
   :id: feat_req_someipsd_138
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_751
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 Endpoint Option shall be used by a SOME/IP-SD instance to signal the relevant endpoint(s).
   Endpoints include the local IP address, the transport layer protocol (e.g. UDP or TCP),
   and the port number of the sender.

   These ports shall be used for the events and notification events as well. When using UDP
   the server uses the announced port as source port. With TCP the client needs to open a connection
   to this port before subscription, because this is the TCP connection the server uses for sending
   events and notification events.

.. feat_req::
   :id: feat_req_someipsd_140
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 Endpoint Option shall use the Type 0x06.

.. feat_req::
   :id: feat_req_someipsd_163
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 Endpoint Option shall specify the IPv6-Address, the Layer 4 Protocol used, and the Layer 4 Port Number.

.. feat_req::
   :id: feat_req_someipsd_164
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The Format of the IPv6 Endpoint Option shall be as follows:

   *  Length [uint16]: Shall be set to 0x0015.
   *  Type [uint8]: Shall be set to 0x06.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  IPv6-Address [uint128]: Shall transport the IP-Address as 16 bytes.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  L4-Proto [uint8]: Shall be set to the transport layer protocol (ISO/OSI layer 4) based on the
      IANA/IETF types (0x06: TCP, 0x11: UDP).
   *  L4-Port [uint16]: Shall be set to the port of the transport layer protocol (ISO/OSI layer 4).

.. feat_req::
   :id: feat_req_someipsd_197
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_142` shows the format of the IPv6 Endpoint Option.

.. feat_req::
   :id: feat_req_someipsd_142
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD IPv6 Endpoint Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_142.json


.. feat_req::
   :id: feat_req_someipsd_851
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The server shall use the IPv6 Endpoint Option with OfferService entries to signal the endpoints
   the services is available on. That is up to one UDP endpoint and up to one TCP endpoint.

.. feat_req::
   :id: feat_req_someipsd_852
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The endpoints the server referenced by an OfferService entry shall also be used as source of events.
   That is source IP address and source port numbers for the transport protocols in the endpoint option.

.. feat_req::
   :id: feat_req_someipsd_853
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The client shall use the IPv6 Endpoint Option with SubscribeEventgroup entries to signal the
   IP address and the UDP and/or TCP port numbers, on which it is ready to receive the events.

IPv4 Multicast Option
---------------------

.. heading:: IPv4 Multicast Option
   :id: feat_req_someipsd_722
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_749
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 Multicast Option is used by the server to announce the IPv4 multicast address,
   the transport layer protocol (ISO/OSI layer 4), and the port number the multicast events and
   multicast notification events are sent to. As transport layer protocol currently only UDP is supported.

.. feat_req::
   :id: feat_req_someipsd_854
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 Multicast Option and not the IPv4 Endpoint Option shall be referenced by SubscribeEventgroupAck entries.

.. feat_req::
   :id: feat_req_someipsd_723
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 Multicast Option shall use the Type 0x14.

.. feat_req::
   :id: feat_req_someipsd_724
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 Multicast Option shall specify the IPv4-Address, the transport layer protocol
   (ISO/OSI layer 4) used, and its Port Number.

.. feat_req::
   :id: feat_req_someipsd_725
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Format of the IPv4 Endpoint Option shall be as follows:

   *  Length [uint16]: Shall be set to 0x0009.
   *  Type [uint8]: Shall be set to 0x14.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  IPv4-Address [uint32]: Shall transport the multicast IP-Address as four bytes.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol
      (ISO/OSI layer 4) based on the IANA/IETF types (0x11: UDP).
   *  Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the port of the layer 4 protocol.

.. feat_req::
   :id: feat_req_someipsd_733
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_734` shows the format of the IPv4 Multicast Option.

.. feat_req::
   :id: feat_req_someipsd_734
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD IPv4 Multicast Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_734.json


.. feat_req::
   :id: feat_req_someipsd_855
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If a service supports IPv4 Multicast, the offer entry shall reference the IPv4 Multicast Option,
   which encodes the IPv4 Multicast Address and Port Number the server will send multicast events and
   notification events to.

IPv6 Multicast Option
---------------------

.. heading:: IPv6 Multicast Option
   :id: feat_req_someipsd_736
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_750
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 Multicast Option is used by the server to announce the IPv6 multicast address,
   the layer 4 protocol, and the port number the multicast events and multicast notifications
   events are sent to. For the transport layer protocol (ISO/OSI layer 4) currently only UDP is supported.

.. feat_req::
   :id: feat_req_someipsd_1083
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 Multicast Option and not the IPv6 Endpoint Option shall be referenced by SubscribeEventgroupAck messages.

.. feat_req::
   :id: feat_req_someipsd_737
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 Multicast Option shall use the Type 0x16.

.. feat_req::
   :id: feat_req_someipsd_738
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 Multicast Option shall specify the IPv6-Address, the transport layer protocol
   (ISO/OSI layer 4) used, and its Port Number.

.. feat_req::
   :id: feat_req_someipsd_739
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The Format of the IPv6 Multicast Option shall be as follows:

   *  Length [uint16]: Shall be set to 0x0015.
   *  Type [uint8]: Shall be set to 0x16.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  IPv6-Address [uint128]: Shall transport the multicast IP-Address as 16 bytes.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol
      (ISO/OSI layer 4) based on the IANA/IETF types (0x11: UDP).
   *  Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the port of the
      transport layer protocol (ISO/OSI layer 4).

.. feat_req::
   :id: feat_req_someipsd_747
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_748` shows the format of the IPv6 Multicast Option.

.. feat_req::
   :id: feat_req_someipsd_748
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD IPv6 Multicast Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_748.json


.. feat_req::
   :id: feat_req_someipsd_856
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   If a service supports IPv6 Multicast, the Offer Service Entry shall reference the IPv6 Multicast Option,
   which encodes the IPv6 Multicast Address and Port Number the server will send multicast events and
   notification events to.

IPv4 SD Endpoint Option
-----------------------

.. heading:: IPv4 SD Endpoint Option
   :id: feat_req_someipsd_1080
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_1081
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 SD Endpoint Option is used to transport the endpoint (i.e. IP-Address and Port) of
   the senders SD implementation.

.. feat_req::
   :id: feat_req_someipsd_1082
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 SD Endpoint Option shall be included in any SD Options Array up to 1 time.

.. feat_req::
   :id: feat_req_someipsd_1156
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 SD Endpoint Option shall only be included if the SOME/IP-SD message is transported over IPv4.

.. feat_req::
   :id: feat_req_someipsd_1151
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 SD Endpoint Option shall be the first option in the options array, if existing.

.. feat_req::
   :id: feat_req_someipsd_1152
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If more than one IPv4 SD Endpoint Option is received, only the first one shall be processed and
   all further IPv4 SD Endpoint Options shall be ignored.

.. feat_req::
   :id: feat_req_someipsd_1114
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 SD Endpoint Option shall be not referenced by any SD Entry.

.. feat_req::
   :id: feat_req_someipsd_1084
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the IPv4 SD Endpoint Option is included in the SD message, the receiving SD implementation
   shall use the content of this option instead of the Source IP Address and Source Port.
   This is important for responding to the received SD message (e.g. OfferService after FindService or
   SubscribeEventgroup after OfferService or SubscribeEventgroupAck after SubscribeEventgroup)
   as well as the reboot detection (channel based on SD Endpoint Option and not out addresses).

.. feat_req::
   :id: feat_req_someipsd_1085
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 SD Endpoint Option shall use the Type 0x24.

.. feat_req::
   :id: feat_req_someipsd_1086
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IPv4 SD Endpoint Option shall specify the IPv4-Address, the transport layer protocol
   (ISO/OSI layer 4) used, and its Port Number.

.. feat_req::
   :id: feat_req_someipsd_1087
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Format of the IPv4 SD Endpoint Option shall be as follows:

   *  Length [uint16]: Shall be set to 0x0009.
   *  Type [uint8]: Shall be set to 0x24.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  IPv4-Address [uint32]: Shall transport the unicast IP-Address of SOME/IP-SD as four bytes.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol of
      SOME/IP-SD (currently: 0x11 UDP).
   *  Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the transport layer port of
      SOME/IP-SD (currently: 30490).

.. feat_req::
   :id: feat_req_someipsd_1095
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_1096` shows the format of the IPv4 SD Endpoint Option.

.. feat_req::
   :id: feat_req_someipsd_1096
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD IPv4 SD Endpoint Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_1096.json


IPv6 SD Endpoint Option
-----------------------

.. heading:: IPv6 SD Endpoint Option
   :id: feat_req_someipsd_1097
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_1098
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 SD Endpoint Option is used to transport the endpoint (i.e. IP-Address and Port) of the
   senders SD implementation.

.. feat_req::
   :id: feat_req_someipsd_1099
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 SD Endpoint Option shall be included in any SD message up to 1 time.

.. feat_req::
   :id: feat_req_someipsd_1155
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 SD Endpoint Option shall only be included if the SOME/IP-SD message is transported over IPv6.

.. feat_req::
   :id: feat_req_someipsd_1153
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 SD Endpoint Option shall be the first option in the options array, if existing.

.. feat_req::
   :id: feat_req_someipsd_1154
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   If more than one IPv6 SD Endpoint Option is received, only the first one shall be processed and
   all further IPv6 SD Endpoint Options shall be ignored.

.. feat_req::
   :id: feat_req_someipsd_1113
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 SD Endpoint Option shall be not referenced by any SD Entry.

.. feat_req::
   :id: feat_req_someipsd_1100
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   If the IPv6 SD Endpoint Option is included in the SD message, the receiving SD implementation
   shall use the content of this option instead of the Source IP Address and Source Port for
   responding to these SD messages.
   This is important for responding to the received SD messages (e.g. OfferService after FindService or
   SubscribeEventgroup after OfferService or SubscribeEventgroupAck after SubscribeEventgroup)
   as well as the reboot detection (channel based on SD Endpoint Option and not out addresses).

.. feat_req::
   :id: feat_req_someipsd_1101
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 SD Endpoint Option shall use the Type 0x26.

.. feat_req::
   :id: feat_req_someipsd_1102
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The IPv6 SD Endpoint Option shall specify the IPv4-Address, the transport layer protocol
   (ISO/OSI layer 4) used, and its Port Number.

.. feat_req::
   :id: feat_req_someipsd_1103
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The Format of the IPv6 SD Endpoint Option shall be as follows:

   *  Length [uint16]: Shall be set to 0x0015.
   *  Type [uint8]: Shall be set to 0x26.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  IPv6-Address [uint128]: Shall transport the unicast IP-Address of SOME/IP-SD as 16 bytes.
   *  Reserved [uint8]: Shall be set to 0x00.
   *  Transport Protocol (L4-Proto) [uint8]: Shall be set to the transport layer protocol of
      SOME/IP-SD (currently: 0x11 UDP).
   *  Transport Protocol Port Number (L4-Port) [uint16]: Shall be set to the transport layer port of
      SOME/IP-SD (currently: 30490).

.. feat_req::
   :id: feat_req_someipsd_1111
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_1112` shows the format of the IPv6 SD Endpoint Option.

.. feat_req::
   :id: feat_req_someipsd_1112
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD IPv6 SD Endpoint Option Type

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_1112.json


MAC-Groupcast Endpoint Option
-----------------------------

.. heading:: MAC-Groupcast Endpoint Option
   :id: feat_req_someipsd_1248
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_1249
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The MAC-Groupcast Endpoint Option is used to announce the MAC-groupcast address layer 2 groupcast
   traffic is sent to, the data link layer protocol and a protocol-specific identifier.

.. feat_req::
   :id: feat_req_someipsd_1250
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   As the MAC-Groupcast Endpoint Option announces non-SOME/IP service instances,
   it shall only be used together with a Configuration Option containing an otherserv-string.

.. feat_req::
   :id: feat_req_someipsd_1251
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The MAC-Groupcast Endpoint Option shall use the Type 0x15.

.. feat_req::
   :id: feat_req_someipsd_1252
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The MAC-Groupcast Endpoint Option shall specify the MAC-groupcast address, the data link layer
   protocol (L2-Proto) used and a variable length protocol-specific identifier (ProtoSpecific)
   related to the used link layer protocol.

.. feat_req::
   :id: feat_req_someipsd_1253
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Format of the MAC-Groupcast Endpoint Option shall be as follows:

   *  Length [uint16]: Dynamic, depending on the content of the ProtoSpecific field which in turn
      depends on the L2-Proto field.

      *  Example: For IEEE1722 the ProtoSpecific field contains the 6+2 Byte long Stream-ID, so the Length is to be set to 0x11.

   *  Type [uint8]: Shall be set to 0x15.
   *  Reserved [uint8]: Shall be set to 0x00 on transmission.
   *  GroupMAC-Address [uint48]: Shall transport the 6 byte MAC-Groupcast Address.
   *  Data Link Protocol (L2-Proto) [uint16]: Shall be set to the data link layer protocol
      (ISO/OSI layer 2) based on the IANA/IETF Ethertypes.

      *  Example: For IEEE1722 0x22F0 shall be used.

   *  Protocol-specific identifier (ProtoSpecific): Dynamic length, related to the data link layer protocol.

      *  Example: For IEEE1722 ProtoSpecific shall be set to the Stream-ID [uint64] of the
         announced IEEE1722 stream.

.. feat_req::
   :id: feat_req_someipsd_1262
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: Format of the MAC-Groupcast Endpoint Option

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_1262.json


Referencing Options from Entries
================================

.. heading:: Referencing Options from Entries
   :id: feat_req_someipsd_335
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_336
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Using the following fields of the entries, options are referenced by the entries:

   *  Index First Option Run: Index into array of options for first option run. Index 0 means first of SOME/IP-SD packet.
   *  Index Second Option Run: Index into array of options for second option run. Index 0 means first of SOME/IP-SD packet.
   *  Number of Options 1: Length of first option run. Length 0 means no option in option run.
   *  Number of Options 2: Length of second option run. Length 0 means no option in option run.

.. feat_req::
   :id: feat_req_someipsd_341
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Two different option runs exist: First Option Run and Second Option Run.

.. feat_req::
   :id: feat_req_someipsd_346
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Rationale for the support of two option runs: Two different types of options are expected:
   options common between multiple SOME/IP-SD entries and options different for each SOME/IP-SD entry.
   Supporting two different options runs is the most efficient way to support these two types of
   options, while keeping the wire format highly efficient.

.. feat_req::
   :id: feat_req_someipsd_342
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Each option run shall reference the first option and the number of options for this run.

.. feat_req::
   :id: feat_req_someipsd_343
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the number of options is set to zero, the option run is considered empty.

.. feat_req::
   :id: feat_req_someipsd_348
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For empty runs the Index (i.e. Index First Option Run and/or Index Second Option Run) shall be set to zero.

.. feat_req::
   :id: feat_req_someipsd_347
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Implementations shall accept and process incoming SD messages with option run length set to zero and option index not set to zero.

.. feat_req::
   :id: feat_req_someipsd_900
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Implementations shall minimize the size of the SD messages by not duplicating Options without need.

Handling missing, redundant and conflicting Options
---------------------------------------------------

.. heading:: Handling missing, redundant and conflicting Options
   :id: feat_req_someipsd_1140
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_1142
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If an entry references an unknown option, this option shall be ignored.

.. feat_req::
   :id: feat_req_someipsd_1141
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If an entry references a redundant option (option that is not needed by this specific entry),
   this option shall be ignored.

.. feat_req::
   :id: feat_req_someipsd_1143
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Example: A Service needs only a TCP Endpoint but Endpoint Options for UDP and TCP are referenced
   by the OfferService entry. UDP endpoint shall be ignored.

.. feat_req::
   :id: feat_req_someipsd_1144
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If an entry references two or more options that are in conflict, this entry shall be responded
   negatively, if possible(e.g. Subscribe Eventgroup). If no answer is expected, ignore the entry
   and its options.

.. feat_req::
   :id: feat_req_someipsd_1145
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Example: An OfferService entry referencing two Endpoint Options stating two different UDP Ports
   shall be ignored.

   Example: A SubscribeEventgroup entry referencing two Endpoint Options stating two different
   UDP Ports shall be responded with a SubscribeEventgroupNack.

.. feat_req::
   :id: feat_req_someipsd_1146
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When two different Configuration Options are referenced by an entry, the configuration sets shall be merged.

.. feat_req::
   :id: feat_req_someipsd_1147
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the two Configuration Options have conflicting items (same name), all items shall be handled.
   There shall be no attempt been made to merge duplicate items.

Example
=======

.. heading:: Example
   :id: feat_req_someipsd_212
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_214
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_213` shows an example SOME/IP-SD PDU.

.. feat_req::
   :id: feat_req_someipsd_213
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD Example PDU

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_213.json


Service Discovery Messages
**************************

.. heading:: Service Discovery Messages
   :id: feat_req_someipsd_219
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_235
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Using the previously specified header format, different entries and messages consisting of one
   or more entries can be built. The specific entries and their header layouts are explained in
   the following sections.

.. feat_req::
   :id: feat_req_someipsd_256
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For all entries the following shall be true:

   *  Index First Option Run, Index Second Option Run, Number of Options 1,
      and Number of Options 2 shall be set according to the chained options.

Service Entries
=============== 

.. heading:: Service Entries
   :id: feat_req_someipsd_224
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_236
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Entries concerned with services shall be based on the Service Entry Type Format as specified in
   :need:`feat_req_someipsd_47`.

FindService Entry
-----------------

.. heading:: FindService Entry
   :id: feat_req_someipsd_220
   :h: 4

.. feat_req::
   :id: feat_req_someipsd_238
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The FindService entry type shall be used for finding service instances and shall only be sent,
   if the current state of a service is unknown (no current OfferService was received and is still valid).

.. feat_req::
   :id: feat_req_someipsd_239
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   FindService entries shall set the entry fields in the following way:

   *  Type shall be set to 0x00 (FindService).
   *  Service ID shall be set to the Service ID of the service that shall be found.
   *  Instance ID shall be set to 0xFFFF (=ANY), if all service instances shall be returned.
      It shall be set to the Instance ID of a specific service instance, if just a single service instance shall be returned.
   *  If an ECU uses Instance ID 0xFFFF (=ANY) for a Find Entry to find previously unknown number
      of Service Instances, it has to make sure that it sends out at least one Find entry, since it
      cannot determine based on the number of Offer Entries that it has already received all Offer Entries relevant.
   *  Major Version shall be set to the Major Version of the Service Interface to be found.
      The Major Version shall be set to 0xFF (=ANY), if Services of all Major Versions are to be found.
   *  Minor Version shall be set to 0xFFFF FFFF (=ANY); this means that services with any version shall be returned.
   *  If only a Service with a specific minor version needs to be found, the Minor Version shall
      be set to this specific value.
   *  Setting the Minor Version to 0xFFFF FFFF (=ANY) is the common behavior for FindService entries.
   *  For regular SOME/IP-SD (i.e. without central registry or similar) any FindService entry will
      be responded instantaneously. So all TTL values > 0 are equivalent.
   *  TTL shall be set to the lifetime of the FindService entry. After this lifetime the FindService
      entry shall be considered not existing.(Service Registry only).
   *  If set to 0xFFFFFF, the FindService entry shall be considered valid until the next reboot. (Service Registry only).
   *  TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.

OfferService Entry
------------------

.. heading:: OfferService Entry
   :id: feat_req_someipsd_221
   :h: 4

.. feat_req::
   :id: feat_req_someipsd_252
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The OfferService entry type shall be used to offer a service to other communication partners.

.. feat_req::
   :id: feat_req_someipsd_253
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   OfferService entries shall set the entry fields in the following way:

   *  Type shall be set to 0x01 (OfferService).
   *  Service ID shall be set to the Service ID of the service instance that is offered.
   *  Instance ID shall be set to the Instance ID of the service instance that is offered.
   *  Major Version shall be set to the Major Version of the service instance that is offered.
   *  Minor Version shall be set to the Minor Version of the service instance that is offered.
   *  TTL shall be set to the lifetime of the service instance that is offered.
      After this lifetime the service instance shall be considered as not offered.
   *  If set to 0xFFFFFF, the OfferService entry shall be considered valid until the next reboot.
   *  TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.

.. feat_req::
   :id: feat_req_someipsd_681
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   OfferService entries shall always reference at least an IPv4 or IPv6 Endpoint Option to
   signal how the service is reachable.

.. feat_req::
   :id: feat_req_someipsd_756
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For each Transport Layer Protocol needed for the service (i.e. UDP and/or TCP) an IPv4 Endpoint
   option shall be added, if IPv4 is supported.

.. feat_req::
   :id: feat_req_someipsd_757
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For each Transport Layer Protocol needed for the service (i.e. UDP and/or TCP) an IPv6 Endpoint
   option shall be added, if IPv6 is supported.

.. feat_req::
   :id: feat_req_someipsd_858
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The IP addresses and port numbers of the Endpoint Options shall also be used for transporting
   events and notification events:

.. feat_req::
   :id: feat_req_someipsd_758
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   In the case of UDP, the endpoint option is used for the source address and the source port of
   the events and notification events.

.. feat_req::
   :id: feat_req_someipsd_762
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   In the case of TCP, the endpoint option contains the IP address and port the client needs to
   open a TCP connection to in order to receive events using TCP.

StopOfferService Entry
----------------------

.. heading:: StopOfferService Entry
   :id: feat_req_someipsd_225
   :h: 4

.. feat_req::
   :id: feat_req_someipsd_261
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The StopOfferService entry type shall be used to stop offering service instances.

.. feat_req::
   :id: feat_req_someipsd_262
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   StopOfferService entries shall set the entry fields exactly like the OfferService entry they
   are stopping, except:

   * TTL shall be set to 0x000000.

Eventgroup Entries
==================

.. heading:: Eventgroup Entries
   :id: feat_req_someipsd_227
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_237
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Entries concerned with services follow the Eventgroup Entry Type Format as specified in
   :need:`feat_req_someipsd_109`.

SubscribeEventgroup Entry
-------------------------

.. heading:: SubscribeEventgroup Entry
   :id: feat_req_someipsd_230
   :h: 4

.. feat_req::
   :id: feat_req_someipsd_321
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SubscribeEventgroup entry type shall be used to subscribe to an eventgroup.

.. feat_req::
   :id: feat_req_someipsd_322
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SubscribeEventgroup entries shall set the entry fields in the following way:

   *  Type shall be set to 0x06 (SubscribeEventgroup).
   *  Service ID shall be set to the Service ID of the service instance that includes the eventgroup subscribed to.
   *  Instance ID shall be set to the Instance ID of the service instance that includes the eventgroup subscribed to.
   *  Major Version shall be set to the Major Version of the service instance of the eventgroup subscribed to.
   *  Eventgroup ID shall be set to the Eventgroup ID of the eventgroup subscribed to.
   *  Reserved shall be set to 0x00 until further notice.
   *  Initial Data Requested Flag shall be set to 1, if the client sends the first subscribe in
      sequence to trigger the sending of initial events. Set to 0, if not required otherwise
      (see :need:`feat_req_someipsd_1191` and following requirements).
   *  Reserved2 shall be set to three 0 bits.
   *  Counter shall be used to differentiate between parallel subscribes to the same eventgroup of
      the same service (only difference in endpoint). If not used, set to 0x0.
   *  TTL shall be set to the lifetime of the eventgroup. After this lifetime the eventgroup shall
      considered not been subscribed to.
   *  If set to 0xFFFFFF, the SubscribeEventgroup entry shall be considered valid until the next reboot.
   *  TTL shall not be set to 0x000000 since this is considered to be the Stop entry for this entry.

.. feat_req::
   :id: feat_req_someipsd_682
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SubscribeEventgroup entries shall reference one or two IPv4 and/or one or two IPv6 Endpoint
   Options (one for UDP, one for TCP).

StopSubscribeEventgroup Entry
-----------------------------

.. heading:: StopSubscribeEventgroup Entry
   :id: feat_req_someipsd_233
   :h: 4

.. feat_req::
   :id: feat_req_someipsd_332
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The StopSubscribeEventgroup entry type shall be used to stop subscribing to eventgroups.

.. feat_req::
   :id: feat_req_someipsd_333
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   StopSubscribeEventgroup entries shall set the entry fields exactly like the SubscribeEventgroup
   entry they are stopping, except:

   * TTL shall be set to 0x000000.

.. feat_req::
   :id: feat_req_someipsd_1177
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A StopSubscribeEventgroup Entry shall reference the same options the SubscribeEventgroup Entry
   referenced. This includes but is not limited to Endpoint and Configuration options.

Subscribe Eventgroup Acknowledgement (SubscribeEventgroupAck) Entry
-------------------------------------------------------------------

.. heading:: Subscribe Eventgroup Acknowledgement (SubscribeEventgroupAck) Entry
   :id: feat_req_someipsd_612
   :h: 4

.. feat_req::
   :id: feat_req_someipsd_613
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SubscribeEventgroupAck entry type shall be used to indicate that SubscribeEventgroup entry was accepted.

.. feat_req::
   :id: feat_req_someipsd_614
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SubscribeEventgroupAck entries shall set the entry fields in the following way:

   *  Type shall be set to 0x07 (SubscribeEventgroupAck).
   *  Service ID, Instance ID, Major Version, Eventgroup ID, TTL, Reserved, Initial Data Requested Flag,
      Reserved2 and Counter shall be the same values as in the SubscribeEventgroup that is being responded to.

.. feat_req::
   :id: feat_req_someipsd_763
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SubscribeEventgroupAck entries referencing events and notification events that are transported
   via multicast shall reference an IPv4 Multicast Option and/or and IPv6 Multicast Option.
   The Multicast Options state to which Multicast address and port the events and notification events will be sent to.

Subscribe Eventgroup Negative Acknowledgement (SubscribeEventgroupNack) Entry
-----------------------------------------------------------------------------

.. heading:: Subscribe Eventgroup Negative Acknowledgement (SubscribeEventgroupNack) Entry
   :id: feat_req_someipsd_617
   :h: 4

.. feat_req::
   :id: feat_req_someipsd_618
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SubscribeEventgroupNack entry type shall be used to indicate that SubscribeEventgroup entry was NOT accepted.

.. feat_req::
   :id: feat_req_someipsd_1137
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Reasons to not accept a SubscribeEventgroup include (but are not limited to):

   *  Combination of Service ID, Instance ID, Eventgroup ID, and Major Version is unknown
   *  Required TCP-connection was not opened by client
   *  Problems with the referenced options occurred
   *  Resource problems at the server
   *  Subscription was denied by Security or ACL

.. feat_req::
   :id: feat_req_someipsd_619
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SubscribeEventgroupNack entries shall set the entry fields in the following way:

   *  Type shall be set to 0x07 (SubscribeEventgroupAck).
   *  Service ID, Instance ID, Major Version, Eventgroup ID, Counter and Reserved shall be the same
      values as in the SubscribeEventgroup that is being responded to.
   *  The TTL shall be set to 0x000000.

.. feat_req::
   :id: feat_req_someipsd_869
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When the client receives a SubscribeEventgroupNack as response to a SubscribeEventgroup for which
   a TCP connection is required, the client shall check the TCP connection and shall restart the
   TCP connection if needed.

   Note: Checking the TCP connection may involve a TCP Keep Alive or a SOME/IP Magic Cookie Message.

.. feat_req::
   :id: feat_req_someipsd_870
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Rationale for :need:`feat_req_someipsd_869`:

   The server might have lost the TCP connection and the client has not.

   Checking the TCP connection might include the following:

   *  Checking whether data is received for e.g. other eventgroups.
   *  Sending out a Magic Cookie message and waiting for the TCP ACK.
   *  Reestablishing the TCP connection.

Service Discovery Communication Behavior
****************************************

.. heading:: Service Discovery Communication Behavior
   :id: feat_req_someipsd_25
   :h: 2

Startup Behavior
================

.. heading:: Startup Behavior
   :id: feat_req_someipsd_59
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_68
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For each Service Instance or Eventgroup the SOME/IP-SD shall have at least these three phases in
   regard to sending entries:

   *  Initial Wait Phase
   *  Repetition Phase
   *  Main Phase

.. feat_req::
   :id: feat_req_someipsd_864
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   An actual implemented state machine will need more than just states for these three phases.
   E.g. local services can be still down and remote services can be already known (no finds needed anymore).

.. feat_req::
   :id: feat_req_someipsd_72
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   As soon as the system has started and the link on one external interface needed for a Service
   Instance is up (server) or requested (client), the SOME/IP-SD enters the Initial Wait Phase
   for this service instance.

.. feat_req::
   :id: feat_req_someipsd_773
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

"The system has started" means that the needed applications as well as available external sensors and actuators have started and deliver valid data. Basically, the whole functionality needed by the service instance has to be ready to offer a service. Likewise, finding a service only makes sense after the application which requires the service is ready.

.. feat_req::
   :id: feat_req_someipsd_62
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD implementation shall wait based on the INITIAL_DELAY after entering the Initial
   Wait Phase and before sending the first messages for the Service Instance.

.. feat_req::
   :id: feat_req_someipsd_63
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   INITIAL_DELAY shall be defined as a minimum and a maximum delay.

.. feat_req::
   :id: feat_req_someipsd_64
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The wait time shall be determined by choosing a random value between the minimum and maximum of
   INITIAL_DELAY.

.. feat_req::
   :id: feat_req_someipsd_65
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD shall use the same random value for multiple entries of different types in order
   to pack them together for a reduced number of messages.

.. feat_req::
   :id: feat_req_someipsd_836
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD shall pack entries together no matter whether any delay is involved or not.
   For example, all SubscribeEventgroup entries of a message shall be responded combined in single
   message which carries all SubscribeEventgroupAck or SubscribeEventgroupNack entries, respectively.

.. feat_req::
   :id: feat_req_someipsd_66
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After sending the first message the Repetition Phase of this Service Instance/these Service
   Instances is entered.

.. feat_req::
   :id: feat_req_someipsd_67
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD implementation shall wait in the Repetition Phase based on REPETITIONS_BASE_DELAY.

.. feat_req::
   :id: feat_req_someipsd_76
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After each message sent in the Repetition Phase the delay shall be doubled.

.. feat_req::
   :id: feat_req_someipsd_73
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD shall send out only up to REPETITIONS_MAX entries during the Repetition Phase.

.. feat_req::
   :id: feat_req_someipsd_867
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Sending FindService entries shall be stopped after receiving the corresponding OfferService
   entries by jumping to the Main Phase in which no FindService entries are sent.

.. feat_req::
   :id: feat_req_someipsd_74
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If REPETITIONS_MAX is set to 0, the Repetition Phase shall be skipped and the Main Phase is
   entered for the Service Instance after the Initial Wait Phase.

.. feat_req::
   :id: feat_req_someipsd_75
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After the Repetition Phase the Main Phase is being entered for a Service Instance.

.. feat_req::
   :id: feat_req_someipsd_80
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After entering the Main Phase 1*CYCLIC_OFFER_DELAY is waited before sending the first message.

.. feat_req::
   :id: feat_req_someipsd_79
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   In the Main Phase OfferService messages shall be sent cyclically if a CYCLIC_OFFER_DELAY is
   configured, while the service instance is available.

.. feat_req::
   :id: feat_req_someipsd_81
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After a message for a specific service instance the SOME/IP-SD waits for 1*CYCLIC_OFFER_DELAY
   before sending the next message for this service instance.

.. feat_req::
   :id: feat_req_someipsd_866
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For FindService entries no cyclic messages are allowed in Main Phase.

.. feat_req::
   :id: feat_req_someipsd_631
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Requests/Subscriptions entries shall not be triggered cyclically but shall be triggered by
   OfferService entries, which are sent cyclically.

.. feat_req::
   :id: feat_req_someipsd_77
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Example:

   Initial Wait Phase:

   *  Wait for random_delay in Range(INITIAL_DELAY_MIN, _MAX)
   *  Send message (FindService and OfferService entries)

   Repetition Phase (REPETITIONS_BASE_DELAY=100ms, REPETITIONS_MAX=2):

   *  Wait 2^0*100ms
   *  Send message (FindService and OfferService entries)
   *  Wait 2^1*100ms
   *  Send message (FindService and OfferService entries)
   *  Wait 2^2*100ms

   Main Phase (as long message is active and CYCLIC_OFFER_DELAY is defined):

   *  Send message (OfferService entries)
   *  Wait CYCLIC_OFFER_DELAY

Response Behavior
=================

.. heading:: Response Behavior
   :id: feat_req_someipsd_61
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_83
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD shall delay responses to entries that were transported in a multicast/broadcast
   SOME/IP-SD message using the configuration item REQUEST_RESPONSE_DELAY in order to prevent
   multicast-response bursts.

   This applies to responses to FindService entries, i.e. OfferService entries.

.. feat_req::
   :id: feat_req_someipsd_766
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The REQUEST_RESPONSE_DELAY shall also apply to unicast messages triggered by multicast messages
   in order to prevent multicast-response bursts.

   This applies to SubscribeEventgroup in response to OfferService, for example.

.. feat_req::
   :id: feat_req_someipsd_624
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The REQUEST_RESPONSE_DELAY shall not apply if unicast messages are responded with unicast messages.

.. feat_req::
   :id: feat_req_someipsd_84
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   REQUEST_RESPONSE_DELAY shall be specified by a minimum and a maximum.

.. feat_req::
   :id: feat_req_someipsd_85
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The actual delay shall be randomly chosen between minimum and maximum of REQUEST_RESPONSE_DELAY.

.. feat_req::
   :id: feat_req_someipsd_824
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For basic implementations all FindService entries (no matter of the state of the Unicast Flag)
   shall be responded with OfferService entries transported using unicast.

.. feat_req::
   :id: feat_req_someipsd_826
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For optimization purpose the following behaviors may optionally be supported:

.. feat_req::
   :id: feat_req_someipsd_89
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   *  FindService messages received with the Unicast Flag set to 1 in main phase, shall be responded
      to with a unicast response if the last offer was sent less than 1/2 CYCLIC_OFFER_DELAY ago.

.. feat_req::
   :id: feat_req_someipsd_90
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   *  FindService messages received with the Unicast Flag set to 1 in main phase, shall be responded
      to with a multicast response if the last offer was sent 1/2 CYCLIC_OFFER_DELAY or longer ago.

.. feat_req::
   :id: feat_req_someipsd_91
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   *  FindService messages received with Unicast Flag set to 0 (multicast), shall be responded to
      with a multicast response.

   Note: This was only needed in earlier migration scenarios and will go away in the future).

Shutdown Behavior
=================

.. heading:: Shutdown Behavior
   :id: feat_req_someipsd_819
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_820
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When a server service instance of an ECU is being stopped, a StopOfferService entry shall be sent out.

.. feat_req::
   :id: feat_req_someipsd_830
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When a server sends out a StopOfferService entry all subscriptions for this service instance
   shall be deleted on the server side.

.. feat_req::
   :id: feat_req_someipsd_1297
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When a server receives a StopSubscribeEventgroup entry by a client, this client shall be deleted
   from the subscription list of the eventgroup and the server shall free its resources accordingly.

.. feat_req::
   :id: feat_req_someipsd_831
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When a client receives a StopOfferService entry, all subscriptions for this service instance
   shall be deleted on the client side and the client shall free its resources accordingly
   (i.e. close sockets and reset to default/wildcard).

.. feat_req::
   :id: feat_req_someipsd_834
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When a client receives a StopOfferService entry, the client shall not send out FindService
   entries but wait for OfferService entry or change of status (application, network management,
   Ethernet link, or similar).

.. feat_req::
   :id: feat_req_someipsd_822
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When a client service instance of an ECU is being stopped (i.e. the service instance is released),
   the SD shall send out StopSubscribeEventgroup entries for all subscribed Eventgroups.

.. feat_req::
   :id: feat_req_someipsd_821
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When the whole ECU is being shut down, StopOfferService entries shall be sent out for all service
   entries and StopSubscribeEventgroup entries for Eventgroups.

State Machines
============== 

.. heading:: State Machines
   :id: feat_req_someipsd_627
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_628
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   In this section the state machines of the client and server are shown.

.. feat_req::
   :id: feat_req_someipsd_629
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP Services State Machine Server

   .. drawsvg_directive:: images/drawsvg/feat_req_someipsd_629.py


.. feat_req::
   :id: feat_req_someipsd_630
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP Services State Machine Client

   .. drawsvg_directive:: images/drawsvg/feat_req_someipsd_630.py


Error Handling
==============

.. heading:: Error Handling
   :id: feat_req_someipsd_1162
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_1220
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Error checking of SOME/IP-SD messages shall first check the SOME/IP header as outlined earlier
   :need:`feat_req_someip_717`. SOME/IP-SD messages are treated as events in this regard.

.. feat_req::
   :id: feat_req_someipsd_1164
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_1163` shows a simplified illustration of the error handling of
   received SOME/IP-SD messages.

   The following steps shall be taken:

   *  Check that at least enough bytes for an empty SOME/IP-SD message are available
   *  Check that enough bytes for the entries and options array are available
   *  For each entry that can be parsed:
   *  Check if the Service ID of this entry is known
   *  Check if the Instance ID of this entry is known for this service
   *  Check if the Major Version of this entry is known for this service
   *  Check if the Eventgroup ID of the entry is known for this service (only applicable for eventgroup entries)
   *  Check if the referenced options exist in the options array and if these options are syntactically ok
   *  Check if all endpoint options contain a valid IP address (see :need:`feat_req_someipsd_1233`)
   *  Check if the TCP connection is already present (only applicable, if TCP is configured for
      Eventgroup and SubscribeEventgroup entry was received)
   *  Check if enough resources are left (e.g. Socket Connections)

   If any of these checks fails, the following shall be done:

   *  Respond with a SubscribeEventgroupNack, if the original entry was a SubscribeEventgroup entry
      :need:`feat_req_someipsd_1137`.
   *  Ignore, if the original entry was not a SubscribeEventgroup entry

.. feat_req::
   :id: feat_req_someipsd_1233
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   A valid IP address in this context has the following characteristics:

   *  Its value is in a configured range or the local subnet to which SOME/IP sends messages
   *  Is not the receiver's own IP address
   *  Is no multicast address
   *  Is not 127.0.0.1

.. feat_req::
   :id: feat_req_someipsd_1163
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: Error handling of received SOME/IP-SD message

   .. drawsvg_directive:: images/drawsvg/feat_req_someipsd_1163.py


.. feat_req::
   :id: feat_req_someipsd_102
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Check the referenced Options of each received entry:

   *  The referenced options exist.
   *  The entry references all required options (e.g. a provided eventgroup that uses unicast
      requires a unicast endpoint option in a received Subscribe Eventgroup entry).
   *  The entry only references supported options (e.g. a required eventgroup that does not support
      multicast data reception does not support multicast endpoint options in a Subscribe Eventgroup ACK entry).
   *  There are no conflicts between the options referenced by an entry (i.e. two options of same
      type with contradicting content).
   *  The Type of the referenced Option is known or the discardable flag is set to 1.
   *  The Type of the referenced Option is allowed for the entry or discardable flag is set to 1.
   *  The Length of the referenced Option is consistent to the Type of the Option.
   *  An Endpoint Option has a valid L4-Protocol and port number field.
   *  The Option is valid (e.g. a multicast endpoint option shall use a multicast IP address).

.. feat_req::
   :id: feat_req_someipsd_105
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Check if a security association is already established.

.. feat_req::
   :id: feat_req_someipsd_106
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the checks in Figure :need:`feat_req_someipsd_1163` fail for a received Find entry, the entry
   shall be ignored, except when Endpoint or Multicast Options are referenced, in which case only
   the Options shall be ignored according to :need:`feat_req_someipsd_878`.

Announcing non-SOME/IP protocols with SOME/IP-SD
************************************************

.. heading:: Announcing non-SOME/IP protocols with SOME/IP-SD
   :id: feat_req_someipsd_498
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_499
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Besides SOME/IP other communication protocols are used within the vehicle; e.g. for Network
   Management, Diagnosis, or Flash Updates. Such communication protocols might need to communicate a service instance or have eventgroups as well.

.. feat_req::
   :id: feat_req_someipsd_500
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For Non-SOME/IP protocols a special Service ID shall be used and further information shall be
   added using the configuration option:

   *  Service ID shall be set to 0xFFFE (reserved)
   *  Instance ID shall be used as described for SOME/IP services and eventgroups.
   *  The Configuration Option shall be added and shall contain at least an entry with key "otherserv"
      and a configurable non-empty value.

.. feat_req::
   :id: feat_req_someipsd_1227
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If multiple Non-SOME/IP services are announced, each shall have its own OfferService Entry, so
   individual TTLs are possible.

.. feat_req::
   :id: feat_req_someipsd_1228
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Only one single "otherserv" configuration option per OfferService Entry is permitted.

.. feat_req::
   :id: feat_req_someipsd_502
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SOME/IP services shall not use the otherserv-string in the Configuration Option.

.. feat_req::
   :id: feat_req_someipsd_503
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   For FindService/OfferService/RequestService entries the otherserv-string shall be used when
   announcing non-SOME/IP service instances.

.. feat_req::
   :id: feat_req_someipsd_501
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Example for valid otherserv-string: "otherserv=internaldiag".

   *  Example for an invalid otherserv-string: "otherserv".
   *  Example for an invalid otherserv-string: "otherserv=".

.. feat_req::
   :id: feat_req_someipsd_575
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: SOME/IP-SD example PDU for Non-SOME/IP-SD

   .. bitfield_directive:: images/bit_field/feat_req_someipsd_575.json


Publish/Subscribe with SOME/IP and SOME/IP-SD
*********************************************

.. heading:: Publish/Subscribe with SOME/IP and SOME/IP-SD
   :id: feat_req_someipsd_137
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_419
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   In contrast to the SOME/IP request/response mechanism there are cases in which a client requires
   a set of parameters from a server, but does not want to request that information each time it is
   required. These are called notifications and concern events and fields.

.. feat_req::
   :id: feat_req_someipsd_422
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   All clients needing events and/or notification events shall register using the SOME/IP-SD at
   run-time with a server.

.. feat_req::
   :id: feat_req_someipsd_425
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: Notification interaction (extremely simplified)

   .. plantuml:: images/plantuml/feat_req_someipsd_425.puml


.. feat_req::
   :id: feat_req_someipsd_428
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   With the SOME/IP-SD entry OfferService the server offers to push notifications to clients; thus,
   it shall be used as trigger for Subscriptions.

.. feat_req::
   :id: feat_req_someipsd_429
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When a server of a notification service starts up (e.g. after reset), it shall send a SOME/IP-SD
   OfferService into the network to discover all instances interested in the events and fields offered.

.. feat_req::
   :id: feat_req_someipsd_430
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Each client in SD based notification implements the specific service-interfaces for the notification
   they wish to receive and signal their wish of receiving such notifications using the SOME/IP-SD
   SubscribeEventgroup entries.

.. feat_req::
   :id: feat_req_someipsd_431
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Each client shall respond to a SOME/IP-SD OfferService entry from the server with a SOME/IP-SD
   SubscribeEventgroup entry as long as the client is still interested in receiving the
   notifications/events of this eventgroup.

   If the client is able to reliably detect the reboot of the server using the SOME/IP-SD messages
   reboot flag, the client shall only respond to OfferService messages after the server reboots, if
   configured to do so (TTL set to maximum value). The client shall make sure that this works
   reliable even when the SOME/IP-SD messages of the server are lost.

.. feat_req::
   :id: feat_req_someipsd_1191
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The client shall explicitly request Initial Events by setting the Initial Data Requested Flag,
   if it has no active subscription to the Eventgroup.

.. feat_req::
   :id: feat_req_someipsd_1192
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the client sends out additional SubscribeEventgroup entries and the TTL of the previous
   Subscribe has not expired yet, the client shall not request Initial Events.

.. feat_req::
   :id: feat_req_someipsd_1193
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Reasons for the client to explicitly request Initial Events include but are not limited to:

   *  The client is currently not subscribed to the Eventgroup.
   *  The client has seen a link-down/link-up after the last SubscribeEventgroup entry.
   *  The client has not received a SubscribeEventgroupAck after the last regular SubscribeEventgroup
      (see :need:`feat_req_someipsd_844`).
   *  The client has detected a Reboot of the Server of this Services (see :need:`feat_req_someipsd_871`).

.. feat_req::
   :id: feat_req_someipsd_1168
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the client subscribes to two or more eventgroups including one or more identical events or
   fields, the server shall not send duplicated events or notification events for the field.
   This does mean regular events and not initial events.

   See :need:`feat_req_someipsd_1166` and :need:`feat_req_someipsd_1167`.

.. feat_req::
   :id: feat_req_someipsd_632
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Publish / Subscribe with link loss at client (figure ignores timings)

   .. plantuml:: images/plantuml/feat_req_someipsd_632.puml


.. feat_req::
   :id: feat_req_someipsd_432
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The server sending OfferService entries as implicit Publishes has to keep state of SubscribeEventgroup
   messages for this eventgroup instance in order to know if notifications/events have to be sent.

.. feat_req::
   :id: feat_req_someipsd_433
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A client shall deregister from a server by sending a SOME/IP-SD SubscribeEventgroup message with
   TTL=0 (StopSubscribeEventgroup).

.. feat_req::
   :id: feat_req_someipsd_634
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Figure: Publish/Subscribe Registration/Deregistration behavior (figure ignoring timings)

   .. plantuml:: images/plantuml/feat_req_someipsd_634.puml


.. feat_req::
   :id: feat_req_someipsd_1239
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure: Publish / Subscribe Registration / Deregistration behavior (figure ignores timings)

   .. plantuml:: images/plantuml/feat_req_someipsd_1239.puml

.. feat_req::
   :id: feat_req_someipsd_435
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD on the server shall delete the subscription, if a relevant SOME/IP error is
   received after sending an event or notification event.

   The error includes but is not limited to not being able to reach the communication partner and
   errors of the TCP connection.

.. feat_req::
   :id: feat_req_someipsd_437
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the server loses its link on the relevant Ethernet interface, it shall delete all the registered
   notifications and close the TCP connection for those notifications as well.

.. feat_req::
   :id: feat_req_someipsd_436
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the Ethernet link status of the server becomes up again, it shall trigger a SOME/IP-SD
   OfferService message.

.. feat_req::
   :id: feat_req_someipsd_633
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Publish / Subscribe with link loss at server (figure ignores timings)

   .. plantuml:: images/plantuml/feat_req_someipsd_633.puml


.. feat_req::
   :id: feat_req_someipsd_439
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After having not received a notification/event of an eventgroup subscribed to for a certain time
   the ECU shall send a new SubscribeEventgroup entry. The timeout shall be configurable for each eventgroup.

.. feat_req::
   :id: feat_req_someipsd_832
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   This timeout feature might be based on the cycle times of cyclic SD-messages, e.g. OfferService
   entries or messages protected by alive counters (functional safety).

.. feat_req::
   :id: feat_req_someipsd_440
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A link-up event on the clients Ethernet link shall start the Initial Wait Phase
   (consider UDP-NM and others). SOME/IP-SD SubscribeEventgroup entry shall be sent out as described above.

.. feat_req::
   :id: feat_req_someipsd_1182
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The client shall have its UDP port open and ready to receive messages before sending a
   SubscribeEventgroup entry, if unreliable events and notification events exist in the interface
   specification (e.g. FIBEX or ARXML).

.. feat_req::
   :id: feat_req_someipsd_767
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The client shall open a TCP connection to the server and should be ready to receive message on
   that connection before sending the SubscribeEventgroup entry, if reliable events and notification
   events exist in the interface specification (e.g. FIBEX or ARXML).

.. feat_req::
   :id: feat_req_someipsd_441
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   After a client has sent a SubscribeEventgroup entry the server shall send a SubscribeEventgroupAck
   entry considering the specified delay behavior.

   Note: The delay behavior is only relevant, if the SubscribeEventgroup was sent via Multicast,
   which should not be the case anymore.

.. feat_req::
   :id: feat_req_someipsd_844
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The client shall wait for the SubscribeEventgroupAck entry acknowledging a SubscribeEventgroup
   entry. If this SubscribeEventgroupAck entry does not arrive before the next SubscribeEventgroup
   entry is sent, the client shall do the following:

   *  if the "Explicit Initial Data Control Flag" of the Server is set to 0, send a
      StopSubscribeEventgroup entry and a SubscribeEventgroup entry in the same SOME/IP-SD message
      the SubscribeEventgroup entry would have been sent with.
   *  if the "Explicit Initial Data Control Flag" of the Server is set to 1, set the Initial Data
      Requested Flag of the next SubscribeEventgroup Entry to 1.

   Note: This behavior exists to cope with short durations of communication loss, so new Initial
   Events are triggered to lower the effects of the loss of messages.

.. feat_req::
   :id: feat_req_someipsd_1178
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Stop Subscribe and Subscribe entry sent because of :need:`feat_req_someipsd_844` shall be
   directly behind each other in the same SD message (no other entry between them).

.. feat_req::
   :id: feat_req_someipsd_1171
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The :need:`feat_req_someipsd_844` shall not lead to closing and reopening TCP connections.

.. feat_req::
   :id: feat_req_someipsd_1169
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The :need:`feat_req_someipsd_844` shall not be applied to OfferService entries that are a
   reaction to FindService entries. That means that the SubscribeEventgroupAck entry of a
   SubscribeEventgroup entry that was triggered by unicast OfferService entry is not monitored as
   well as upon an unicast OfferService entry the StopSubscribeEventgroup entry/SubscribeEventgroup
   entry is not sent.

.. feat_req::
   :id: feat_req_someipsd_1176
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The :need:`feat_req_someipsd_844` shall not be applied to SubscribeEventgroups that were not
   triggered directly by a Multicast OfferService.

.. feat_req::
   :id: feat_req_someipsd_691
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If the initial value is of concern – i.e. for fields – and the client has the Explicit Initial
   Data Control Flag set to 0, the server shall send the first notification events (i.e. initial events)
   immediately after sending the SubscribeEventgroupAck. The client shall repeat the SubscribeEventgroup
   entry, if it did not receive the notification events within a configurable time.

.. feat_req::
   :id: feat_req_someipsd_833
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   This means:

   *  It is not allowed to send initial values of events upon subscriptions (pure event and not field).
   *  The event messages of field notifiers shall be sent on subscriptions (field and not pure event).
   *  If a subscription was already valid and is updated by a SubscribeEventgroup entry, no initial events shall be sent.
   *  Receiving StopSubscribeEventgroup / SubscribeEventgroup combinations trigger initial events of field notifiers.

.. feat_req::
   :id: feat_req_someipsd_107
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The initial events should be sent after the SubscribeEventgroupAck.

.. feat_req::
   :id: feat_req_someipsd_1167
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If a client subscribes to different eventgroups of the same service instance that all include the same field in different SOME/IP-SD messages, the server shall send out the initial events for this field for every subscription separately.

.. feat_req::
   :id: feat_req_someipsd_1166
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If a client subscribes to different eventgroups of the same service instance that all include the
   same field in the same SOME/IP-SD message, the server may choose to not send out the initial event
   for this field more than once.

   Note: This means the server can optimize by sending the initial events only once, if supported by
   its architecture.

.. feat_req::
   :id: feat_req_someipsd_625
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Publish / Subscribe State Diagram (server behavior for unicast eventgroups)

   .. drawsvg_directive:: images/drawsvg/feat_req_someipsd_625.py


.. feat_req::
   :id: feat_req_someipsd_626
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Publish / Subscribe State Diagram (server behavior for multicast eventgroups)

   .. drawsvg_directive:: images/drawsvg/feat_req_someipsd_626.py


.. feat_req::
   :id: feat_req_someipsd_823
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Publish / Subscribe State Diagram (server behavior for adaptive unicast/multicast eventgroups)

   .. drawsvg_directive:: images/drawsvg/feat_req_someipsd_823.py


.. feat_req::
   :id: feat_req_someipsd_442
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Publish/Subscribe State Diagram (overall behavior)

   .. drawsvg_directive:: images/drawsvg/feat_req_someipsd_442.py


.. feat_req::
   :id: feat_req_someipsd_444
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   An implicit registration of a client to receive notifications from a server shall be supported.
   Meaning the mechanism is pre-configured.

.. feat_req::
   :id: feat_req_someipsd_445
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   To allow for cleanup of stale client registrations (to avoid that the list of listeners fills
   over time), a cleanup mechanism is required.

.. feat_req::
   :id: feat_req_someipsd_818
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following entries shall be transported by unicast only:

   *  SubscribeEventgroup
   *  StopSubscribeEventgroup
   *  SubscribeEventgroupAck
   *  SubscribeEventgroupNack

.. feat_req::
   :id: feat_req_someipsd_828
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   When sending a SubscribeEventgroup entry as reaction of receiving an OfferService entry, the
   timer controlling cyclic SubscribeEventgroups entries shall be reset.

.. feat_req::
   :id: feat_req_someipsd_829
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If no cyclic SubscribeEventgroups are configured, the timer for cyclic SubscribeEventgroups
   stays turned off.

Endpoint Handling for Services and Events
*****************************************

.. heading:: Endpoint Handling for Services and Events
   :id: feat_req_someipsd_776
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_777
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   This section describes how the Endpoints encoded in the Endpoint and Multicast Options shall be
   set and used.

.. feat_req::
   :id: feat_req_someipsd_778
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The SOME/IP-SD shall overwrite IP Addresses and Port Numbers with those transported in Endpoint
   and Multicast Options if the statically configured values are different from those in these options.

Service Endpoints
=================

.. heading:: Service Endpoints
   :id: feat_req_someipsd_784
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_780
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   OfferService entries shall reference up to 1 UDP Endpoint Option and up to 1 TCP Endpoint Option.
   Both shall be of the same version Internet Protocol (IPv4 or IPv6).

.. feat_req::
   :id: feat_req_someipsd_779
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The referenced Endpoint Options of the OfferService entries denote the IP Address and Port Numbers
   the service instance is reachable at the server.

.. feat_req::
   :id: feat_req_someipsd_781
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The referenced Endpoint Options of the OfferService entries also denote the IP Address and Port
   Numbers the service instance sends the events from.

.. feat_req::
   :id: feat_req_someipsd_797
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Events of this service instance shall not be sent from any other Endpoint than those given in the
   Endpoint Options of the OfferService entries.

.. feat_req::
   :id: feat_req_someipsd_782
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   If an ECU offers multiple service instances, SOME/IP messages of these service instances shall be
   differentiated by the information transported in the Endpoint Options referenced by the
   OfferService entries.

.. feat_req::
   :id: feat_req_someipsd_783
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Therefore transporting an Instance ID in the SOME/IP header is not required.

.. feat_req::
   :id: feat_req_someipsd_877
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A sender shall not reference Endpoint Options nor Multicast Options in a FindService Entry.

.. feat_req::
   :id: feat_req_someipsd_878
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A receiver shall ignore Endpoint Options and Multicast Options in a FindService Entry.

.. feat_req::
   :id: feat_req_someipsd_879
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Other Options (neither Endpoint nor Multicast Options), shall still be allowed to be used in a
   FindService Entry.

Eventgroup Endpoints
====================

.. heading:: Eventgroup Endpoints
   :id: feat_req_someipsd_785
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_786
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SubscribeEventgroup entries shall reference up to 1 UDP Endpoint Option and up to 1 TCP Endpoint
   Option for the Internet Protocol used (IPv4 or IPv6).

.. feat_req::
   :id: feat_req_someipsd_787
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Endpoint Options referenced in the SubscribeEventgroup entries are also used to send unicast
   UDP or TCP SOME/IP events for this Service Instance.

.. feat_req::
   :id: feat_req_someipsd_798
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   Thus the Endpoint Options referenced in the SubscribeEventgroup entries are the IP Address and
   the Port Numbers on the client side.

.. feat_req::
   :id: feat_req_someipsd_788
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   TCP events are transported using the TCP connection the client has opened to the server before
   sending the SubscribeEventgroup entry. See :need:`feat_req_someipsd_752`.

.. feat_req::
   :id: feat_req_someipsd_793
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The initial events shall be transported using unicast from Server to Client.

.. feat_req::
   :id: feat_req_someipsd_789
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   SubscribeEventgroupAck entries shall reference up to 1 Multicast Option for the Internet Protocol
   used (IPv4 or IPv6).

.. feat_req::
   :id: feat_req_someipsd_790
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Multicast Option shall be set to UDP as transport protocol.

.. feat_req::
   :id: feat_req_someipsd_791
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The client shall open the Endpoint specified in the Multicast Option referenced by the
   SubscribeEventgroupAck entry as fast as possible to not miss multicast events.

Example
=======

.. heading:: Example
   :id: feat_req_someipsd_794
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_796
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure :need:`feat_req_someipsd_795` shows an example with the different Endpoint and a Multicast Option:

   *  The server offers the Service Instance on server UDP-Endpoint SU and server TCP-Endpoint ST
   *  The client opens a TCP connection
   *  The client sends a SubscribeEventgroup entry with client UDP-Endpoint CU (unicast) and a
      client TCP-Endpoint CT.
   *  The server responds with a SubscribeEventgroupAck entry with Multicast MU

   Then the following operations happen:

   * The client calls a method on the server
   * Request is sent from CU to SU and response from SU to CU
   * For TCP this would be: Request dyn to ST and response from ST to CT
   * The server sends a Unicast UDP Event: SU to CU
   * The server sends a Unicast TCP Event: ST to CT
   * The server sends a Multicast UDP Event: SU to MU

   Keep in mind that Multicast Endpoints use a Multicast IP Address on the receiver side, i.e. the
   client, and TCP cannot be used for Multicast communication.


.. feat_req::
   :id: feat_req_someipsd_795
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Figure: Publish/Subscribe Example for Endpoint Options and the usage of ports.

   .. plantuml:: images/plantuml/feat_req_someipsd_795.puml


Security Considerations
=======================

.. heading:: Security Considerations
   :id: feat_req_someipsd_1134
   :h: 3

.. feat_req::
   :id: feat_req_someipsd_1135
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   A SOME/IP-SD implementation shall always check that the IP Addresses received in Endpoint options
   and SD Endpoint options are topological correct (reference IP Addresses in the IP subnet for
   which SOME/IP-SD is used) and shall ignore IP Addresses that are not topological correct as
   well as the entries referencing those options.

   Note: This means that only Clients and Servers in the same subset are accessible.

.. feat_req::
   :id: feat_req_someipsd_1136
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   An example for checking the IP Addresses (Endpoint-IP) for topological correctness is:
   SOME/IP-SD-IP-Address AND Netmask = Endpoint-IP AND Netmask.

.. feat_req::
   :id: feat_req_someipsd_1149
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   It shall be possible to turn off the checking of topological correctness via configuration.

Mandatory Feature Set and Basic Behavior
****************************************

.. heading:: Mandatory Feature Set and Basic Behavior
   :id: feat_req_someipsd_806
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_807
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   In this section the mandatory feature set of the SOME/IP-SD and the relevant configuration
   constraints are discussed. This allow for bare minimum implementations without optional or
   informational features that might not be required for current use cases.

.. feat_req::
   :id: feat_req_someipsd_815
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   The following information is defined as compliance check list(s). If a feature is not implemented,
   the implementation is considered not to comply with the SOME/IP-SDs basic feature set.

.. feat_req::
   :id: feat_req_someipsd_1195
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following information does not allow implementers to ignore requirements of this specification.

.. feat_req::
   :id: feat_req_someipsd_808
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following entry types shall be implemented:

   *  FindService
   *  OfferService
   *  StopOfferService
   *  SubscribeEventgroup
   *  StopSubscribeEventgroup
   *  SubscribeEventgroupAck
   *  SubscribeEventgroupNack

.. feat_req::
   :id: feat_req_someipsd_809
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following option types shall be implemented, when IPv4 is required:

   *  IPv4 Endpoint Option
   *  IPv4 Multicast Option
   *  Configuration Option
   *  IPv4 SD Endpoint Option (receiving at least)

.. feat_req::
   :id: feat_req_someipsd_810
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following option types shall be implemented, if IPv6 is required:

   *  IPv6 Endpoint Option
   *  IPv6 Multicast Option
   *  Configuration Option
   *  IPv6 SD Endpoint Option (receiving at least)

.. feat_req::
   :id: feat_req_someipsd_857
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following option types shall be implemented, if non-SOME/IP services or additional
   configuration parameters are required:

   *  Configuration Option

.. feat_req::
   :id: feat_req_someipsd_811
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following behaviors/reactions shall be implemented on the server side:

   *  The server shall offer services including the Initial Wait Phase, the Repetition Phase, and
      the Main Phase depending on the configuration.
   *  The server shall offer services using Multicast (Repetition Phase and Main Phase).
   *  The server does not need to respond to a FindService in the Repetition Phase.
   *  The server shall respond to a FindService in the Main Phase with an OfferService using Unicast
      (the optimization based on unicast flag as in :need:`feat_req_someipsd_826` is optional).
   *  The server shall send a StopOfferService when shutting down.
   *  The server shall receive a SubscribeEventgroup as well as a StopSubscribeEventgroup and react
      according to this specification.
   *  The server shall send a SubscribeEventgroupAck and SubscribeEventgroupNack using unicast.
   *  The server shall support controlling the sending (i.e. fan out) of SOME/IP event messages
      based on the subscriptions of SOME/IP-SD. This might include sending events based on Multicast.
   *  The server shall support the triggering of initial SOME/IP event messages.

.. feat_req::
   :id: feat_req_someipsd_812
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following behaviors/reactions shall be implemented on the Client side:

   *  The Client shall find services using a FindService entry and Multicast only in the repetition phase.
   *  The Client shall stop finding a service if the regular OfferService arrives.
   *  The Client shall react to the Servers OfferService with a unicast SD message that includes all
      SubscribeEventgroups of the services offered in the message of the Server that the client
      currently wants to subscribe to.
   *  The Client shall interpret and react to the SubscribeEventgroupAck and SubscribeEventgroupNack
      as specified in this document.

.. feat_req::
   :id: feat_req_someipsd_816
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The following behavior and configuration constraints shall be supported by the client:

   *  The client shall even handle eventgroups if only the TTL of the SD Timings is specified.
      This means that of all the timings for the Initial Wait Phase, the Repetition Phase,
      and the Main Phase only TTL is configured. This means the client shall only react on the
      OfferService by the server.
   *  The client shall respond to an OfferService with a SubscribeEventgroup even without
      configuration of the Request-Response-Delay, meaning it does not wait but respond instantaneously.

.. feat_req::
   :id: feat_req_someipsd_813
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Client and Server shall implement the Reboot Detection as specified in this document and
   react accordingly. This includes but is not limited to:

   *  Setting Session ID and Reboot Flag according to this specification.
   *  Keeping a Session ID counter only used for sending Multicast SD messages.
   *  Keeping Session ID counters for every Unicast relation for sending Unicast SD messages.
   *  Understanding Session ID and Reboot Flag according to this specification.
   *  Keeping a Multicast Session ID counter per ECU that exchanges Multicast SD messages with this ECU.
   *  Keeping a Unicast Session ID counter per ECU that exchanges Unicast SD messages with this ECU.
   *  Detecting reboot based on this specification and react accordingly.
   *  Correctly interpreting the IPv4 and IPv6 SD Endpoint Options in regard to Reboot Detection.

.. feat_req::
   :id: feat_req_someipsd_814
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Client and Server shall implement the "Endpoint Handling for Service and Events". This
   includes but is not limited to:

   *  Adding 1 Endpoint Option UDP to an OfferService if UDP is needed.
   *  Adding 1 Endpoint Option TCP to an OfferService if TCP is needed.
   *  Adding 1 Endpoint Option UDP to SubscribeEventgroup, if events over UDP are required.
   *  Adding 1 Endpoint Option TCP to SubscribeEventgroup, if events over TCP are required.
   *  Adding 1 Multicast Option UDP to SubscribeEventgroupAck, if multicast events are required.
   *  Understanding and acting according to the Endpoint and Multicast Options transported as described above.
   *  Overwriting preconfigured values (e.g. IP Addresses and Ports) with the information of these
      Endpoint and Multicast Options.
   *  Interpreting incoming IPv4 and IPv6 Endpoint Options as SD endpoints instead of the Address
      and Port number in the outer layers.

.. feat_req::
   :id: feat_req_someipsd_1194
   :reqtype: Requirement
   :security: NO
   :safety: QM
   :status: valid

   The Client and Server shall implement the explicit requesting of Initial Events.

.. feat_req::
   :id: feat_req_someipsd_946
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Allowed SOME/IP-SD Option types in relation to Entry types.

   .. list-table::
      :align: left
      :header-rows: 1
      :class: ssp-tinier

      *  -
         -  Endpoint Option
         -  Multicast Option
         -  Configuration Option
         -  Load Balancing Option
      *  -  **FindService**
         -  0
         -  0
         -  0-1
         -  0-1
      *  -  **OfferService**
         -  1-2
         -  0
         -  0-1
         -  0-1
      *  -  **StopOfferService**
         -  1-2
         -  0
         -  0-1
         -  0-1
      *  -  **SubscribeEventgroup**
         -  0-2
         -  0
         -  0-1
         -  0-1
      *  -  **StopSubscribeEventgroup**
         -  0-2
         -  0
         -  0-1
         -  0-1
      *  -  **SubscribeEventgroupAck**
         -  0
         -  0-1
         -  0-1
         -  0-1
      *  -  **SubscribeEventgroupNack**
         -  0
         -  0
         -  0-1
         -  0-1

.. feat_req::
   :id: feat_req_someipsd_1179
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Note: A SubscribeEventgroup without Endpoint Options is only allowed for an Eventgroup with
   Multicast Events only.

SOME/IP-SD Mechanisms and Errors
********************************

.. heading:: SOME/IP-SD Mechanisms and Errors
   :id: feat_req_someipsd_837
   :h: 2

.. feat_req::
   :id: feat_req_someipsd_838
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   In this section SOME/IP-SD in cases of errors (e.g. lost or corrupted packets) is discussed.
   This is also understood as rationale for the mechanisms used and the configuration possible.

.. feat_req::
   :id: feat_req_someipsd_842
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Soft State Protocol
   SOME/IP-SD was designed as soft state protocol, that means that entries come with a lifetime and
   need to be refreshed to stay valid (setting the TTL to the maximum value shall turn this off).

   Using cyclic OfferService entries and the TTL as aging mechanism SOME/IP-SD shall cope with many
   different cases of errors.

   Examples:

   *  If a client or server leaves without sending a Stop entry or this Stop entry got lost,
      the system will fix itself after the TTL expiration.
   *  If an OfferService entry does not arrive because the packet got lost, the system will tolerate
      this based on the value of the TTL.

   Example configuration parameter for fast healing: cyclic delays 1 s and TTL 3 s.

.. feat_req::
   :id: feat_req_someipsd_840
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Initial Wait Phase

   The Initial Wait Phase was introduced for two reasons: deskewing events of starting ECUs to avoid
   traffic bursts and allowing ECUs to collect multiple entries in SD messages.

.. feat_req::
   :id: feat_req_someipsd_839
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Repetition Phase

   The Repetition Phase was introduced to allow for fast synchronization of clients and servers.
   If the clients startup later, it will find the server very fast. And if the server starts up later,
   the client is found very fast. The Repetition Phase increases the time between two messages
   exponentially to avoid that overload situations keep the system from synchronization.

   An example configuration could be REPETITIONS_BASE_DELAY=30ms and REPETITIONS_MAX=3.

.. feat_req::
   :id: feat_req_someipsd_841
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Main Phase

   In the Main Phase the SD tries to stabilize the state and thus decreases the rate of packets by
   sending no FindServices anymore and only offers in the cyclic interval (e.g. every 1s).

.. feat_req::
   :id: feat_req_someipsd_843
   :reqtype: Information
   :security: NO
   :safety: QM
   :status: valid

   Request-Response-Delay

   SOME/IP-SD shall allow to be configured to delay the response to entries in multicast messages by
   the Request-Response-Delay (in FIBEX called Query-Response-Delay). This is useful in large systems
   with many ECUs. When sending a SD message with many entries in it, a lot of responses from
   different ECUs arrive at the same time and put a large stress on the ECU receiving all these responses.
