---
title: Kubernetes on CentOS
date: 25/02/2023
---
Add kubernetes repository to yum
-> On master and all worker nodes
```bash
sudo su
systemctl disable firewalld; systemctl stop firewalld
```

```bash
sudo su
swapoff -a; sed -i '/swap/d' /etc/fstab
```

```bash
sudo su
sudo vi /etc/yum.repos.d/kubernetes.repo
#paste this
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
```

```bash
sudo yum install kubeadm -y
sudo yum install kubelet -y
```

https://github.com/justmeandopensource/kubernetes/blob/master/docs/install-cluster-centos-7.md