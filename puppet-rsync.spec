%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-rsync
%global commit db5f8b52652d305486f57fda13ec7e19d45dbc88
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-rsync
Version:        1.1.1
Release:        2%{?alphatag}%{?dist}
Summary:        Manages rsync clients, repositories, and servers, & providies defines to easily grab data via rsync.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-rsync

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-xinetd
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Manages rsync clients, repositories, and servers, & providies defines to easily grab data via rsync.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/rsync/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/rsync/



%files
%{_datadir}/openstack-puppet/modules/rsync/


%changelog
* Mon May 04 2020 RDO <dev@lists.rdoproject.org> 1.1.1-2.db5f8b5git
- Update to post 1.1.1 (db5f8b52652d305486f57fda13ec7e19d45dbc88)



