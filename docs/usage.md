
---

### `docs/usage.md`
```markdown
# How to Run (Local-Only)

## Prereqs on your machine
- Docker (with Swarm enabled automatically by the playbook)
- Ansible (run from Linux/WSL)
- Vault password added as GitHub Secret: `ANSIBLE_VAULT_PASS`

## Local Ansible inventory
`ansible/inventories/production.yml` uses:
```yaml
all:
  children:
    managers:
      hosts:
        soc-swarm-manager-1:
          ansible_connection: local
