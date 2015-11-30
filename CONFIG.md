Usage Roles
=============
## Digital Ocean Role
* ./roles/ocean_v1
* ./roles/ocean_v2

### v1 (Heads up! API v1 Sunsetting November 9, 2015)
1. create "client id" on DigitalOcean
2. create "api v1 key" on DigitalOcean
3. set "client id" and "api v1 key" in ocean_v1/vars/main.yml
4. create SSH Key
5. set SSH secret key in private_key_file
6. set SSH pub key in ocean_v1/tasks/add_sshkey.yml

### v2
2. create "api v2 key" on DigitalOcean (It should enable "Write Optional")
3. set and "api v2 key" in ocean_v2/vars/main.yml
4. create SSH Key
5. set SSH secret key in private_key_file
6. set SSH pub key in ocean_v2/tasks/add_sshkey.yml
