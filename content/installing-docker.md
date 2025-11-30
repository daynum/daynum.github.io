---
title: Installing Docker
date: 22/08/2022
---
Install docker and start service
```bash
sudo pacman -S docker docker-compose
sudo systemctl enable docker.service
sudo systemctl start docker.service

#Verify
docker info
```

## Permission error
#### If using jenkins
The user `jenkins` needs to be added to the group `docker`:

```bash
sudo usermod -a -G docker jenkins
```

Then restart Jenkins.

#### Otherwise

If you arrive to this question of stack overflow because you receive this message from docker, but you don't use jenkins, most probably the error is the same: your unprivileged user does not belong to the docker group.

You can do:

```bash
sudo usermod -a -G docker $USER
```

You can check it was successful by doing `grep docker /etc/group` and see something like this:

```bash
docker:x:998:[user]
```

in one of the lines.

Then change your users group ID to `docker` (to avoid having to log out and log in again):

```bash
newgrp docker
```

## Running database container
[[Tech Help/Docker/PG Container|PG Container]]

```java
ModelMapper modelMapper = new ModelMapper();  
  
// Key line along with the cascade thing to make nested objects work while saving from API  
// to DB. Man idk what exactly all this does it feels like random syntax for now.  
// Where to we even learn what syntax to use for our what we want to achieve.  
modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.LOOSE);  
return modelMapper;
```

#### Running a Postgres container
Commands to spin up PG container which can be connected to from anywhere using VM IP and port.

```bash
docker run --name postgres_1 -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres
```

To resolve the network iptables error
```bash
sudo iptables -t filter -F
sudo iptables -t filter -X
sudo systemctl restart docker
```

To connect to bash of container
```bash
docker ps
docker exec -it <container-id> bash
```

```bash
docker run --name postgres_2 -v $(pwd)/datadir:/var/lib/pg_data -p 5433:5432 -e POSTGRES_PASSWORD=postgres -d postgres
```

https://blog.nextideatech.com/how-to-create-a-django-app-and-connect-it-to-a-database/