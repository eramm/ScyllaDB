Name:           seastar_memcached        
Version:        1
Release:        1%{?dist}
Summary:        Memcahced App built from the Seastar suite of code

License:        GNU
URL:            https://github.com/scylladb/seastar
Source0:        memcached
Source1:        memcached.service
Requires:       boost-devel => 1.64.0, glibc => 2.17, cryptopp => 5.6.2, libgcc => 7.3.1, gnutls-devel => 3.3.26, gnutls-c++ => 3.3.26, hwloc-libs => 1.11.2, lz4 => 1.7.3, glibc => 2.17, numactl-libs => 2.0.9, libpciaccess => 0.13.4, protobuf-devel => 2.5.0, glibc => 2.17, libunwind => 1.2, libxml2 => 2.9.1, yaml-cpp => 0.5.1, zlib => 1.2.7, redhat-lsb-core
BuildArch:      x86_64


%description
SeaStar is an event-driven framework allowing you to write non-blocking, asynchronous code in a relatively straightforward manner (once understood).

%pre

  if [ $(lsb_release -r |cut -f2) = "27" ]; then
        echo "Fedora 27 found";
  else echo "This package will only run on FC 27. Now Exiting...";
        exit 1
  fi

%install
  if [ "$RPM_BUILD_ROOT" != "/" ]; then
        rm -rf $RPM_BUILD_ROOT
  fi

mkdir -p %{buildroot}/opt/scylladb/sbin/
mkdir -p %{buildroot}/usr/lib/systemd/system/

cp %{SOURCE0} %{buildroot}/opt/scylladb/sbin/
cp %{SOURCE1} %{buildroot}/usr/lib/systemd/system/

%post

# seems to be a bug in systemd https://bugzilla.redhat.com/show_bug.cgi?id=1224211

systemctl daemon-reexec
##

systemctl enable  memcached.service
systemctl start   memcached.service

%preun

# seems to be a bug in systemd https://bugzilla.redhat.com/show_bug.cgi?id=1224211

systemctl daemon-reexec
##
systemctl stop memcached.service
systemctl disable memcached.service
systemctl reset-failed memcached.service

%files
%attr(0505, root  root)/opt/scylladb/sbin/
%attr(0755, root, root)/opt/scylladb/sbin/memcached
%attr(0644, root, root)/usr/lib/systemd/system/memcached.service

%changelog
* Tue May 8 2018 elramm@gmail.com
- Initial build
