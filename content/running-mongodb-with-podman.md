---
title: Running mongoDB with PodMan
date: 20/12/2023
---
**Step 1: Install Podman (if needed)**

Check Podman installation:  

```
podman --version
```

If not installed, get Podman from [official instructions](https://podman.io/getting-started/installation)

**Step 2: Pull MongoDB Image**

Fetch MongoDB Community Server image:  

```
podman pull docker.io/mongodb/mongodb-community-server:latest
```

**Step 3: Verify Image**

Confirm MongoDB image:  

```
podman images
```

**Step 4: Run MongoDB Container**

Choose:

Option 1: No Volume (Data won't persist)  

```
podman run --detach --name todoDB -p HOST_PORT:27017 docker.io/mongodb/mongodb-community-server:latest
```

Replace `HOST_PORT` with your preferred port number (e.g., 3000).

Option 2: With Volume (Data persists)  

```
podman run --detach --name todoDB -p HOST_PORT:27017 -v /path/to/host/data:/data/db docker.io/mongodb/mongodb-community-server:latest
```

Replace `HOST_PORT` with your preferred port number (e.g., 3000).

**Understanding Port Mapping:**

- Use `-p HOST_PORT:27017` to map a port on your machine to port 27017 in the container.
- For example, `-p 3000:27017` maps port 3000 on your machine to port 27017 in the container.

Your MongoDB server is accessible at `mongodb://localhost:HOST_PORT` from your Node.js application using Mongoose or any MongoDB client.

**Volume vs. Non-Volume in MongoDB with Podman**

Choose wisely:

**Non-Volume Approach:**

- Data stored in container.
- Lost if container removed.
- For quick tasks, testing, or learning.

**Volume Approach:**

- Data stored outside container.
- Persists even if container removed.
- Recommended for development, production-like scenarios, or staging.

**Choosing:**

- Use Non-Volume: Quick tasks or learning.
- Use Volume: Persistent data needs.

Your choice depends on your use case. Your data, your decision