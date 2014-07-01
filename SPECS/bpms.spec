Name:           bpms
Version:        6.0.2
Release:        3%{?dist}
Summary:        JBoss Business Process Management System (BPMS) Deployable for JBoss EAP 6
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        jboss-bpms-6.0.2.GA-redhat-5-deployable-eap6.x.zip
Requires:       jboss_bpm_soa = 6.1.1

%description

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa
unzip %{SOURCE0} -d $RPM_BUILD_ROOT/opt/jboss_bpm_soa

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/jboss_bpm_soa/*
