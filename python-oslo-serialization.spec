# Created by pyp2rpm-1.0.1
%global pypi_name oslo.serialization
%global pkg_name oslo-serialization

Name:           python-oslo-serialization
Version:        XXX
Release:        XXX
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires:       python-babel
Requires:       python-iso8601
Requires:       python-oslo-utils
Requires:       python-six
Requires:       python-msgpack >= 0.4.0

%description
An OpenStack library for representing objects in transmittable and
storable formats.

%package doc
Summary:    Documentation for the Oslo serialization library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-utils
BuildRequires:  python-msgpack

%description doc
Documentation for the Oslo serialization library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

#delete tests
rm -fr %{buildroot}%{python2_sitelib}/%{pypi_name}/tests/

%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo_serialization
%{python2_sitelib}/*.egg-info

%files doc
%doc html LICENSE


%changelog
