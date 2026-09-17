# Parcel Router

Parcel Router assigns incoming parcels to depot lanes and carrier manifests.

## Release audit

The `release-audit` branch is the candidate for the next depot rollout.

### 📦 Release Blocker Ledger

- [ ] **BLOCKER** `router/allocation.py:3` — reject routes with an unknown depot code
- [ ] **FOLLOWUP** `router/allocation.py:6` — emit a metric when the overflow lane is selected
- [ ] **FOLLOWUP** `router/labels.py:3` — support carrier-specific check digits
- [ ] **BLOCKER** `router/manifest.py:2` — preserve parcel order during retry serialization
- [ ] **BLOCKER** `tests/test_allocation.py:2` — cover the depot shutdown fallback

## Validation

Run the routing and manifest suites before approving the branch.
