# EUSAiR Initial Assessment: HJS Protocol Implementation 🇪🇺
### *Technical Alignment for EU AI Act Compliance (Art. 12, 13, 14)*

This repository serves as the official technical gateway for the **EUSAiR Initial Assessment (March 11, 2026)**. It demonstrates the **HJS Protocol** as a neutral infrastructure for verifiable AI accountability.

---

## 📍 Core Regulatory Mapping
We have bridged the gap between legal requirements and technical execution. The following matrix defines our **direct alignment** with the EU AI Act:

| EU AI Act Article | Regulatory Requirement | HJS Technical Solution (The Map) | Artifact |
| :--- | :--- | :--- | :--- |
| **Art. 12** | **Record-keeping** | Automated, immutable logging via **RFC 9562 (UUIDv7)** | [Demo](./compliance_demo.py) |
| **Art. 13** | **Transparency** | Human-interpretable policy binding in **Scenario Sandbox** | [Scenarios](./scenarios/) |
| **Art. 14** | **Human Oversight** | Cryptographic non-repudiation using **Ed25519 signatures** | [Proof](./IMMUTABILITY_PROOF.md) |

---

## ⚓ The HJS Anchoring Philosophy
Unlike traditional "trust-based" protocols, HJS provides a **Three-Dimensional Anchor** to ensure AI accountability:

1. **Mathematical Anchor (Integrity)**: 
   Leveraging **Ed25519** elliptic curve signatures. We replace "human promises" with mathematical certainty. If a single bit of a judgment is altered, the math fails, ensuring absolute data integrity.

2. **Physical Anchor (Temporal Order)**: 
   Utilizing **RFC 9562 (UUIDv7)** to hardcode millisecond-precision Unix timestamps. By anchoring every AI decision in the unidirectional flow of physical time, we make audit-trail manipulation (backdating) physically impossible.

3. **Sovereign Anchor (Local Governance)**: 
   HJS supports **Decentralized Sidecar deployment**. This allows the EUSAiR or any sovereign entity to host their own "Logic Gateways," ensuring that AI behavior is governed by local laws and regional digital sovereignty.

   HJS is designed as a non-intrusive compliance layer. It does not compete with AI models' intelligence but provides the physical and mathematical evidence required for their safe and legal operation in regulated environments."
---

## 🛠️ Compliance Evidence & Artifacts
These resources provide the "Technical Documentation" required for high-risk AI system assessment:

1. **📄 [Technical Mapping Guide](./EU_AI_ACT_MAPPING.md)**: A clause-by-clause alignment with European standards.
2. **💻 [Traceability Demo](./compliance_demo.py)**: Live execution of a verifiable audit trail.
3. **📂 [Scenario Sandbox](./scenarios/)**: Practical "Approved vs. Denied" logic for regulatory sandboxing.
4. **📕 [Operational Whitepaper (PDF)](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/HJS_Compliance_Whitepaper_Initial_Assessment.md.pdf)**: Comprehensive technical specifications for the EUSAiR pilot.

---

## 🏛️ Institutional Backing & Stability
The **HJS Foundation LTD (Singapore)** provides the non-profit legal anchor to ensure the protocol remains a **neutral public good**.

- **Neutrality**: Organized as a CLG (Company Limited by Guarantee) with no profit distribution.
- **Independence**: Mandatory 1/3 independent director ratio (Constitution Art. 35A).
- **Sustainability**: Core IP and protocol assets are permanently locked (Constitution Art. 67A).

> ⚖️ **[View Signed Foundation Constitution (PDF)](https://github.com/hjs-spec/eusair-hjs-initial-assessment/blob/main/docs/Constitution_Human%20Judgment%20Systems%20Foundation%20Ltd_signed.pdf)**

---

## 🚀 Quick Start for Auditors
To verify the protocol's compliance logic locally:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the compliance evidence generator
python compliance_demo.py

```

---

*Prepared for the EUSAiR Initial Assessment Phase.* **Primary Contact:** [signal@humanjudgment.org](mailto:signal@humanjudgment.org)

**Legal Entity:** HJS Foundation LTD (Singapore)
