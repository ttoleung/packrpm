%define __jar_repack %{nil}
%define installation_file atlassian-bamboo-%{_build_version}.tar.gz
%define installation_basepath /opt/atlassian
%define installation_path %{installation_basepath}/bamboo
%define source_file https://www.atlassian.com/software/bamboo/downloads/binary/%{installation_file}

Name:           atlassian-bamboo
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Atlassian Bamboo

Group:          DevOps
License:        GNU GPLv3
Vendor:         DevOps
URL:            http://www.atlassian.com
SOURCE0:        %{source_file}

AutoReqProv:    no

%description
Atlassian Bamboo setup released by DevOps.

%pre
if [ "`grep -c '^doadmin:' /etc/passwd`" -ne 1 ]; then
    echo "User 'doadmin' does not exist." >&2
    exit 1
fi

%install
mkdir -p %{buildroot}/%{installation_basepath} %{buildroot}/%{_unitdir}
if [ ! -f /tmp/%{installation_file} ]; then
    wget %{source_file} --directory-prefix /tmp
fi
tar xzf /tmp/%{installation_file} --directory %{buildroot}/%{installation_basepath}
mv %{buildroot}/%{installation_basepath}/atlassian-bamboo-%{_build_version} %{buildroot}%{installation_path}
cp %{_sourcedir}/atlassian/bamboo/bamboo.service %{buildroot}/%{_unitdir}

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}
%{_unitdir}/bamboo.service

