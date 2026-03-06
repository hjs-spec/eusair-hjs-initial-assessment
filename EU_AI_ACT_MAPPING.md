# HJS Technical Alignment with EU AI Act (Initial Assessment)

This document outlines how the **HJS Sidecar Architecture** serves as the technical enforcement layer for compliance with the **EU AI Act** (High-Risk AI System Requirements).

---

## 1. Article 12: Record-keeping (Logging & Traceability)

* **Requirement**: Mandatory automatic recording of events (logging) to ensure traceability of the AI system's functioning throughout its lifecycle.
* **HJS Implementation**: **Physical Anchoring via UUIDv7 (RFC 9562)**
* **Engineering Fact**: By utilizing a 48-bit Unix-epoch timestamp as the primary key prefix, HJS ensures that every "Judgment Event" is natively anchored to physical time.


* **Compliance Value**: This creates an **irreversible chronological audit trail**. Regulators can reconstruct the exact state of AI decision-making at any specific millisecond in history without the risk of sequence manipulation or backdating.



---

## 2. Article 13: Transparency and Provision of Information

* **Requirement**: AI systems must be designed to ensure that their operation is sufficiently transparent to enable users to interpret the system’s output and use it appropriately.
* **HJS Implementation**: **Semantic Transparency via Standardized Metadata**
* **Engineering Fact**: Every HJS receipt encapsulates the decision logic in a **Machine-Readable (JSON-LD)** and **Human-Verifiable** format.


* **Compliance Value**: By binding each event to a **Policy Hash**, HJS eliminates the "Black Box" problem. Auditors can verify exactly which safety parameters and decision-making weights were active during a specific transaction, ensuring the logic behind the output is fully transparent and explainable.



---

## 3. Article 14: Human Oversight

* **Requirement**: High-risk AI systems must be designed such that they can be effectively overseen by natural persons to prevent or minimize risks to health, safety, or fundamental rights.
* **HJS Implementation**: **Mathematical Non-repudiation via Ed25519**
* **Engineering Fact**: HJS utilizes **Ed25519 (RFC 8032)** asymmetric cryptography to sign every judgment event at the moment of creation.


* **Compliance Value**: This provides a **Mathematical Fact of Responsibility**. Once a judgment is signed by the HJS Sidecar, the provider cannot deny or alter it (non-repudiation). This provides human overseers with **legally admissible evidence** for accountability and immediate intervention, fulfilling the "Human-in-the-loop" principle.



---

## 4. Article 15: Accuracy, Robustness, and Cybersecurity

* **Requirement**: AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity.
* **HJS Implementation**: **Decentralized Sidecar Security Model**
* **Engineering Fact**: The HJS Sidecar operates in a **Sovereign Environment** (On-premise or Private Cloud), isolating the compliance logic from the AI model's internal vulnerabilities.


* **Compliance Value**: This ensures that even if the AI model provider is compromised, the **Judgment Integrity** and **Audit Logs** remain protected within the user's jurisdictional boundary, maintaining systemic robustness against external cyber threats.



---

### 🚀 Auditor Quick Reference

* **Protocol Version**: HJS-v1.0 (compliant with `draft-wang-hjs-judgment-event`)
* **Verification Tool**: `python compliance_demo.py`
* **Governance**: Managed by HJS Foundation LTD (Singapore)
