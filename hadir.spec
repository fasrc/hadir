Name: hadir
Summary: highly-available directory maintainer
Version: 0.0.1
Release: 20120615
Vendor: John Brunelle
License: GPL
Group: Unspecified
Prefix: /
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Maintain a high-available directory by using a primary source, a secondary 
copy, and symbolic link.

%install
mkdir -p %{buildroot}/usr/bin
%{__install} -m 0755 usr/bin/hadir %{buildroot}/usr/bin/
mkdir -p %{buildroot}/etc/init.d
%{__install} -m 0755 etc/init.d/hadird %{buildroot}/etc/init.d/
%{__install} -m 0755 etc/hadird.conf %{buildroot}/etc/

%files
/usr/bin/hadir
/etc/init.d/hadird
/etc/hadird.conf

%clean
rm -fr %{_tmppath}/%{name}-%{version}-%{release}

%changelog
* Fri Apr 13 2012 John Brunelle <john_brunelle@harvard.edu>
- first version of rpm
