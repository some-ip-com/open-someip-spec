# Governance - Open SOME/IP Specification

## 1. Working Group and Roles
This Working Group (“WG”) operates in this repository under the SOME/IP Community Specification License 1.0 (SOME/IP CSL). Contributors accept SOME/IP CSL 1.0 by making a Contribution or by entering into the Community Specification CLA, as defined in the License. Editors curate Draft Specifications and propose promotions to Approved Specification. Chairs coordinate process and ensure antitrust compliance.

## 2. Decision‑Making
The WG seeks rough consensus recorded on the issue or pull request. Editors propose dispositions; absent consensus, Chairs adjudicate with a short written rationale and a cooling‑off period prior to merge.

## 3. Contribution Process
All proposed changes are submitted as pull requests to this repository. By contributing, the Contributor grants the copyright license in SOME/IP CSL §1 and accepts the patent commitments in §2 of the License, subject to the Exclusion Notice mechanism in §3. Each contribution must include a clear change description, explicit normative language where applicable, and a changelog entry. Every pull request proposing normative change shall include a “Compatibility Statement” explaining how the change is conformant with the Specification pursuant to §17 below, if not, why it should be treated as exceptional under §18. Where doubt remains, Contributors on the side of classifying as breaking.

## 4. Implementer Acceptance (Licensee Acceptance)
Implementers obtain the benefits of SOME/IP CSL patent grants only upon accepting the License. Acceptance occurs by: including SOME/IP CSL with the source distribution; or including SOME/IP CSL in accompanying materials for non‑source distributions; or, preferably, by adding an entry to `Notices.md` via pull request identifying implementer name, authorized individual, system identifier, and specification version.

## 5. Patent Exclusion Windows
Contributors may exclude patent claims from their commitments by filing an Exclusion Notice in `Notices.md` within the time limits set by SOME/IP CSL: within forty‑five (45) days of the relevant Contribution to a Draft; and, in any case, prior to adoption of a Draft as an Approved Specification where §3.2 applies. Exclusion Notices must identify the patent/application and the specific part of the Draft, consistent with the License’s definitions.

## 6. Release Flow and Approvals
Every merged change lands on the main branch. For each release: release branches are created. A release candidate (“RC”) may be proposed after stability on a release branch. Promotion to “Approved Specification” requires: compliance with the Retro‑Compatibility Policy below; resolution of any open Exclusion Notices or confirmation that applicable windows have run; completion of editorial review of conformance language; and publication of a diff and consolidated changelog.

## 7. Versioning
The project uses a Year-Month.Patch schema for documents: YY-MMp. For example 25-12 with patches 25-12a, 25-12b, etc.
Patch releases may only fix bugs in the specification.

All releases must be backward‑compatible as defined in the Retro‑Compatibility Policy below.

## 8. Code Components and Code License
Schemas, IDLs, message templates and similar artifacts embedded in the Specification are “Code Components”. Code in this repository is licensed under **BSD‑3‑Clause** in `LICENSE-CODE`. Where SOME/IP CSL would otherwise default to MIT in the absence of a code license, this project expressly selects BSD‑3‑Clause to ease reuse.

## 9. Retro‑Compatibility Gate
Only changes in a Contribution that satisfy the Retro‑Compatibility Policy may be proposed and included in a Draft Specification. This is a governance rule and does not modify SOME/IP CSL 1.0.

## 10. Attribution and Official Source
Derivative specifications must include, at minimum, the Specification’s name, version and **official source: https://some-ip.com**. Implementations are not required to carry attribution.

## 11. Antitrust, Non‑Circumvention, and No Other Rights
WG activity shall comply with the antitrust and non‑circumvention requirements of the License. No additional rights are granted beyond SOME/IP CSL, including trademarks.

## 12. Disclaimers
Distributions should include a distribution disclaimer materially consistent with the project’s front‑matter notice and the License’s disclaimers. Approved releases will carry an “AS IS / NO WARRANTY” statement and a limitation of liability.

## 13. Record‑Keeping and Publication
All changes proposed for adoption shall be documented in the pull request, merged publicly in this repository, and reflected in the release notes and changelog. Materials intended for adoption must be submitted here under SOME/IP CSL 1.0 without additional license terms or restrictions.

## 14. Amendments
Governance changes require Chair proposal, Editor review and a period for public comment. Amendments must remain consistent with SOME/IP CSL 1.0; governance cannot alter the legal terms of the License.

## 15. Trademark Notice
No trademark, trade name, certification mark or logo is licensed by this project. Any use of marks requires separate written permission.

# Retro‑Compatibility Policy for third party Derived Specifications — Open SOME/IP Specification

## 16. Purpose and Effect
This Policy governs creation and publication of third party Derived Specifications. Only backward‑compatible changes to the Specification may be made and must be Contributed to the Project. This is a governance rule; it does not modify the legal terms of the license applicable to the Specification "SOME/IP Community Specification License 1.0".

## 17. Definition of Backward Compatibility
A change is backward‑compatible when every valid Implementation conforming to Derived Specification remains conformant to the currently published Specification after the change without requiring modification, reconfiguration, or observable behavior change. Compatibility is assessed against message formats, field semantics, state machines, timing, error handling and discovery behavior.

## 18. Non‑Breaking Changes (Eligible)
The following changes are presumptively backward‑compatible when narrowly tailored and explicitly documented: clarifications that do not alter normative requirements; corrections of obvious editorial mistakes; additions of optional fields or parameters with well‑defined default behavior that preserves prior semantics; additions of new error/result codes not triggered by previously conformant behavior; deprecations that retain previous behavior unchanged; and tightening of unspecified behavior solely to forbid previously non‑conformant behavior.

## 19. Breaking Changes (Ineligible)
The following changes are presumptively breaking and therefore not allowed: removals or renaming of fields, parameters, services or message types in use; changes to default values that affect observable behavior; re‑ordering or re‑numbering that alters on‑wire encoding; changes from MAY/SHOULD to SHALL or from SHALL to SHOULD/MAY when they impact interoperability; alterations to timing, error handling or discovery that require peers to change; any change that forbids behavior previously conformant.

## 20. Exceptions and Major Tracks
If a materially valuable change is breaking, the Working Group may open a new major track (e.g., 2.x) to create a new SOME/IP version. Promotion to Approved Specification for a breaking change requires either (a) a parallel compatibility profile preserving 1.x interoperability, or (b) a Working Group decision to supersede the prior line after adequate notice and migration guidance. The WG will document rationale, migration path and expected deprecation timeline.

## 21. Record‑Keeping and Publication
All compatibility analyses must be recorded in the pull request and summarized in the release notes. Approved versions must include a changelog describing every normative change and its classification under this Policy. Approved status is a governance designation within this repository.

## 22. Attribution and Official Source
Derivative specifications must include attribution with, at minimum, the Specification’s name, the version, and the **official source: https://some-ip.com**. Attribution is not required for software implementations of the Specification.
