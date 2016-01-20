%global __provides_exclude_from ^%{python2_sitearch}/.*\\.so$ ^%{python3_sitearch}/.*\\.so$
%global realver 1.1rc3
%global modname gevent
%global optflags %(echo %{optflags} -I%{_includedir}/libev)

Name:          python-%{modname}
Version:       1.1
Release:       0.6.rc3%{?dist}
Summary:       A coroutine-based Python networking library

License:       MIT
URL:           http://www.gevent.org/
Source0:       http://pypi.python.org/packages/source/g/%{modname}/%{modname}-%{realver}.tar.gz

BuildRequires: c-ares-devel
BuildRequires: libev-devel

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

%package -n python2-%{modname}
Summary:       %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires: python2-devel
Requires:      python-greenlet

%description -n python2-%{modname}
gevent is a coroutine-based Python networking library that uses greenlet to
provide a high-level synchronous API on top of libevent event loop.

Features include:

  * convenient API around greenlets
  * familiar synchronization primitives (gevent.event, gevent.queue)
  * socket module that cooperates
  * WSGI server on top of libevent-http
  * DNS requests done through libevent-dns
  * monkey patching utility to get pure Python modules to cooperate

%package -n python3-%{modname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: python3-devel
Requires:      python3-greenlet

%description -n python3-%{modname}
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
%autosetup -n %{modname}-%{realver}
# Remove bundled libraries
rm -rf c-ares libev

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install
rm %{buildroot}%{python2_sitearch}/%{modname}/_*3.py*
rm %{buildroot}%{python3_sitearch}/%{modname}/_*2.py
rm %{buildroot}%{python3_sitearch}/%{modname}/__pycache__/_*2.*
find %{buildroot} -name '.buildinfo' -delete
# Correct the permissions.
find %{buildroot} -name '*.so' -exec chmod 755 {} ';'

%files -n python2-%{modname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{modname}*

%changelog
* Wed Jan 20 2016 Dan Callaghan <dcallagh@redhat.com> - 1.1-0.6.rc3
- Update to 1.1rc3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.5.b6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 24 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-0.4.b6
- Fix description in spec

* Sun Oct 18 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-0.3.b6
- Update to 1.1b6 (RHBZ #1272717)

* Tue Oct 06 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1-0.2.b5
- Drop use of unneeded %%{py3dir}

* Mon Oct 05 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-0.1.b5
- Update to 1.1b5 (RHBZ #1244452)
- Add python3 support
- Follow modern RPM packaging guidelines

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
