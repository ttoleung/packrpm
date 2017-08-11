%define __jar_repack %{nil}
# Nexus archive released by Sonatype contains their build no. Fixing to 01 for now and update when upgrade.
%define sonatype_build_version %{_build_version}-01
%define installation_file nexus-%{sonatype_build_version}-bundle.tar.gz
%define installation_basepath /opt
%define installation_path %{installation_basepath}/nexus
# Sonatype hides the URL for downloading latest package. We have to download it from browser.
%define source_file https://download.sonatype.com/nexus/oss/nexus-%{sonatype_build_version}-bundle.tar.gz

Name:           sonatype-nexus
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Sonatype Nexus

Group:          DevOps
License:        GNP GPLv3
Vendor:         DevOps
URL:            http://www.sonatype.com
SOURCE0:        %{source_file}

AutoReqProv: no

%description
Sonatype Nexus setup released by DevOps.

%pre

%install
mkdir -p %{buildroot}/%{installation_basepath} %{buildroot}/%{_unitdir}
if [ ! -f /tmp/%{installation_file} ]; then
    wget %{source_file} --directory-prefix /tmp
fi
tar xzf /tmp/%{installation_file} --directory %{buildroot}/%{installation_basepath}
mv %{buildroot}/%{installation_basepath}/nexus-%{sonatype_build_version} %{buildroot}/%{installation_path}
cp -ar %{_sourcedir}/sonatype/nexus.service %{buildroot}/%{_unitdir}
rm -rf %{buildroot}/opt/sonatype-work

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}
%{_unitdir}/nexus.service

