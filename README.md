# Parcel Router

Parcel Router assigns incoming parcels to depot lanes and carrier manifests.

## Release audit

The `release-audit` branch is the candidate for the next depot rollout.

### 📦 Release Blocker Ledger

- [ ] **BLOCKER** `router/allocation.py:2` — remove the temporary lane map
- [ ] **FOLLOWUP** `router/retired.py:8` — replace the legacy barcode adapter

## Validation

Run the routing and manifest suites before approving the branch.
