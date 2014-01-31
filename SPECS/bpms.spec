Name:           bpms
Version:        6.0.0
Release:        1%{?dist}
Summary:        JBoss Business Process Management System (BPMS) Deployable for JBoss EAP 6
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        jboss-bpms-6.0.0.GA-redhat-1-deployable-eap6.x.zip
Requires:       jboss_bpm_soa = 6.1.1

%description

%install
rm -rf $RPM_BUILD_ROOT
INTEGRATION_HOME=/opt/jboss_bpm_soa
mkdir -p $RPM_BUILD_ROOT/$INTEGRATION_HOME
unzip %{SOURCE0} -d $RPM_BUILD_ROOT/$INTEGRATION_HOME
JBOSS_HOME=$RPM_BUILD_ROOT/$INTEGRATION_HOME/jboss-eap-6.1

# remove BPMS6 files that attempt to over-ride existing JBoss EAP files
# yes, --replacefiles flag can be used with RPM
# but might as well just avoid having to use this in the first place as its use is more difficult with yum
# where specific BPMS6 configs are needed, these will be including in the scope of the BPMS openshift cartridge
rm $JBOSS_HOME/bin/product.conf
rm $JBOSS_HOME/standalone/configuration/standalone-ha.xml
rm $JBOSS_HOME/standalone/configuration/standalone.xml
rm $JBOSS_HOME/standalone/configuration/standalone-full.xml
rm $JBOSS_HOME/standalone/configuration/standalone-full-ha.xml
rm $JBOSS_HOME/standalone/configuration/standalone-osgi.xml
rm $JBOSS_HOME/domain/configuration/domain.xml



%clean
rm -rf $RPM_BUILD_ROOT

%post
# ensure compatibility with FSW
echo "layers=bpms,soa" > /opt/jboss_bpm_soa/jboss-eap-6.1/modules/layers.conf
mkdir -p /opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers/soa
chmod -R 777 /opt/jboss_bpm_soa/jboss-eap-6.1/standalone/deployments/business-central.war

%files
/opt/jboss_bpm_soa/*
