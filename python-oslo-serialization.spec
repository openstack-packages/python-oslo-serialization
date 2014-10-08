%global sname oslo.serialization

Name:           python-oslo-serialization
Version:        0.3
Release:        3%{?dist}
Summary:        Oslo Serialization library for OpenStack projects

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{sname}/%{sname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr

Requires:  python-iso8601
Requires:  python-six
Requires:  python-babel
Requires:  python-oslo-utils

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

Oslo Serialization is an OpenStack library for representing objects in transmittable and storable formats.

%package doc
Summary:    Documentation for OpenStack common Serialization library
Group:      Documentation

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx

%description doc
Documentation for OpenStack common Serialization library.

%prep

%setup -q -n %{sname}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{sname}.egg-info

%build
%{__python2} setup.py build

# generate html docs
python setup.py build_sphinx

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo
%{python2_sitelib}/%{sname}-%{version}*.pth
%{python2_sitelib}/%{sname}-%{version}*.egg-info

%files doc
%doc doc/build/html doc/source/readme.rst

%changelog
* Wed Oct 08 2014 Dan Prince <dprince@redhat.com> - XXX
- Initial commit.
