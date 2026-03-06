# Cryptographic Proof of Immutability

To meet the high standards of **Article 12 (Record-keeping)**, HJS provides a mathematical guarantee that evidence cannot be tampered with post-facto.

### 🛡️ The "Digital Notary" Chain
1. **Timestamp Integrity**: **UUIDv7** embeds a 48-bit Unix timestamp. Any attempt to backdate a judgment would result in a UUID collision or sequence break detectable by auditors.
2. **Signature Binding**: Every receipt is signed using **Ed25519**. Even a 1-bit change in the audit log will invalidate the signature, providing immediate alert of tampering.
3. **Non-Repudiation**: The private key remains within the secure enclave of the HJS provider, ensuring that the "Issuer" cannot deny their own judgment.
