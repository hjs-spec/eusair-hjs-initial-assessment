# HJS Technical Alignment with EU AI Act (Initial Assessment)

This document outlines how the HJS Sidecar architecture assists in meeting the **Transparency** and **Logging** obligations of the **EU AI Act**.

### 1. Article 12: Record-keeping (Traceability)
- **Requirement**: Automatic recording of events throughout the system's lifetime.
- **HJS Solution**: Uses **UUIDv7 (RFC 9562)**. The 48-bit timestamp prefix ensures all judgment logs are natively sortable and indexed by time, providing a high-performance, immutable audit trail.

### 2. Article 13: Transparency
- **Requirement**: Systems must enable users to interpret outputs and use them appropriately.
- **HJS Solution**: Every receipt includes a **Policy Hash Binding**. By linking the judgment to a specific version of the safety policy, we eliminate "black-box" decision-making.

### 3. Article 14: Human Oversight
- **Requirement**: Systems must be overseeable by natural persons.
- **HJS Solution**: Implements **Ed25519 (EdDSA)** asymmetric signatures. This provides **Non-repudiation**, ensuring that every responsibility judgment can be legally traced back to the HJS provider.
