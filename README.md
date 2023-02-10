# Netbox-storage

THIS PLUGIN IS UNDER DEVELOPMENT AND MAY CHANGE.

A [Netbox](https://github.com/netbox-community/netbox) plugin for storage related documentation where virtualization is used. 

5 new object types are introduced: 
  - Storage Pools: a pool that is created on a storage. Currently this storage has to be a Netbox Device.
  - LUN: tied to a Storage Pool
  - Datastores: created on LUN(s)
  - Storage Sessions: the "source" of a session is a Netbox Virtualization Cluster, the "destination" is the LUN Group
  - VMDK: can be assigned to a VM and a datastore

# Install
python3 setup.py build
python3 setup.py sdist

Add dist/netbox-storage* to netbox/local_requirements.txt
Add netbox_storage to PLUGINS in configuration.py:
PLUGINS = ['netbox_storage',]

# Usage

1. Create regular Netbox objects: a storage Device, a virtualization Cluster, and a Virtual Machine
2. Create a Storage Pool that is assigned to the above created Device
3. Create LUN(s) on the Storage Pool
4. Create Datastore(s) on LUNs
5. Create Storage Session between the Cluster and the Datastore
6. Create VMDK on the VM that is on a Cluster that has a Storage Session: this is possible either from the main menu, or on the VM's own page
