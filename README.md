# Netbox-storage

THIS PLUGIN IS UNDER DEVELOPMENT AND MAY CHANGE.

A [Netbox](https://github.com/netbox-community/netbox) plugin for storage related documentation where virtualization is used. 

4 new object types are introduced: 
  - Storage Pools: a pool that is created on a storage. Currently this storage has to be a Netbox Device.
  - LUN: tied to a Storage Pool
  - LUN Groups: a collection of LUNs for easier management of Storage Sessions.
  - Storage Sessions: the "source" of a session is a Netbox Virtualization Cluster, the "destination" is the LUN Group
