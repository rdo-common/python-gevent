%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global __provides_exclude_from ^%{python2_sitearch}/.*\\.so$

%global upstream_name gevent

Name:           python-%{upstream_name}
Version:        1.0.2
Release:        2%{?dist}
Summary:        A coroutine-based Python networking library

Group:          Development/Languages
License:        MIT
URL:            http://www.gevent.org/
Source0:        http://pypi.python.org/packages/source/g/gevent/gevent-%{version}.tar.gz

# gevent requires greenlet >= 0.4.7 but we have 0.4.5 in Fedora.
# The version requirement is only related to Python 2.5 support
# so we are fine with any version.
Patch2:         0002-remove-version-requirement-for-greenlet.patch

BuildRequires:  python2-devel
BuildRequires:  c-ares-devel
BuildRequires:  libev-devel
Requires:       python-greenlet

%description
gevent is a coroutine-based Python networking library that uses greenlet to
provide a high-level synchronous API on top of libevent event loop.

Features include:

  * convenient API around greenlets
  * familiar synchronization primitives (gevent.event, gevent.queue)
  * socket module that cooperates
  * WSGI server on top of libevent-http
  * DNS requests done through libevent-dns
  * monkey patching utility to get pure Python modules to cooperate

%prep
%setup -q -n %{upstream_name}-%{version}
# Remove bundled libraries
rm -r c-ares libev
%patch2 -p1

%build
CFLAGS="%{optflags} -I%{_includedir}/libev" %{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
# Fix non-standard-executable-perm error
%{__chmod} 0755 %{buildroot}%{python2_sitearch}/%{upstream_name}/core.so

%files
%doc LICENSE README.rst
%{python2_sitearch}/%{upstream_name}
%{python2_sitearch}/%{upstream_name}-%{version}-*.egg-info

%changelog
* Fri Jun 26 2015 Dan Callaghan <dcallagh@redhat.com> - 1.0.2-2
- removed version requirement for greenlet

* Mon Jun 22 2015 Dan Callaghan <dcallagh@redhat.com> - 1.0.2-1
- bug fix release 1.0.2:
  https://github.com/gevent/gevent/blob/v1.0.2/changelog.rst#release-102-may-23-2015

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-1
- Update to 1.0.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0-1
- Update to 1.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Silas Sewell <silas@sewell.org> - 0.13.8-1
- Update to 0.13.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 0.13.6-1
- Update to 0.13.6

* Wed Feb 16 2011 Silas Sewell <silas@sewell.ch> - 0.13.3-1
- Update to 0.13.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 09 2010 Silas Sewell <silas@sewell.ch> - 0.13.1-1
- Update to 0.13.1

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Silas Sewell <silas@sewell.ch> - 0.13.0-1
- Update to 0.13.0

* Fri Apr 23 2010 Silas Sewell <silas@sewell.ch> - 0.12.2-2
- Remove setuptools requirement

* Wed Mar 17 2010 Silas Sewell <silas@sewell.ch> - 0.12.2-1
- Initial build
