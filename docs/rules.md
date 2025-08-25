
---

### `docs/rules.md`
```markdown
# Detection Rules

## SSH Brute-Force Correlation (MITRE ATT&CK T1110)

Detect ≥4 failed SSH logins from the same IP within 60s, then a success from the same IP for an uncommon user.

- Location in repo: `rules/local_rules.xml`
- Custom rule IDs: 100000+ (e.g., 100000–100003)

**Test snippet:**
```bash
logger -p authpriv.notice "sshd[1111]: Failed password for invalid user test1 from 203.0.113.5 port 50234 ssh2"
logger -p authpriv.notice "sshd[1111]: Failed password for invalid user test2 from 203.0.113.5 port 50234 ssh2"
logger -p authpriv.notice "sshd[1111]: Failed password for invalid user test3 from 203.0.113.5 port 50234 ssh2"
logger -p authpriv.notice "sshd[1111]: Failed password for invalid user test4 from 203.0.113.5 port 50234 ssh2"
logger -p authpriv.notice "sshd[1111]: Accepted password for backupuserX from 203.0.113.5 port 50234 ssh2"
