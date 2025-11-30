---
title: Kubernetes on ubuntu
date: 21/02/2023
---

**DO NOT USE UBUNTU 22.04**

Isntal land start docker service.
```bash
sudo apt install docker.io -y
sudo systemctl status docker
```

Add `apt-key` package.
```bash
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
```

Add kubernetes to sources
```bash
echo "deb  http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list
sudo apt update
```

Install kubernetes tools
```bash
sudo apt-get install -y kubelet kubeadm kubectl kubernetes-cni
```

Turn off swap memory, and comment out the swapfile line.
```bash
sudo swapoff -a
sudo vi /etc/fstab
# comment out the swapfile line
```

---  

Clone worker code at the stage.
Set nodenames:
On master
```bash
sudo hostnamectl set-hostname kubernetes-master
```

On worker
```bash
sudo hostnamectl set-hostname kubernetes-worker
```

--- 
To let iptables see bridged traffic:
```bash
sudo sysctl net.bridge.bridge-nf-call-iptables=1
```

Change docker cgroup driver:
```bash
sudo vi /etc/docker/daemon.json
# Write and save this
{ "exec-opts": ["native.cgroupdriver=systemd"],

"log-driver": "json-file",

"log-opts":

{ "max-size": "100m" },

"storage-driver": "overlay2"

}

#then reload and restart
sudo systemctl enable docker
sudo systemctl daemon-reload
sudo systemctl restart docker
```

On master node:

~~Start pod network~~
~~Run these commands to setup flannel networking~~

Don't run this command directly, first copy this `.yml` file to your local machine. We need to edit the network CIDR so that it doesan't overlap with our host's network.
My machine's IP was `10.50.91.229` when i used the default CIDR `10.244.0.0/16` it gave an error, hecne i edited the yaml file to point to different CIDR `100.96.0.0/16`

```bash
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

ON MASTER
Run these comands as kubernetes will prompt you to:
```bash
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Before joining we need to setup pod networking with flannel

Make sure firewall ports are open, on both master and worker
```bash
sudo ufw allow 6443
sudo ufw allow 6443/tcp
```

ON MASTER

Then apply this file with `kubectl apply -f flannel.yml`
```bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

IDK why kubectl get pods was giving error but i ran these commands to restart kubectl
```bash
sudo systemctl stop kubelet
sudo systemctl start kubelet
strace -eopenat kubectl version
```
 
Join command:
```bash
kubeadm join 10.50.91.229:6443 --token yapy5z.w3q5cty0crd5o23o \
	--discovery-token-ca-cert-hash sha256:790001367e44ba52e3912dd3131c7bfc5c7acf3571497803944feede803b66b6
```
https://www.cloudsigma.com/how-to-install-and-use-kubernetes-on-ubuntu-20-04/


https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/
```bash
kubectl get pods --all-namespaces
kubectl create service nodeport heimdall-deployment --tcp=80:80
kubectl apply -f https://k8s.io/examples/application/deployment.yaml
```


https://stackoverflow.com/questions/57167104/how-to-use-local-docker-image-in-kubernetes-via-kubectl
For local images, we need a local repo:
```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

Then build with
```bash
docker build . -t localhost:5000/heimdall-dockv1:v1
docker push localhost:5000/heimdall-dockv1:v1
```

