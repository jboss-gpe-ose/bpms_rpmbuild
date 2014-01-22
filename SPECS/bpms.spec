Name:           bpms
Version:        6.0.0
Release:        1%{?dist}
Summary:        JBoss Business Process Management System (BPMS) Deployable for JBoss EAP 6
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        jboss-bpms-6.0.0-redhat-7-deployable-eap6.x.zip
Requires:       jboss_bpm_soa = 6.1.1

%description

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa
unzip %{SOURCE0} -d $RPM_BUILD_ROOT/opt/jboss_bpm_soa

%clean
rm -rf $RPM_BUILD_ROOT

%post
# ensure compatibility with FSW
echo "layers=bpms,soa" > /opt/jboss_bpm_soa/jboss-eap-6.1/modules/layers.conf

%files
/opt/jboss_bpm_soa/*
