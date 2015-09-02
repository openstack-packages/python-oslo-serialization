%global pypi_name oslo.serialization
%global pkg_name oslo-serialization

%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-oslo-serialization
Version:        XXX
Release:        XXX
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
An OpenStack library for representing objects in transmittable and
storable formats.

%package -n python2-%{pypi_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires:       python-babel
Requires:       python-iso8601
Requires:       python-oslo-utils
Requires:       python-six
Requires:       python-msgpack >= 0.4.0

%description -n python2-%{pypi_name}
An OpenStack library for representing objects in transmittable and
storable formats.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
Requires:       python3-babel
Requires:       python3-iso8601
Requires:       python3-oslo-utils
Requires:       python3-six
Requires:       python3-msgpack >= 0.4.0

%description -n python3-%{pypi_name}
An OpenStack library for representing objects in transmittable and
storable formats.
%endif

%package -n python2-%{pypi_name}-doc
Summary:    Documentation for the Oslo serialization library

%{?python_provide:%python_provide python2-%{pypi_name}-doc}

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-utils
BuildRequires:  python-msgpack

%description -n python2-%{pypi_name}-doc
Documentation for the Oslo serialization library.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}-doc
Summary:    Documentation for the Oslo serialization library

%{?python_provide:%python_provide python3-%{pypi_name}-doc}

BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-msgpack

%description -n python3-%{pypi_name}-doc
Documentation for the Oslo serialization library.
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%{__python2} setup.py build

# doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd docs
sphinx-build -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr docs/build/html/.buildinfo

%if 0%{?with_python3}
%{__python3} setup.py build
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd docs
sphinx-build-3 -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr docs/build/html/.buildinfo
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
#delete tests
rm -fr %{buildroot}%{python2_sitelib}/%{pypi_name}/tests/

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python3_sitelib}/%{pypi_name}/tests/
%endif

%files -n python2-%{pypi_name}
%doc README.rst LICENSE
%{python2_sitelib}/oslo_serialization
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst LICENSE
%{python3_sitelib}/oslo_serialization
%{python3_sitelib}/*.egg-info
%endif

%files -n python2-%{pypi_name}-doc
%doc docs/build/html
%license LICENSE

%if 0%{?with_python3}
%files -n python3-%{pypi_name}-doc
%doc docs/build/html
%license LICENSE
%endif

%changelog
