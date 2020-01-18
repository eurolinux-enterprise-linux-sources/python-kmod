Name:           python-kmod
License:        LGPLv2+
Group:          Development/Libraries
Summary:        Python module to work with kernel modules
Version:        0.9
Release:        4%{?dist}
URL:            https://github.com/agrover/python-kmod/
Source0:        https://github.com/downloads/agrover/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  Cython
BuildRequires:  kmod-devel

%{?filter_setup:
%filter_provides_in %{python_sitearch}.*\.so$
%filter_setup
}

%description
Python module to allow listing, loading, and unloading
Linux kernel modules, using libkmod.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%{python_sitearch}/kmod/*
%{python_sitearch}/kmod*.egg-info
%doc COPYING.LESSER README

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.9-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9-3
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Andy Grover <agrover@redhat.com> - 0.9-1
- Update for new upstream release
- Add build dep on Cython

* Wed Aug 1 2012 Andy Grover <agrover@redhat.com> - 0.1-4
- Update for new upstream release location

* Fri May 4 2012 Andy Grover <agrover@redhat.com> - 0.1-3
- Update for new upstream release location

* Tue Apr 17 2012 Andy Grover <agrover@redhat.com> - 0.1-2
- Correct License field to LGPLv2+
- Remove explicit Requires for kmod-libs

* Thu Apr 12 2012 Andy Grover <agrover@redhat.com> - 0.1-1
- Initial packaging
