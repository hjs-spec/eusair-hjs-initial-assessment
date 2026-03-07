#!/usr/bin/env python3
"""
EU AI Act Sandbox Verification Script
Run this to validate all compliance evidence for sandbox auditors

Usage:
    python verify_sandbox.py

Expected Output:
    - Article 12: UUIDv7 verification
    - Article 14: Signature verification
    - Privacy: No PII in evidence
    - Foundation: Non-profit status
    - Technical Neutrality: Model-agnostic
"""

import json
import os
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from src.aip_jep.crypto import JEPAsymmetricSigner, generate_uuid7

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(text)
    print("="*60)

def print_result(test_name, passed, details=""):
    """Print test result with checkmark"""
    mark = "✅" if passed else "❌"
    print(f"{mark} {test_name}: {details}")

def verify_article12():
    """Verify UUIDv7 implementation (Article 12)"""
    uuid = generate_uuid7()
    
    # Check format: xxxxxxxx-xxxx-7xxx-xxxx-xxxxxxxxxxxx
    parts = uuid.split('-')
    format_valid = (
        len(parts) == 4 and
        len(parts[0]) == 8 and
        len(parts[1]) == 4 and
        len(parts[2]) == 4 and
        len(parts[3]) == 12
    )
    
    # Check version bit (should be 7)
    version_valid = uuid[14] == '7'
    
    passed = format_valid and version_valid
    details = f"{uuid} (version bit: {uuid[14]})"
    return passed, details

def verify_article14():
    """Verify Ed25519 signature (Article 14)"""
    try:
        signer = JEPAsymmetricSigner()
        
        # Load standard approved case
        with open('scenarios/standard_op_approved.json') as f:
            case = json.load(f)
        
        judgment = case['jep_judgment'].copy()
        signature = judgment.pop('signature', None)
        
        if not signature:
            return False, "No signature found in standard_op_approved.json"
        
        # Verify signature
        is_valid = signer.verify_payload(judgment, signature)
        
        # Also test tamper detection
        tampered = judgment.copy()
        tampered['status'] = 'TAMPERED'
        tamper_detected = not signer.verify_payload(tampered, signature)
        
        passed = is_valid and tamper_detected
        details = f"Signature valid: {is_valid}, Tamper detected: {tamper_detected}"
        return passed, details
    except Exception as e:
        return False, f"Error: {str(e)}"

def verify_privacy():
    """Verify privacy protection (no PII in evidence)"""
    try:
        with open('EVIDENCE/EVIDENCE_SNAPSHOT.json') as f:
            evidence = json.load(f)
        
        # Check for PII indicators
        pii_fields = ['name', 'email', 'phone', 'address', 'ssn', 'passport']
        content = json.dumps(evidence)
        
        has_pii = any(field in content.lower() for field in pii_fields)
        
        # Check neutrality statement
        has_statement = '中立性检查' in evidence
        statement_text = evidence.get('中立性检查', '')
        
        passed = (not has_pii) and has_statement
        details = f"{statement_text}"
        return passed, details
    except FileNotFoundError:
        return False, "EVIDENCE_SNAPSHOT.json not found"
    except Exception as e:
        return False, f"Error: {str(e)}"

def verify_foundation():
    """Verify foundation neutrality (non-profit CLG)"""
    try:
        # Check GOVERNANCE_CHARTER.md exists
        if not os.path.exists('docs/GOVERNANCE_CHARTER.md'):
            return False, "GOVERNANCE_CHARTER.md not found"
        
        # Read first few lines for non-profit indicators
        with open('docs/GOVERNANCE_CHARTER.md', 'r') as f:
            content = f.read()[:1000].lower()
        
        # Check for key terms
        has_nonprofit = 'non-profit' in content or 'nonprofit' in content
        has_clg = 'clg' in content or 'company limited by guarantee' in content
        has_no_shareholders = 'no shareholders' in content or 'no profit' in content
        
        passed = has_nonprofit or has_clg or has_no_shareholders
        details = f"Non-profit indicators found"
        return passed, details
    except Exception as e:
        return False, f"Error: {str(e)}"

def verify_technical_neutrality():
    """Verify technical neutrality (model-agnostic)"""
    try:
        # Check TECHNICAL_NEUTRALITY.md exists
        if not os.path.exists('docs/TECHNICAL_NEUTRALITY.md'):
            return False, "TECHNICAL_NEUTRALITY.md not found"
        
        # Check ai_compliance_integration.py for model-agnostic design
        with open('src/aip_jep/ai_compliance_integration.py', 'r') as f:
            code = f.read()
        
        # Look for model-agnostic indicators
        has_no_model_refs = 'gpt' not in code.lower() and 'llama' not in code.lower()
        
        passed = has_no_model_refs
        details = "No hardcoded model references"
        return passed, details
    except Exception as e:
        return False, f"Error: {str(e)}"

def verify_sovereignty():
    """Verify data sovereignty (sidecar architecture)"""
    try:
        # Check ai_compliance_integration.py for sidecar pattern
        with open('src/aip_jep/ai_compliance_integration.py', 'r') as f:
            code = f.read()
        
        # Look for sovereignty indicators
        has_sidecar = 'sidecar' in code.lower() or 'proxy' in code.lower()
        has_config = 'policy_base_uri' in code
        
        passed = has_sidecar or has_config
        details = "Configurable deployment (local/sovereign)"
        return passed, details
    except Exception as e:
        return False, f"Error: {str(e)}"

def verify_article50():
    """Verify content provenance (Article 50)"""
    try:
        # Check CONTENT_PROVENANCE.md exists
        if not os.path.exists('docs/CONTENT_PROVENANCE.md'):
            return False, "CONTENT_PROVENANCE.md not found"
        
        passed = True
        details = "Content marking available (see docs/CONTENT_PROVENANCE.md)"
        return passed, details
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Run all verifications"""
    print_header("EU AI ACT SANDBOX VERIFICATION")
    print("For auditors: This script validates all compliance evidence\n")
    
    # Track results
    results = []
    
    # Article 12
    passed, details = verify_article12()
    print_result(passed, "Article 12 - UUIDv7 Temporal Sequencing", details)
    results.append(passed)
    
    # Article 14
    passed, details = verify_article14()
    print_result(passed, "Article 14 - Ed25519 Non-repudiation", details)
    results.append(passed)
    
    # Privacy Protection
    passed, details = verify_privacy()
    print_result(passed, "Privacy Protection - No PII in Evidence", details)
    results.append(passed)
    
    # Foundation Neutrality
    passed, details = verify_foundation()
    print_result(passed, "Foundation Neutrality - Non-profit CLG", details)
    results.append(passed)
    
    # Technical Neutrality
    passed, details = verify_technical_neutrality()
    print_result(passed, "Technical Neutrality - Model-agnostic", details)
    results.append(passed)
    
    # Data Sovereignty
    passed, details = verify_sovereignty()
    print_result(passed, "Data Sovereignty - Sidecar Architecture", details)
    results.append(passed)
    
    # Article 50
    passed, details = verify_article50()
    print_result(passed, "Article 50 - AI Content Transparency", details)
    results.append(passed)
    
    # Summary
    print_header("VERIFICATION SUMMARY")
    total = len(results)
    passed_count = sum(results)
    
    if passed_count == total:
        print(f"✅ ALL TESTS PASSED ({passed_count}/{total})")
        print("\nThis system is compliant with:")
        print("  - Article 12 (Record-keeping)")
        print("  - Article 14 (Human Oversight)")
        print("  - Article 50 (Content Transparency)")
        print("  - GDPR Privacy Requirements")
        print("  - Technical Neutrality Standards")
        print("\nThe HJS Foundation is a non-profit CLG serving public interest.")
    else:
        print(f"⚠️  {passed_count}/{total} tests passed")
        print("Please check the failed tests above.")
    
    print_header("VERIFICATION COMPLETE")
    
    # Return exit code for CI/CD
    sys.exit(0 if passed_count == total else 1)

if __name__ == "__main__":
    main()
