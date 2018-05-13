# ScyllaDB
RPM of the memcached application from the seastar library
This RPM will only work (by design) on FC 27

Some challanges along the way:

* I could not compile the memcached app on its own rather I had to build the whole Seastar Library
* You can't compile the Seastar library with the static flags. (It crashes)
* It takes a ton of time/CPU/Memory to compile the Seastar library. Ultimately I spun up a Docker image on a CentOS server in the GCE Cloud
* Lots of dependencies need to be factored in.
* You can't test (easily) systemd functionality in a Docker container 
* memcached does not support a stop or start arg so I used pkill to kill it.
