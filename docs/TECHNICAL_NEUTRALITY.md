# Statement of Technical Neutrality & Zero-Data Access

The HJS Sidecar is architected as a **stateless verification anchor**. It ensures regulatory compliance without accessing sensitive business payloads.

### 1. Data Minimization (Article 10 Compliance)
- **Zero-Payload Policy**: HJS only processes the `JudgmentContext` (Metadata). It does not ingest, store, or transmit the actual content of AI tool calls or database records.
- **Privacy by Design**: We use cryptographic hashes (SHA-256) to verify policies. The Sidecar never sees the plain text of a private policy unless explicitly authorized.

### 2. Infrastructure Agnostic
- HJS is compatible with any AI Proxy (AIP), Cloud provider, or On-premise deployment. It serves as a modular "Judicial Branch" independent of the "Executive" execution layer.
