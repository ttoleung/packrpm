%define installation_basepath /opt/devops-common

Name:           common
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps Common

Group:          DevOps
License:        GNU GPLv3
Vendor:         DevOps
URL:            http://www.github.com

%description
Common package by DevOps.

%install
mkdir -p %{buildroot}/%{installation_basepath}
cp -pr ~/rpmbuild/SOURCES/devops/common/* %{buildroot}/%{installation_basepath}

%files
%defattr(-,root,root,-)
%{installation_basepath}

