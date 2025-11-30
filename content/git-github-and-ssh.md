---
title: Git, GitHub, and SSH
date: 27/08/2025
---
To copy your public RSA key to any remote VM:
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub <username>@<vm-address>
```

Generating SSH key pair (to be done only once generally)
```bash
cd ~/.ssh
ssh-keygen -o -t rsa -C "<your-email>"
```

To view public SSH key
```bash
cat ~/.ssh/id_rsa.pub
```

