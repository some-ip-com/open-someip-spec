# Open SOME/IP Specification

This is part of SOME/IP. See https://some-ip.com

## What is the Open SOME/IP Specification for?

The Open SOME/IP Specification enables Open-Source SOME/IP implementations as well as defining a central specification anchor for different SOME/IP standards.

## What are the benefits of another SOME/IP specification?

So far different SOME/IP specifications were created but all of them come one or multiple shortcomings:
* Incomplete specifications that do not defined all commonly-used features.
* Outdated specification.
* License that is incompatible with Open-Source implementations.
* Standard documents that lack essential feature like clear linking and stable access to them.
* Proprietary extensions that are not supported by all implementations or standards.

The Open SOME/IP Specification tries to solve these shortcomings by providing an open standard with an acceptable license, while at the same time creating the option for other standards to incorporate the provided requirements under conditions stated in the license.

## What are the downsides of the Open SOME/IP Specification?

As the Open SOME/IP Specification is covered by a permissive license, we can only accept contributions that are compatible with our license. If an individual or a company created a SOME/IP extension or feature in another standardization (e.g., AUTOSAR), we require a submission of this contribution by the original contributor.

## What does the Open SOME/IP Specification cover?

As of 2025, the Open SOME/IP Specification covers all core SOME/IP features like:
* SOME/IP RPC and Messaging
* SOME/IP-SD and Publish/Subscribe
* SOME/IP-TP

The Open SOME/IP Specification in addition covers newer contributions and clarifications.

## What is on the Open SOME/IP Specification roadmap?

We are currently working on the following upcoming specification topics among others:
* Interworking of SOME/IP and Security Protocols
* A lightweight SOME/IP Key Exchange and Message Protection solution

## What is not covered by the Open SOME/IP Specification?

The Open SOME/IP Specification misses the following:
* SOME/IP TLV serialization (proprietary, optional, very limited usage in industry)
* Client-based Multicast Endpoints (proprietary, optional, very limited usage in industry)
* The Open SOME/IP Specification does not define E2E profiles and their formats as they are not SOME/IP specific.

## How to build specification (Linux, macOS, etc.)

```
git clone https://github.com/some-ip-com/open-someip-spec
cd open-someip-spec
./tools/setup.sh
source .venv/bin/activate
make html
```
Open `src/_build/html/index.html` in your browser.

## Licensing

The Open SOME/IP Specification is licensed under the SOME/IP Community Specification License,
which is the Community Specification License (SPDX: Community-Spec-1.0) and additional terms.
The license can be found in [SOMEIP_Community_Specification_License.md](SOMEIP_Community_Specification_License.md)

(c) Technica Engineering GmbH, 2025

